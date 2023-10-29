import requests


api_key = "f98aceee3f421c570b9ca989a86331ca"
ip_address = "134.201.250.155"


url = f'http://api.ipstack.com/{ip_address}?access_key={api_key}'
response = requests.get(url)


if response.status_code == 200:
    data = response.json()
    print("IP Address:", data['ip'])
    print("Country:", data['country_name'])
    print("Region:", data['region_name'])
    print("City:", data['city'])
    print("Latitude:", data['latitude'])
    print("Longitude:", data['longitude'])
else:
    print("Unsuccessful attempt", response.status_code)