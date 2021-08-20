""" Add new Member to a Webex Room """

import json
import requests
import pprint

URL = "https://webexapis.com/v1/memberships"
PAYLOAD = {
    "roomId" : "Y2lzY29zcGFyazovL3VzL1JPT00vYzk2NWU2YzAtNWVmMS0xMWViLThlNGUtMTU4ZmY4NjIzYTQ3",
  "personEmail": "newUser@devasc.com",
  "personDisplayName": "Cisco DevNet",
  "isModerator": "false"
}
HEADERS = {
    "Authorization": "Bearer OTkwODFmZjEtZDkzMS00ZGE5LWE4YWYtOWVjYTZjYWNjNmRiZmMzMmJiMDMtMzJh_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f",
    "Content-Type": "application/json"
}
RESPONSE = requests.request("POST", URL, data=json.dumps(PAYLOAD), headers=HEADERS)
pprint.pprint(json.loads(RESPONSE.text))
