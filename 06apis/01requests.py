import requests
import json
#Beautiful Soup # Para web scraping
url = "https://api.spacexdata.com/v3/rockets"

response = requests.get(url)

#print(response)
#print(response.text)
response = response.json()
print(type(response))
print(len(response))

print(json.dumps(response, indent=4))