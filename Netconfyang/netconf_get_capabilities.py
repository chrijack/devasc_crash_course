#!/usr/bin/env python
""" Get the capabilities of a remote device with NETCONF """

from ncclient import manager

IOS_HOST = "ios-xe-mgmt.cisco.com"
NETCONF_PORT = "10000"
USERNAME = "developer"
PASSWORD = "C1sco12345"

# create a get_capabilities() method
def get_capabilities():
    """
    Method that prints NETCONF capabilities of remote device.
    """
    with manager.connect(
            host=IOS_HOST,
            port=NETCONF_PORT,
            username=USERNAME,
            password=PASSWORD,
            hostkey_verify=False
        ) as device:

        # print all NETCONF capabilities
        print('\n***NETCONF Capabilities for device {}***\n'.format(IOS_HOST))
        for capability in device.server_capabilities:
            print(capability)

if __name__ == '__main__':
    get_capabilities()
