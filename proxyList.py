import requests
import json

# Print Banner
print("----------------------------")
print("     Pr0xyList v1.0")
print("     Dev: LSDeep")
print("     level23hacktools.com")
print("----------------------------\n")

# Your URL
url = 'https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc'

# Send GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Load JSON data from response
    data = json.loads(response.text)

    proxies = []

    # Loop through each proxy in the data
    for proxy in data['data']:
        ip_port = f"{proxy['ip']}:{proxy['port']}"
        print(ip_port)
        proxies.append(ip_port)

    # Ask user whether to export data
    export = input("Do you want to export data to a .txt file? (yes/no): ")
    if export.lower() == 'yes':
        # Write proxies to a .txt file
        with open('proxies.txt', 'w') as f:
            for proxy in proxies:
                f.write(proxy + '\n')
        print("Data has been exported to proxies.txt")
else:
    print("Failed to fetch data")
