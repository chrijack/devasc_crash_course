#!/usr/bin/env python3
import requests
import pprint

base_url = '<change to your reserved lab from DevNet>'
username = '<change to your rserverd lab from DevNet>'
password = '<change to your reserved lab from DevNet>'

get_device_url = base_url + '/restconf/data/tailf-ncs:devices/device'

headers = {
    'Content-Type': 'application/yang-data+json'
    }

response = requests.get(get_device_url, 
                      auth=(username, password), 
                      headers=headers, 
                      verify=False)

pprint.pprint(response.text)


