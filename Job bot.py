import requests
from bs4 import BeautifulSoup

KEYWORDS = [
    "Project Officer",
    "Project Coordinator",
    "PMO",
    "Partnerships Officer",
    "Stakeholder Engagement"
]

for keyword in KEYWORDS:
    print(f"\n===== {keyword} =====")
