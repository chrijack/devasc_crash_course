import requests
import pprint

url = "https://10.10.20.49:443/restconf/data/tailf-ncs:devices/device"

payload={}
headers = {
  'Accept': 'application/yang-data+json',
  'Authorization': 'Basic ZGV2ZWxvcGVyOkMxc2NvMTIzNDU='
}

response = requests.request("GET", url, headers=headers, data=payload,verify=False)

pprint.pprint(response.text)
