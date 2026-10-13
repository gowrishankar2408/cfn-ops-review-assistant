import requests
import time
import json



time.sleep(5)

SECRET = "9DQQdESwkwvQybYH8ZyhtZly8UJQKgsntQwTkeLmJgLFdB6ShYkbJQQJ99CJACL93NaAArohAAABAZBS4RUv.BVlFeKphrS3NisgNRZzPk0NV5Aa6Ly3v3jplQey1pFvKAQ8Jcrx6JQQJ99CJACL93NaAArohAAABAZBS1Kpo"

url = (
    f"https://directline.botframework.com/v3/directline/"
    f"conversations/{'4YCkn56L8bX4WSjjk2rkzm-us'}/activities"
)

response = requests.get(
    url,
    headers={
        "Authorization": f"Bearer {SECRET}"
    },
    verify=False
)

data = response.json()

print(data)
'''
for activity in data["activities"]:
    print(json.dumps(activity, indent=2))

'''