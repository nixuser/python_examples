import toml

# Load the TOML file
config = toml.load("config.toml")

# Modify the config
config["cluster"]["hosts"]["host2"]["ip"] = "10.0.0.2"

# Write the config back to disk
with open("config.toml", "w") as f:
    toml.dump(config, f)
