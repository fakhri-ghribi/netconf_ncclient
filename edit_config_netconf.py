from ncclient import manager
from paramiko import hostkeys

router_info = {
    "host": "ios-xe-mgmt-latest.cisco.com",
    "port": "830",
    "username": "developer",
    "password": "C1sco12345"
}

config_template = open('C:\Users\Fakhri\Desktop\projects\Netconf_Python/ios_config.xml').read()

netconf_config = config_template.format(interface_name="GigabitEthernet2", interface_desc="edit interface with ncclient")

with manager.connect(**router_info, hostkey_verify=False) as m:
    response = m.edit_config(netconf_config, target="candidate")


print(response)