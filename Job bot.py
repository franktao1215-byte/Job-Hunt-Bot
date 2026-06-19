import requests

print("Starting Job Search...")

response = requests.get("https://www.civilservicejobs.service.gov.uk")

print("Status Code:", response.status_code)

if response.status_code == 200:
    print("Website reachable")
else:
    print("Website not reachable")
