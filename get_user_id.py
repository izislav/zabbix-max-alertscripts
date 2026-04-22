#!/usr/bin/env python3
import os
import requests
import json

token = os.environ.get("MAX_BOT_TOKEN")

if not token:
    print("No token")
    exit(1)

url = "https://platform-api.max.ru/updates"
headers = {
    "Authorization": token
}

r = requests.get(url, headers=headers)

print(json.dumps(r.json(), indent=2))
