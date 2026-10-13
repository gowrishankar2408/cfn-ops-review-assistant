import requests
import urllib3

urllib3.disable_warnings()

SECRET = "9DQQdESwkwvQybYH8ZyhtZly8UJQKgsntQwTkeLmJgLFdB6ShYkbJQQJ99CJACL93NaAArohAAABAZBS4RUv.BVlFeKphrS3NisgNRZzPk0NV5Aa6Ly3v3jplQey1pFvKAQ8Jcrx6JQQJ99CJACL93NaAArohAAABAZBS1Kpo"

headers = {
    "Authorization": f"Bearer {SECRET}"
}

response = requests.post(
    "https://directline.botframework.com/v3/directline/conversations",
    headers=headers,
    verify=False
)

conversation_id = response.json()["conversationId"]

print("Conversation:", conversation_id)