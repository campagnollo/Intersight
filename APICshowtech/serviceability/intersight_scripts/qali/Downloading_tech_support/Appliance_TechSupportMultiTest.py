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

    applTS = controlerSetup()
    params.logger.info("TechSupport Collection Completed for Appliance ")


    """
    test for downloading tar files
    """
    techSupportDownload(applTS)
    params.logger.info("Tar subfiles fully downloaded")



    """
    test for measuring len of tech support files in a multi serial request
    """


    if len(applTS.techsupport_files) == params.platformParamMulti["ExpectedReturn"]:
        params.logger.info("Multi request for serial returns two or more tech support files as planned")
    else:
        raise Exception("Number of bundle return not the same as expected returns.")




def controlerSetup():
    par = params.platformParamMulti['platformparams']
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
