import requests
import json

# IP address to test
ip_address = '147.229.2.90'


request_url = 'https://geolocation-db.com/jsonp/' + ip_address
response = requests.get(request_url)
result = response.content.decode()
result = result.split("(")[1].strip(")")
result = json.loads(result)
print(result)
