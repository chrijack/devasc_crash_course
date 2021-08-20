#! /usr/bin/env python
from dnacentersdk import api

# Create a DNACenterAPI connection object;
# it uses DNA Center sandbox URL, username and password
DNAC = api.DNACenterAPI(username="devnetuser",
                        password="Cisco123!",
                        base_url="https://sandboxdnac2.cisco.com")

# Find all devices
DEVICES = DNAC.devices.get_device_list()

# Print select information about the retrieved devices
print('{0:25s}{1:1}{2:45s}{3:1}{4:15s}'.format("Device Name", "|", \
    "Device Type", "|", "Up Time"))
print('-'*95)
for DEVICE in DEVICES.response:
    print('{0:25s}{1:1}{2:45s}{3:1}{4:15s}'.format(DEVICE.hostname, \
        "|", DEVICE.type, "|", DEVICE.upTime))
print('-'*95)

