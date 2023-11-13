import parameter as params
from TechsupportUtil import techSupportWorkFlow
from TechSupportDownload import techSupportDownload
from TechSupportDownload import techSupportDownloadCleanup
import TechsupportUtil

params.logger = globals().get("runtests_logger", None)


def test_setup():
    '''
        Test setup
    '''

    params.logger.info("In Test Case setup")


def run_test():
    '''
        Tech Support Collection for Appliance
    '''

    applTS = controllerSetup()
    params.logger.info("TechSupport Collection Completed for Appliance ")



    techSupportDownload(applTS)
    params.logger.info("Tar subfiles fully downloaded")


    """
    test for downloading tar files
    """
    TechsupportUtil.single_techSupportFiles(applTS)
    params.logger.info("Single request for serial returns empty tech support files as planned")



def controllerSetup():
    par = params.platformParamSingle['platformparams']
    applSerial = "FCH2102V1RX"
    applPid = "APIC"
    platType = "APIC"
    params.logger.info("Serial = {0} and PID = {1} of Appliance  ".format(applSerial, applPid))
    params.logger.info("\n\nStarting Techsupport Collection for Appliance ")
    applTS = techSupportWorkFlow(apiClient=params.adminHandle,
                                 pid=applPid, serial=applSerial,
                                 platformType=platType,
                                 waitCount=60, waitTime=60, platParam=par)
    return applTS


def test_cleanup():
    '''
    Function to test download and cleanup
    '''
    techSupportDownloadCleanup()

    params.logger.info("Test case clean up\n\n")
