import parameter as params
from qali.intersight.api.intersight_api_client import IntersightApiClient
from qali.intersight import TechsupportmanagementDownloadApi
from qali.test.test import TestFail
def techSupportWorkFlow(apiClient: object, pid: object, serial: object, platformType: object, waitCount: object,
                        waitTime: object, platParam: object) -> object:
    """
    TechSupport Function
    :rtype: object
    """

    statusObj, tsBundle = retrieveTsBundles(apiClient, pid, platParam, platformType, serial,
                                  waitCount, waitTime)

    params.logger.info("Downloading techsupport moid:{0}".format(tsBundle.tech_support_status.moid))
    client = IntersightApiClient(
        host=params.downloadURL,
        private_key=apiClient.private_key_file,
        api_key_id=apiClient.api_key_id)
    api = TechsupportmanagementDownloadApi(client)
    downloadMoids = get_download_moids(statusObj)

    for downloadMoid in downloadMoids:
        tsBundleDownload = api.techsupportmanagement_downloads_moid_get(moid=downloadMoid,
                                                                        **{"_preload_content": False})
        fileName = params.downloadDir + "bundle_{}.tar".format(downloadMoid)
        with open(fileName, "wb") as openFile:
            openFile.write(tsBundleDownload.data)
            openFile.close()
            params.logger.info(
                "Download success and downloaded filename and location: {0}".format(fileName))
    apiClient.TechsupportmanagementTechSupportBundle(moid=tsBundle.moid).delete()
    params.logger.info("TechSupport Bundle with Moid {0} is deleted ".format(tsBundle.moid))

    return statusObj


def retrieveTsBundles(apiClient, pid, platParam, platformType, serial, waitCount, waitTime):
    tsBundle = apiClient.TechsupportmanagementTechSupportBundle(
        pid=pid, serial=serial, platform_type=platformType,
        platform_param=platParam).create()
    statusObj = checkTsBundleStatus(apiClient, tsBundle, waitCount, waitTime)
    return statusObj, tsBundle


def checkTsBundleStatus(apiClient, tsBundle, waitCount, waitTime):
    statusMoid = tsBundle.tech_support_status.moid
    statusObj = apiClient.techsupportmanagement_tech_support_status_api.moid_get(statusMoid)
    expectObj = apiClient.TechsupportmanagementTechSupportStatus()
    expectObj.status = 'Completed'
    exitObj = apiClient.TechsupportmanagementTechSupportStatus()
    exitObj.status = 'CollectionFailed'
    exit2Obj = apiClient.TechsupportmanagementTechSupportStatus()
    exit2Obj.status = 'UploadFailed'
    exit3Obj = apiClient.TechsupportmanagementTechSupportStatus()
    exit3Obj.status = 'TechsupportDownloadUrlCreationFailed'
    errMsg = statusObj.watch(expectObj, waitCount, waitTime, [exitObj, exit2Obj, exit3Obj])
    statusObj = apiClient.techsupportmanagement_tech_support_status_api.moid_get(statusMoid)
    if errMsg:
        raise Exception(errMsg)
    return statusObj


def get_download_moids(statusObj):
    tsfiles = statusObj.techsupport_files
    results = []
    if len(tsfiles) > 0:
        slice_obj = slice(-1, -25, -1)
        for file in tsfiles:
            downUrl = file['techsupport_download_url']
            backward_moid = downUrl[slice_obj]
            results.append(backward_moid[::-1])
        return results
    else:
        return [statusObj.moid]


def single_techSupportFiles(statusObj):
    if not statusObj.techsupport_files:
        return True
    else:
        raise TestFail("Single serial request returned one or more elements in the tech support files")



