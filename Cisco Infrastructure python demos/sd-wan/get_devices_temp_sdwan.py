#! /usr/bin/env python
import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Specify Cisco vManage IP, username and password
VMANAGE_IP = 'sandboxsdwan.cisco.com'
USERNAME = 'devnetuser'
PASSWORD = 'Cisco123!'

BASE_URL_STR = 'https://{}:8443/'.format(VMANAGE_IP)

# Login API resource and login credentials
LOGIN_ACTION = 'j_security_check'
LOGIN_DATA = {'j_username' : USERNAME, 'j_password' : PASSWORD}

# URL for posting login data
LOGIN_URL = BASE_URL_STR + LOGIN_ACTION

# Establish a new session and connect to Cisco vManage
SESS = requests.session()
LOGIN_RESPONSE = SESS.post(url=LOGIN_URL, data=LOGIN_DATA, verify=False)

# Get list of devices that are part of the fabric and display them
DEVICE_RESOURCE = 'dataservice/device'
# URL for device API resource
DEVICE_URL = BASE_URL_STR + DEVICE_RESOURCE

DEVICE_RESPONSE = SESS.get(DEVICE_URL, verify=False)
DEVICE_ITEMS = json.loads(DEVICE_RESPONSE.content)['data']

print('{0:20s}{1:1}{2:12s}{3:1}{4:36s}{5:1}{6:16s}{7:1}{8:7s}'\
    .format("Host-Name", "|", "Device Model", "|", "Device ID", \
        "|", "System IP", "|", "Site ID"))
print('-'*105)

for ITEM in DEVICE_ITEMS:
    print('{0:20s}{1:1}{2:12s}{3:1}{4:36s}{5:1}{6:16s}{7:1}{8:7s}'\
        .format(ITEM['host-name'], "|", ITEM['device-model'], "|", \
            ITEM['uuid'], "|", ITEM['system-ip'], "|", ITEM['site-id']))
print('-'*105)
# Get list of device templates and display them
TEMPLATE_RESOURCE = 'dataservice/template/device'
# URL for device template API resource
TEMPLATE_URL = BASE_URL_STR + TEMPLATE_RESOURCE

TEMPLATE_RESPONSE = SESS.get(TEMPLATE_URL, verify=False)
TEMPLATE_ITEMS = json.loads(TEMPLATE_RESPONSE.content)['data']

print('{0:20s}{1:1}{2:12s}{3:1}{4:36s}{5:1}{6:16s}{7:1}{8:7s}'\
    .format("Template Name", "|", "Device Model", "|", "Template ID", \
        "|", "Attached devices", "|", "Template Version"))
print('-'*105)

for ITEM in TEMPLATE_ITEMS:
    print('{0:20s}{1:1}{2:12s}{3:1}{4:36s}{5:1}{6:<16d}{7:1}{8:<7d}'\
        .format(ITEM['templateName'], "|", ITEM['deviceType'], "|", \
            ITEM['templateId'], "|", ITEM['devicesAttached'], "|", \
                ITEM['templateAttached']))
print('-'*105)
