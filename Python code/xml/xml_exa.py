import xmltodict

with open("xml_sample.xml") as fh:
    xml_example = fh.read()
    
xml_dict = xmltodict.parse(xml_example)

# Save the interface name into a variable using XML nodes as keys
int_name = xml_dict["interface"]["name"]

# Print the interface name
print(int_name)

# Change the IP address of the interface
xml_dict["interface"]["ipv4"]["address"]["ip"] = "192.168.55.3"

# Revert to the XML string version of the dictionary
print(xmltodict.unparse(xml_dict, pretty=True))


with open("xml_sample.xml", "w") as fh:
    fh.write(xmltodict.unparse(xml_dict, pretty=True))
    
    