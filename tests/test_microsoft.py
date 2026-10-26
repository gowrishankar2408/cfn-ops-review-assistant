import requests

r = requests.get(
    "https://www.microsoft.com"
)

print(r.status_code)