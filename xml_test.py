import xml.etree.ElementTree as ET

data ='''
<person>
    <name>Richard</name>
    <phone type="intl">
    +1 510 909 9232
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr', tree.find('email').get('hide'))
