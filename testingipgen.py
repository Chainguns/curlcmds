import random
from random import randrange
import ipaddress
import random
def random_ipv6_addr(network):
    """
    Generate a random IPv6 address in the given network
    Example: random_ipv6_addr("fd66:6cbb:8c10::/48")
    Returns an IPv6Address object.
    "6:1:67::1/64"
    """
    net = ipaddress.IPv6Network(network)
    # Which of the network.num_addresses we want to select?
    addr_no = random.randint(0, net.num_addresses)
    # Create the random address by converting to a 128-bit integer, adding addr_no and converting back
    network_int = int.from_bytes(net.network_address.packed, byteorder="big")
    addr_int = network_int + addr_no
    addr = ipaddress.IPv6Address(addr_int.to_bytes(16, byteorder="big"))
    return str(addr) + "/64"

ips = ([str(ip) + "/16" for ip in ipaddress.IPv4Network('6.0.0.0/16')] )
mac = ("%02x:%02x:%02x:%02x:%02x:%02x" % (random.randint(0, 255),
                             random.randint(0, 255),
                             random.randint(0, 255),
                             random.randint(0, 255),
                             random.randint(0, 255),
                             random.randint(0, 255)))
ipv6s = []
for i in range(10):
    ipv6s.append(random_ipv6_addr("6:1:67::/64"))
# print(ips)
# print(ipv6s)
HEADERS = ["'Authorization: Basic Y3VtdWx1czpCbHN0MjAyMQ=='", "'content-type: application/json'"]
bonds = ['bond1', 'bond2']
swps = ['swp1','swp2','swp3','swp4','swp5','swp6','swp7']
VLANS = range(10,90, 10)
areas = [random.randint(0,10)]
# print(VLANS[0])
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
'https://10.170.6.4:8765/nvue_v1/interface/%s/bridge/domain?rev='% swps[4],
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
D = ["'{\"address\": {\"6.6.6.6/32\": {}}}'", "'{\"address\": {\"%s\": {}}}'"% ips[randrange(0,len(ips))],"'{\"address\": {\"%s\": {}}}'"% ipv6s[randrange(0,len(ipv6s))],"'{\"address\": {\"%s\": {}}}'"% ips[randrange(0,len(ips))],"'{\"address\": {\"%s\": {}}}'"% ipv6s[randrange(0,len(ipv6s))],"'{\"address\": {\"%s\": {}}}'"% ips[randrange(0,len(ips))], "'{\"address\": {\"%s\": {}}}'"% ipv6s[randrange(0,len(ipv6s))], "'{\"address\": {\"%s\": {}}}'"% ips[randrange(0,len(ips))], "'{\"address\": {\"%s\": {}}}'"% ipv6s[randrange(0,len(ipv6s))], "'{\"%s\": {}}'"% bonds[0], "'{\"member\": {\"%s\": {}}}'"% swps[randrange(1,len(swps))],"'{\"mlag\": {\"id\": %s}}'"% random.randrange(1,10),"'{\"br_default\": {\"access\": %s}}'"% VLANS[0],"'{\"untagged\": 1}'","'{\"vlan\" : {\"%s\": {}}}'"% VLANS[0],
     "'{\"address\": {\"%s\": {}}}'"% ips[randrange(0,len(ips))], "'{\"member\": { \"%s\": {}, \"%s\": {}}}'"% (swps[2], swps[3]), "'{\"mac-address\": \"%s\"}'"% mac,"'{\"backup\": {\"5.5.5.5\" : {\"vrf\": \"default\"}}}'","'{\"br_default\": {\"access\": %s}}'"% VLANS[1],"'{\"vlan\" : {\"%s\": {}}}'"% VLANS[1],"'{\"address\": {\"%s\": {}}}'"% ips[randrange(0,len(ips))],"'{\"router-id\": \"6.6.6.6\"}'",
     "'{\"area\": {\"0\": {}}}'", "'{\"network\": {\"6.6.6.6/32\": {}}}'","'{\"network\": {\"%s\": {}}}'"% ips[randrange(0,len(ips))],"'{\"network\": {\"%s\": {}}}'"% ips[randrange(0,len(ips))],"'{\"vni\": {\"%s\": {}}}'"% VLANS[0],"'{\"vni\": {\"%s\": {}}}'"% VLANS[1],"'{\"vni\": {\"%s\": {}}}'"% VLANS[2],"'{\"source\": {\"address\": \"5.5.5.5\"}}'",
     "'{\"autonomous-system\": 200}'","'{\"router-id\": \"6.6.6.6\"}'","'{\"remote-as\": 300}'","'{\"remote-as\": 400}'"
     , "'{\"ipv4-unicast\": {}}'", "'{\"enable\": \"on\"}'", "'{\"l2vpn-evpn\": {\"enable\": \"on\"}}'", "'{\"l2vpn-evpn\": {\"enable\": \"on\"}}'","'{\"l2vpn-evpn\": {\"enable\": \"on\"}}'"]



