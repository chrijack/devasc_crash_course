""" Create Webex Team """

import json
import requests

URL = "https://webexapis.com/v1/teams"
PAYLOAD = {
    "name": "DevNet Associate Certification Team"
}
HEADERS = {
    "Authorization": "Bearer OTkwODFmZjEtZDkzMS00ZGE5LWE4YWYtOWVjYTZjYWNjNmRiZmMzMmJiMDMtMzJh_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f",
    "Content-Type": "application/json"
}
RESPONSE = requests.request("POST", URL, data=json.dumps(PAYLOAD), headers=HEADERS)
print(RESPONSE.text)
