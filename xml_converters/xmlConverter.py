import xmltodict
import json

# Step 1: Read XML Data from File
with open('./psd/Pset_DoorCommon.xml', 'r', encoding='utf-8') as xml_file:
    xml_data = xml_file.read()

# Step 2: Parse XML Data
xml_dict = xmltodict.parse(xml_data)

# Step 3: Convert to JSON
json_data = json.dumps(xml_dict, indent=2)

# Step 4: Write JSON Data to File
with open('psd_json/output.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_data)

print("XML to JSON conversion completed and saved to 'output.json'.")


