import urllib.request, urllib.parse, urllib.error

import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while 1:
    address = input('enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'address':address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)

    data = uh.read().decode()
    print('Retrieved', len(data), ' characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('=== Failure To Retrieve ===')
        print(data)
        continue

    lat = js['result'][0]['geometry']['location']['lat']
    lng = js['result'][0]['geometry']['location']['lng']
    print('lat',lat, 'lng',lng)
    location = js['result'][0]['formatted_address']
    print(location)
