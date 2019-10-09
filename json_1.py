import json

data = '''{
    
"name": "Richard",

"phone": {
    "type":"intl",
    "number": "+1 510 341 9182"
    },

"email": {
    "hide": "yes"
    }
}'''

info = json.loads(data)
print('Name:', info['name'])
print('Hide:',info['email']['hide'])
