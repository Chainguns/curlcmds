import random
from random import randrange
import ipaddress
import random

ips = ([str(ip) + "/16" for ip in ipaddress.IPv4Network('6.1.67.0/24')] )
mac = ("%02x:%02x:%02x:%02x:%02x:%02x" % (random.randint(0, 255),
                             random.randint(0, 255),
                             random.randint(0, 255),
                             random.randint(0, 255),
                             random.randint(0, 255),
                             random.randint(0, 255)))
HEADERS = ["'Authorization: Basic Y3VtdWx1czpCbHN0MjAyMQ=='", "'content-type: application/json'"]
bonds = ['bond1', 'bond2']
swps = ['swp1','swp2','swp3','swp4','swp5','swp6','swp7']
VLANS = range(10,90, 10)
areas = [random.randint(0,10)]
print(VLANS)
URLS = ['https://10.170.6.4:8765/nvue_v1/interface/lo/ip?rev=',
'https://10.170.6.4:8765/nvue_v1/interface/%s/ip?rev='% swps[0],
'https://10.170.6.4:8765/nvue_v1/interface/%s/ip?rev='% swps[0],
'https://10.170.6.4:8765/nvue_v1/interface/%s/ip?rev='% swps[1],
'https://10.170.6.4:8765/nvue_v1/interface/%s/ip?rev='% swps[1],
'https://10.170.6.4:8765/nvue_v1/interface/%s/ip?rev='% swps[2],
'https://10.170.6.4:8765/nvue_v1/interface/%s/ip?rev='% swps[2],
'https://10.170.6.4:8765/nvue_v1/interface/%s/ip?rev='% swps[3],
'https://10.170.6.4:8765/nvue_v1/interface/%s/ip?rev='% swps[3],
'https://10.170.6.4:8765/nvue_v1/interface?rev=',
'https://10.170.6.4:8765/nvue_v1/interface/%s/bond?rev='% bonds[0],
'https://10.170.6.4:8765/nvue_v1/interface/%s/bond?rev='% bonds[0],
'https://10.170.6.4:8765/nvue_v1/interface/%s/bridge/domain?rev='% bonds[0],
'https://10.170.6.4:8765/nvue_v1/bridge/domain/br_default?rev=',
'https://10.170.6.4:8765/nvue_v1/bridge/domain/br_default?rev=',
'https://10.170.6.4:8765/nvue_v1/interface/%s/ip?rev='% bonds[0],
'https://10.170.6.4:8765/nvue_v1/interface/peerlink/bond?rev=',
'https://10.170.6.4:8765/nvue_v1/mlag?rev=changeset%2Fcumulus%2F2022-01-20_16.49.34_VHHH',
'https://10.170.6.4:8765/nvue_v1/mlag?rev=changeset%2Fcumulus%2F2022-01-20_16.49.34_VHHH',
'https://10.170.6.4:8765/nvue_v1/interface/%sbridge/domain?rev='% swps[4],
'https://10.170.6.4:8765/nvue_v1/bridge/domain/br_default?rev=',
'https://10.170.6.4:8765/nvue_v1/interface/vlan%s/ip?rev='% VLANS[0],
'https://10.170.6.4:8765/nvue_v1/vrf/default/router/ospf?rev=',
'https://10.170.6.4:8765/nvue_v1/vrf/default/router/ospf?rev=',
'https://10.170.6.4:8765/nvue_v1/vrf/default/router/ospf/area/%s?rev='% areas[0],
'https://10.170.6.4:8765/nvue_v1/vrf/default/router/ospf/area/%s?rev='% areas[0],
'https://10.170.6.4:8765/nvue_v1/vrf/default/router/ospf/area/%s?rev='% areas[0],
'https://10.170.6.4:8765/nvue_v1/bridge/domain/br_default/vlan/%s?rev='% VLANS[0],
'https://10.170.6.4:8765/nvue_v1/bridge/domain/br_default/vlan/%s?rev='% VLANS[1],
'https://10.170.6.4:8765/nvue_v1/bridge/domain/br_default/vlan/%s?rev='% VLANS[2],
'https://10.170.6.4:8765/nvue_v1/nve/vxlan?rev=',
'https://10.170.6.4:8765/nvue_v1/router/bgp?rev=',
'https://10.170.6.4:8765/nvue_v1/router/bgp?rev=',
'https://10.170.6.4:8765/nvue_v1/vrf/default/router/bgp/neighbor/6.1.67.2?rev=',
'https://10.170.6.4:8765/nvue_v1/vrf/default/router/bgp/neighbor/6.1.68.2?rev=',
'https://10.170.6.4:8765/nvue_v1/vrf/default/router/bgp/address-family?rev=',
'https://10.170.6.4:8765/nvue_v1/evpn?rev=',
'https://10.170.6.4:8765/nvue_v1/vrf/default/router/bgp/address-family?rev=',
'https://10.170.6.4:8765/nvue_v1/vrf/default/router/bgp/neighbor/6.1.68.2/address-family?rev=',
'https://10.170.6.4:8765/nvue_v1/vrf/default/router/bgp/neighbor/6.1.67.2/address-family?rev=',]
D = ["'{\"address\": {\"6.6.6.6/32\": {}}}'", "'{\"address\": {\"6.1.67.1/16\": {}}}'","'{\"address\": {\"6:1:67::1/64\": {}}}'","'{\"address\": {\"6.1.68.1/16\": {}}}'","'{\"address\": {\"6:1:68::1/64\": {}}}'","'{\"address\": {\"5.1.56.2/16\": {}}}'", "'{\"address\": {\"5:1:56::2/64\": {}}}'", "'{\"address\": {\"5.2.56.2/16\": {}}}'", "'{\"address\": {\"5:2:56::2/64\": {}}}'", "'{\"%s\": {}}'"% bonds[0], "'{\"member\": {\"%s\": {}}}'"% swps[randrange(1,len(swps))],"'{\"mlag\": {\"id\": %s}}'"% random.randrange(1,10),"'{\"br_default\": {\"access\": %s}}'"% VLANS[0],"'{\"untagged\": 1}'","'{\"vlan\" : {\"%s\": {}}}'"% VLANS[0],
     "'{\"address\": {\"3.1.35.3/16\": {}}}'", "'{\"member\": { \"%s\": {}, \"%s\": {}}}'"% (swps[randrange(1,len(swps))], swps[randrange(1,len(swps))]), "'{\"mac-address\": \"44:38:39:BE:EF:AA\"}'","'{\"backup\": {\"5.5.5.5\" : {\"vrf\": \"default\"}}}'","'{\"br_default\": {\"access\": %s}}'"% VLANS[1],"'{\"vlan\" : {\"%s\": {}}}'"% VLANS[1],"'{\"address\": {\"4.1.46.2/16\": {}}}'","'{\"router-id\": \"6.6.6.6\"}'",
     "'{\"area\": {\"0\": {}}}'", "'{\"network\": {\"6.6.6.6/32\": {}}}'","'{\"network\": {\"6.1.67.1/16\": {}}}'","'{\"network\": {\"6.1.68.1/16\": {}}}'","'{\"vni\": {\"%s\": {}}}'"% VLANS[0],"'{\"vni\": {\"%s\": {}}}'"% VLANS[1],"'{\"vni\": {\"%s\": {}}}'"% VLANS[2],"'{\"source\": {\"address\": \"5.5.5.5\"}}'",
     "'{\"autonomous-system\": 200}'","'{\"router-id\": \"6.6.6.6\"}'","'{\"remote-as\": 300}'","'{\"remote-as\": 400}'"
     , "'{\"ipv4-unicast\": {}}'", "'{\"enable\": \"on\"}'", "'{\"l2vpn-evpn\": {\"enable\": \"on\"}}'", "'{\"l2vpn-evpn\": {\"enable\": \"on\"}}'","'{\"l2vpn-evpn\": {\"enable\": \"on\"}}'"]
