""" Create Webex Room """
import json
import requests
import pprint

URL = "https://webexapis.com/v1/rooms"
PAYLOAD = {
    "title": "DevAsc Team Room"
}
HEADERS = {
    "Authorization": "Bearer OTkwODFmZjEtZDkzMS00ZGE5LWE4YWYtOWVjYTZjYWNjNmRiZmMzMmJiMDMtMzJh_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f",
    "Content-Type": "application/json"
}
RESPONSE = requests.request("POST", URL, data=json.dumps(PAYLOAD), headers=HEADERS)
pprint.pprint(json.loads(RESPONSE.text))

