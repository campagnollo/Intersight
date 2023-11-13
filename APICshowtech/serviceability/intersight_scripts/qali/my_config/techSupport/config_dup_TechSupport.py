from qali.test.TestSuite import Test_Suite
import sys
import os

from qali.topology import sysdb
from qali.topology import topo_core

test_owner = 'ericmoo'
notify_list = [
    'ericmoo@cisco.com',
]

os.chdir("../..")
directory = os.getcwd()
sys.path.append(directory)

comment = "just for test"
test_system = None

test_topology = 'rybauer_intersight_db'

physical_topology = sysdb.get_rack_info(test_topology)
topogen = topo_core.Topogen(physical_topology=physical_topology, test_topology=test_topology,
                            inventory="ZERO_INVENTORY", logger=logger)

TechSupport_Suite = Test_Suite('ApplianceTechSupport',
                               directory + '/Downloading_tech_support')
TechSupport_Suite.add_tests(
    ['Appliance_TechSupportDupTest'])

test_suites = [
    TechSupport_Suite,
]
comment = 'Tech Support demonstrator.'
