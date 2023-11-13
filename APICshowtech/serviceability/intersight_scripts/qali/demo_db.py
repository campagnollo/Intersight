from qali.topology.physical_topology import *
from qali.topology.topo_core import IntersightUserMap
from qali.topology.topo_core import APIC

topo = Topology(name='rybauer_intersight_topo', description='rybauer')
rack = Rack(name='rybauer_intersight_db', location='rybauer', owner='rybauer')
topo.add(rack)

intersight_appliance = Intersight(name='rybauer-intersight-dev',
                                  url='https://rybauer-intersight-dev.cisco.com',
                                  api_key_id='6393fb687564612d3097f2ee/6394045b7564612d30983c00/63bc5b027564612d3033b1e4',
                                  private_key_file='rbauer-intersight-admin-key.pem',
                                  account_user='',
                                  account_password='',
                                  user_map={
                                      'admin': [IntersightUserMap(url='https://rybauer-intersight-dev.cisco.com',
                                                                  api_key_id='6393fb687564612d3097f2ee/6394045b7564612d30983c00/63bc5b027564612d3033b1e4',
                                                                  private_key_file='rbauer-intersight-admin-key.pem',
                                                                  account_user='',
                                                                  account_password='')
                                                ],
                                  })
topo.add(intersight_appliance)

# Don't know if this APIC class is useable yet
apic = APIC(user="admin", password="ins3965!", ip_address="10.48.31.178", logical=False)
topo.add(apic)
