from ncclient import manager, operations
from ncclient.operations.rpc import RPCReply
from paramiko import hostkeys
import xmltodict

router_info = {
    "host": "ios-xe-mgmt-latest.cisco.com",
    "port": "830",
    "username": "developer",
    "password": "C1sco12345"
}


interface_filter = """
<filter>
 <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
   <interface>
    <name>GigabitEthernet2</name>
   </interface>
 </interfaces>
 <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
   <interface>
    <name>GigabitEthernet2</name>
   </interface>
 </interfaces-state>
</filter>
"""

#with manager.connect(host=router_info["host"], port=router_info["port"], username=router_info["username"], password=router_info["password"], hostkey_verify=False) as m:
with manager.connect(**router_info, hostkey_verify=False) as m:
    netconf_response = m.get(interface_filter)


python_response= xmltodict.parse(netconf_response.xml)["rpc-reply"]["data"]
operation_state = python_response["interfaces-state"]["interface"]
configuration_data = python_response["interfaces"]["interface"]


print(f"Name: {configuration_data['name']['#text']}")
print(f"Description: {configuration_data['description']}")
print(f"Name: {operation_state['stattistics']['in-unicast-pkts']}")

