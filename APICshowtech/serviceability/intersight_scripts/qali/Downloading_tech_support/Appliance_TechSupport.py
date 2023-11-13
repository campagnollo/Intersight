from qali.test.test import TestFail
import parameter as params
from TechsupportUtil import techSupportWorkFlow
from TechSupportDownload import techSupportDownload
from TechSupportDownload import techSupportDownloadCleanup



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

    if applTS:
        params.logger.info("TechSupport Collection Completed for Appliance ")
    else:
        raise TestFail("TechSupport Collection for Appliance  Failed ")

    """
    test for downloading tar files
    """
    if techSupportDownload(applTS):
        params.logger.info("Tar subfiles fully downloaded")
    else:
        raise TestFail("Tar subfiles failed to download")


def controllerSetup():
    par = params.platformParam
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
