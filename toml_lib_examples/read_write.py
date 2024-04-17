import toml

# Read the TOML file
config = toml.load("cluster.toml")

# Modify the IP address of host2
config["cluster"]["hosts"]["host2"]["ip"] = "10.0.0.2"

# Write the changes back to the file
with open("cluster.toml", "w") as f:
    toml.dump(config, f)
