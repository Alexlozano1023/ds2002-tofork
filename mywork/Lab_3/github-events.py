#!/usr/bin/env python3
import os
import json
import requests

GHUSER = os.getenv("GITHUB_USER")

url = f"https://api.github.com/users/{GHUSER}/events"

response = requests.get(url)

if response.status_code == 200:
    events = response.json()
    
    print(f"Recent GitHub activity for {GHUSER}:")
    
 
    for event in events[:5]:
        event_type = event["type"]
        repo_name = event["repo"]["name"]
        print(f"- {event_type} :: {repo_name}")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
