# pylint: disable=invalid-name,undefined-variable,no-member
"""
@NAME:  Cleanup

@AUTHOR: Deepthi (dmachira@cisco.com)


@DESCRIPTION: Cleanup file
@PROCEDURE:

@SUPPORT_ALIAS: qali2-dev@cisco.com



"""

import urllib3
import parameter as params



urllib3.disable_warnings()
params.logger = globals().get("runtests_logger", None)



def cleanup():
    """
    Function to cleanup
    """

    params.logger.info("In test suite cleanup")


