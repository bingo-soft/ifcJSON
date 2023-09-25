# import xmltodict
# import json

# # Step 1: Read XML Data from File
# with open('./psd/Pset_DoorCommon.xml', 'r', encoding='utf-8') as xml_file:
#     xml_data = xml_file.read()

# # Step 2: Parse XML Data
# xml_dict = xmltodict.parse(xml_data)

# # # Remove NameAliases and DefinitionAliases
# # if "PropertyDefs" in xml_dict["PropertySetDef"]:
# #     property_defs = xml_dict["PropertySetDef"]["PropertyDefs"]["PropertyDef"]
# #     for prop_def in property_defs:
# #         if "NameAliases" in prop_def:
# #             del prop_def["NameAliases"]
# #         if "DefinitionAliases" in prop_def:
# #             del prop_def["DefinitionAliases"]


# # Function to remove "@" symbol from attribute names
# def remove_at_symbol(dictionary):
#     new_dict = {}
#     for key, value in dictionary.items():
#         new_key = key.lstrip('@')  # Remove the "@" symbol
#         if isinstance(value, dict):
#             new_dict[new_key] = remove_at_symbol(value)
#         elif isinstance(value, list):
#             new_list = []
#             for item in value:
#                 if isinstance(item, dict):
#                     new_list.append(remove_at_symbol(item))
#                 else:
#                     new_list.append(item)
#             new_dict[new_key] = new_list
#         else:
#             new_dict[new_key] = value
#     return new_dict

# # Remove "@" symbol from attribute names
# xml_dict = remove_at_symbol(xml_dict)

# # Remove NameAliases and DefinitionAliases
# if "PropertyDefs" in xml_dict["PropertySetDef"]:
#     property_defs = xml_dict["PropertySetDef"]["PropertyDefs"]["PropertyDef"]
#     for prop_def in property_defs:
#         if "NameAliases" in prop_def:
#             del prop_def["NameAliases"]
#         if "DefinitionAliases" in prop_def:
#             del prop_def["DefinitionAliases"]

# # Step 3: Convert to JSON
# json_data = json.dumps(xml_dict, indent=2)

# # Step 4: Write JSON Data to File
# with open('psd_json/output.json', 'w', encoding='utf-8') as json_file:
#     json_file.write(json_data)

# print("XML to JSON conversion completed and saved to 'output.json'.")


import os
import xmltodict
import json

# Directory where your XML files are located
xml_directory = 'qto_xml_files'

# Directory where you want to save the JSON files
json_directory = 'qto_json_files'

# Ensure the JSON directory exists
os.makedirs(json_directory, exist_ok=True)

# List of XML file names in the XML directory
xml_files = os.listdir(xml_directory)

# Loop through each XML file
for xml_file_name in xml_files:
    if xml_file_name.endswith('.xml'):
        # Create the full path for the XML file
        xml_file_path = os.path.join(xml_directory, xml_file_name)

        # Read XML Data from File
        with open(xml_file_path, 'r', encoding='utf-8') as xml_file:
            xml_data = xml_file.read()

        # Parse XML Data
        xml_dict = xmltodict.parse(xml_data)

        # Function to remove "@" symbol from attribute names
        def remove_at_symbol(dictionary):
            new_dict = {}
            for key, value in dictionary.items():
                new_key = key.lstrip('@')  # Remove the "@" symbol
                if isinstance(value, dict):
                    new_dict[new_key] = remove_at_symbol(value)
                elif isinstance(value, list):
                    new_list = []
                    for item in value:
                        if isinstance(item, dict):
                            new_list.append(remove_at_symbol(item))
                        else:
                            new_list.append(item)
                    new_dict[new_key] = new_list
                else:
                    new_dict[new_key] = value
            return new_dict

        # Remove "@" symbol from attribute names
        xml_dict = remove_at_symbol(xml_dict)

        # Modify the dictionary to remove elements
        if "QtoSetDef" in xml_dict:
            property_set_def = xml_dict["QtoSetDef"]
            if "QtoDefs" in property_set_def:
                property_defs = property_set_def["QtoDefs"]["QtoDef"]
                if isinstance(property_defs, list):
                    for prop_def in property_defs:
                        if "NameAliases" in prop_def:
                            del prop_def["NameAliases"]
                        if "DefinitionAliases" in prop_def:
                            del prop_def["DefinitionAliases"]
                elif isinstance(property_defs, dict):
                    if "NameAliases" in property_defs:
                        del property_defs["NameAliases"]
                    if "DefinitionAliases" in property_defs:
                        del property_defs["DefinitionAliases"]
            if "QtoDefinitionAliases" in property_set_def:
                del property_set_def["QtoDefinitionAliases"]

        # # Modify the dictionary to remove elements
        # if "PropertySetDef" in xml_dict:
        #     property_set_def = xml_dict["PropertySetDef"]
        #     if "PropertyDefs" in property_set_def:
        #         property_defs = property_set_def["PropertyDefs"]["PropertyDef"]
        #         if isinstance(property_defs, list):
        #             for prop_def in property_defs:
        #                 if "NameAliases" in prop_def:
        #                     del prop_def["NameAliases"]
        #                 if "DefinitionAliases" in prop_def:
        #                     del prop_def["DefinitionAliases"]
        #         elif isinstance(property_defs, dict):
        #             if "NameAliases" in property_defs:
        #                 del property_defs["NameAliases"]
        #             if "DefinitionAliases" in property_defs:
        #                 del property_defs["DefinitionAliases"]
        #     if "PsetDefinitionAliases" in property_set_def:
        #         del property_set_def["PsetDefinitionAliases"]

        # Create the JSON file name (replace .xml with .json)
        json_file_name = xml_file_name.replace('.xml', '.json')

        # Create the full path for the JSON file
        json_file_path = os.path.join(json_directory, json_file_name)

        # Convert to JSON
        json_data = json.dumps(xml_dict, indent=2)

        # Write JSON Data to File
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json_file.write(json_data)

        print(f"Converted {xml_file_name} to {json_file_name}")

print("Conversion of XML to JSON completed.")
