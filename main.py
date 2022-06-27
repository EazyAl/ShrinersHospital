import meraki
import pprint
import csv
import pandas as pd
from datetime import datetime, timedelta
from dateutil import parser

API_KEY = ''

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '862513' # Shriner's org ID

column_names = ["ITEM", "DEPARTMENT", "DEVICE", "SERIALNUMBER" ,"MACADDRESS"]
df = pd.read_csv("ShrinersMAC.csv", names = column_names)

addresses = df.MACADDRESS.to_list()
addresses.pop(0)
print(addresses) # List of MACs populated

networks = dashboard.organizations.getOrganizationNetworks(
    organization_id, total_pages='all'
)

delta = timedelta(days = 120)

# for n in networks:
#
    # try:
#
        # clients = dashboard.networks.getNetworkClients(
        # n['id'], total_pages='all'
        # )
#
    # except meraki.APIError as e:
#
        # network_name = n['name']

montreal_id = 'L_741968038609293913' #MON Network ID

for c in clients:

    if not (c['mac'] in addresses):

        if (c['ssid'] == 'PFA'):

            first = c['firstSeen']
            last = c['lastSeen']

            t1 = parser.parse(first)
            t2 = parser.parse(last)

            diff = t2 - t1

            if (diff >= delta):

                # try:

                response = dashboard.networks.updateNetworkClientPolicy(
                montreal_id, c['id'], 'Group policy',
                groupPolicyId='100'
                )

                # except meraki.APIError as e:
#
                    # network_name = n['name']
                    # print(network_name + "Does not have PFA Group policies")
