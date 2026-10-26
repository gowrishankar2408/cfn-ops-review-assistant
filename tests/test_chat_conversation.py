import json
import requests
from sample_input import prompt

SECRET = "9DQQdESwkwvQybYH8ZyhtZly8UJQKgsntQwTkeLmJgLFdB6ShYkbJQQJ99CJACL93NaAArohAAABAZBS4RUv.BVlFeKphrS3NisgNRZzPk0NV5Aa6Ly3v3jplQey1pFvKAQ8Jcrx6JQQJ99CJACL93NaAArohAAABAZBS1Kpo"

conversation_id = "4YCkn56L8bX4WSjjk2rkzm-us"

url = (
    f"https://directline.botframework.com/v3/directline/"
    f"conversations/{conversation_id}/activities"
)

payload = {
    "type": "message",
    "from": {
        "id": "python-client"
    },
    "text": json.dumps(prompt, indent=2)
}

response = requests.post(
    url,
    headers={
        "Authorization": f"Bearer {SECRET}",
        "Content-Type": "application/json"
    },
    json=payload,
    verify=False
)

print(response.status_code)
print(response.text)