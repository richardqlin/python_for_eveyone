import json

data = '''[
{ "id": "001",
    "x": "2",
    "name": "Richard"
},
{ "id": "009",
    "x": "7",
    "name": "Bob"
}

]'''

info = json.loads(data)
print('User count',len(data))

for item in info:
    print('Name:', item['name'])
    print('Hide:',item['id'])
    print('Attribute',item['x'])
