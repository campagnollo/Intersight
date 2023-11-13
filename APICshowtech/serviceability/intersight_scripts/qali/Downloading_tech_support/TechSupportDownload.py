import re
import tarfile
import os
import parameter as params
import glob



def techSupportDownload(applTS):
    """
    TechSupport Function
    """
    moidList = getDeviceMoidList(applTS)

    """
    Seeing if Tarball is downloaded
    """
    for moidElement in moidList:
        tarLoc = params.downloadDir + "bundle_{}.tar".format(moidElement)

        if not os.path.isfile(tarLoc):
            raise Exception("Tarball not downloaded")

        """
        Peeking inside tarball to see if files are available
        """
        nestedTarFileVerification(moidElement, tarLoc)

    return True


def nestedTarFileVerification(moidElement, tarLoc):
    reTar = [".*1of3\.tgz", ".*2of3\.tgz"]
    untar = []
    with tarfile.open(tarLoc, "r") as tarf:
        for i in tarf.getnames():
            untar.append(i)
    if untar[0] == 'manifest.json':
        untar.pop(0)
    for i in range(2):
        if not (bool(re.search(reTar[i], untar[i]))):
            raise Exception("Missing compressed file {} of 2 from moid {}".format(int(i + 1), moidElement))


def getDeviceMoidList(applTS):
    moidList = []
    if applTS.techsupport_files:
        for device in applTS.techsupport_files:
            downloadUrl = device.techsupport_download_url
            moidList.append(moidSlicer(downloadUrl))
    else:
        moidList.append(moidSlicer(applTS.techsupport_download_url))
    return moidList

def moidSlicer(downloadUrl):
    moidSlice = slice(-24, None, 1)
    moid = downloadUrl[moidSlice]
    return moid


def multiDeviceCountVerification(ExpectedReturn):
    dirlocation = params.downloadDir + "*.tar"
    devcounter = len(glob.glob(dirlocation))
    return devcounter == ExpectedReturn


def techSupportDownloadCleanup():
    downld = os.getcwd() + '/downloads'
    for file in os.listdir(downld):
        filePath = os.path.join(downld, file)
        os.unlink(filePath)

    return
