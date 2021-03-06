import meraki
import pprint

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481107379'

#response = dashboard.networks.getNetworkClients(
#    network_id, total_pages='all'
#)

#pprint.pprint(response)

clients = dashboard.networks.getNetworkClients(network_id, total_pages='all')
for client in clients:
    print("Description: {!s:50}, IP: {!s:14}, LastSeen: {!s}".format(client['description'],client['ip'], client['lastSeen']))