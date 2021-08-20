import requests
from requests.auth import HTTPBasicAuth
import json
import urllib3
urllib3.disable_warnings()

BASE_URL = 'https://sandboxdnac2.cisco.com'
AUTH_URL = '/dna/system/api/v1/auth/token'
USERNAME = 'devnetuser'
PASSWORD = 'Cisco123!'

response = requests.post(BASE_URL + AUTH_URL, auth=HTTPBasicAuth(USERNAME, PASSWORD), verify=False)
token = response.json()['Token']
headers = {'X-Auth-Token': token, 'Content-Type': 'application/json'}


CLIENT_HEALTH = '/dna/intent/api/v1/client-health'
response = requests.get(BASE_URL + CLIENT_HEALTH,headers=headers, verify=False)
clients_health = response.json()['response']
for score in clients_health[0]['scoreDetail']:
    print('Type: {0}, Count: {1}, Score: {2}'.format(
        score['scoreCategory']['value'],
        score['clientCount'], score['scoreValue']))
    try:
        for category in score['scoreList']:
            print('\tType: {0}, Count: {1}'.format(
                category['scoreCategory']['value'],
                category['clientCount']))
    except:
        pass