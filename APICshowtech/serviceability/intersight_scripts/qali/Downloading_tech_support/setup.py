# pylint: disable=invalid-name,undefined-variable,protected-access
"""
@NAME:  Setup

@AUTHOR: Deepthi (dmachira@cisco.com)

@TEST_PLAN:
US6993_Airgap_Appliance_TechSupport

@TIMS_ID:


@DESCRIPTION: Setup file

@PROCEDURE: Claimed UCS Setup with FI, Chassis, Blade Servers, SARS , Hyperflex

@SUPPORT_ALIAS: qali-dev@cisco.com
"""

import os
import urllib3
import time
import parameter as params
from qali.test.test import TestFail



# disable warnings from SSL/TLS certificates
urllib3.disable_warnings()
params.logger = globals().get("runtests_logger", None)
topogen = globals().get("topogen", None)
cliData = globals().get("cli_data", None)


def setup():
    '''
    Test suit level set up
    '''
    params.logger = globals().get("runtests_logger", None)

    params.topogen = globals().get("topogen", None)

    print("************************")
    print(params.topogen)

    params.cloud = params.topogen.get_platform('Intersight')[0]

    if not params.cloud:
        raise TestFail(" Set Up Failed : details not found in RackDB.... ")

    params.apiClient = params.cloud.api

    print("**********************")
    print(params.apiClient)

    params.apiClient.start_new_tracking()

    params.apiClient.spy()



    cwdir = os.getcwd()
    downloadDirloc = os.path.join(cwdir, 'downloads/')
    params.downloadDir = downloadDirloc



    downloadURL = params.cloud.cloud_url

    params.downloadURL = downloadURL + 'api/v1'


    # Creating folder in local path for TechSupport Bundle download:
    path1 = params.downloadDir
    if os.path.exists(path1):
        params.logger.info("\n\n {} directory exists".format(path1))
    else:
        try:
            os.mkdir(path1)
            params.logger.info("{} Directory Creation Successful".format(path1))
        except OSError as errDetail:
            params.logger.info("{} Directory creation failed due to {} ".format(path1, errDetail))

    # User Handles

    params.adminUsers = params.cloud.get_user_handles(role='admin')[0]

    params.adminHandle = params.adminUsers.api

    params.adminHandle.spy()




    params.logger.info("Finished test suit level set up {}.\n\n".format(__file__.split('/')[-1]))

