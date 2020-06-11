import xml.etree.ElementTree as ET
tree = ET.parse('myxml.xml')
root = tree.getroot()
for x in root.findall('number'):
     element = x.find('element').text
     operation=x.find('operation').text
     elem = x.find('elem').text
     op = x.find('op').text
     res = x.find('res').text
     name=x.get('name')
     print(name,element,operation,elem,op,res)