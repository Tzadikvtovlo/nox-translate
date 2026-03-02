import json
import xml.etree.ElementTree as ET

with open('multiplayer_ar.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

root = ET.Element("TS", version="2.1", language="he_IL")
for msg in data['messages']:
    context = ET.SubElement(root, "context")
    name = ET.SubElement(context, "name")
    name.text = msg['context']
    message = ET.SubElement(context, "message")
    source = ET.SubElement(message, "source")
    source.text = msg['source']
    translation = ET.SubElement(message, "translation")
    translation.text = msg['translation']

with open('multiplayer.ts', 'wb') as f:
    f.write(ET.tostring(root, encoding='utf-8', xml_declaration=True))
