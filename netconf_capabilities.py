from ncclient import manager
from paramiko import hostkeys

router_info = {
    "host": "ios-xe-mgmt-latest.cisco.com",
    "port": "830",
    "username": "developer",
    "password": "C1sco12345"
}

#with manager.connect(host=router_info["host"], port=router_info["port"], username=router_info["username"], password=router_info["password"], hostkey_verify=False) as m:
with manager.connect(**router_info, hostkey_verify=False) as m:
    for capability in m.server_capabilities:
        print('*' * 50)
        print(' ')
        print(capability)