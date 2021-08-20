import json

with open("json_sample.json") as fh:
    json_data = fh.read()

print(json_data)

# Parse the json into a Python dictionary
json_dict = json.loads(json_data)

# Save the interface name into a variable
int_name = json_dict["interface"]["name"]

# Print the interface name
print(int_name)

# Change the IP address of the interface
json_dict["interface"]["description"] = "Backup Link"

# Revert to the json string version of the dictionary
print(json.dumps(json_dict, indent = 4))

with open("json_sample.json", "w") as fh:
    json.dump(json_dict, fh, indent = 4)
    
with open ("json_sample.json") as fh:
    json_data = fh.read()
    print(json_data)