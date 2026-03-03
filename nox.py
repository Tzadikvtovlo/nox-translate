import json
import xml.etree.ElementTree as ET
import os

def create_ts(json_file, output_ts):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    ts = ET.Element("TS", version="2.1", language="he_IL")
    contexts = {}
    for msg in data['messages']:
        ctx_name = msg.get('context', 'Global')
        if ctx_name not in contexts:
            contexts[ctx_name] = ET.SubElement(ts, "context")
            ET.SubElement(contexts[ctx_name], "name").text = ctx_name
        
        context_element = contexts[ctx_name]
        message = ET.SubElement(context_element, "message")
        ET.SubElement(message, "source").text = msg.get('source', '')
        ET.SubElement(message, "translation").text = msg.get('translation', '')

    tree = ET.ElementTree(ts)
    with open(output_ts, 'wb') as f:
        tree.write(f, encoding='utf-8', xml_declaration=True)

# סורק את התיקייה וממיר את כל קבצי ה-JSON
for file in os.listdir('.'):
    if file.endswith('.json'):
        print(f"Converting {file}...")
        create_ts(file, file.replace('.json', '.ts'))
