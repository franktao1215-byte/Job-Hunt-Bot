import requests

url = "https://www.civilservicejobs.service.gov.uk"

response = requests.get(url)

print(response.status_code)
