import yaml

with open("yaml_sample.yaml") as fh:
    yaml_sample = fh.read()

yaml_dict = yaml.load(yaml_sample, Loader=yaml.FullLoader)

# Save the interface name into a variable
int_name = yaml_dict["interface"]["name"]

# Print the interface name
print(int_name)

# Change the IP address of the interface
yaml_dict["interface"]["name"] = "GigabitEthernet1"

# Revert to the yaml string version of the dictionary
print(yaml.dump(yaml_dict, default_flow_style=False))
