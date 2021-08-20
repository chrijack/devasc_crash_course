#!/usr/bin/env python
""" Add a loopback interface to a device with NETCONF """

from ncclient import manager

IOS_HOST = "ios-xe-mgmt.cisco.com"
NETCONF_PORT = "10000"
USERNAME = "developer"
PASSWORD = "C1sco12345"
LOOPBACK_ID = "53"
LOOPBACK_IP = "1.1.1.1"
MASK = "255.255.255.255"
TYPE = "ianaift:softwareLoopback"
DESC = "New Loopback Added By Python"

# create add_loopback() method
def add_loopback():
    """
    Method that adds loopback interface and configures IP address
    """

    add_loop_interface = """
    <config>
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
                <name>Loopback{id}</name>
                <description>{desc}</description>
                <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">
                    {type}
                </type>
                <enabled>{status}</enabled>
                <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                    <address>
                        <ip>{ip}</ip>
                        <netmask>{mask}</netmask>
                    </address>
                </ipv4>
            </interface>
        </interfaces>
    </config>""".format(id=LOOPBACK_ID, ip=LOOPBACK_IP, mask=MASK, type=TYPE, status="true", desc = DESC )
    with manager.connect(
            host=IOS_HOST,
            port=NETCONF_PORT,
            username=USERNAME,
            password=PASSWORD,
            hostkey_verify=False
        ) as device:

        # Add loopback interface
        print("\n Adding Loopback {} with IP address {} to device {}...\n".\
            format(LOOPBACK_ID, LOOPBACK_IP, IOS_HOST))
        netconf_response = device.edit_config(target='running', config=add_loop_interface)
        # Print the XML response
        print(netconf_response)

if __name__ == '__main__':
    add_loopback()
