import json

with open('/Users/kaylabowler/Desktop/HackTech2020/example.json') as f:
    data = json.load(f)
    entity = data['entity']
    entityTag = data['entityTag']
    body = data['body']
