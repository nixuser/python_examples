import rtoml
from pathlib import Path

# Read the TOML file
cluster_file = Path("./cluster.toml")
config = rtoml.load(cluster_file)

# Modify the IP address of host2
config["cluster"]["hosts"]["host2"]["ip"] = "10.1.1.2"

# Write the changes back to the file
with open("cluster.toml", "w") as f:
    rtoml.dump(config, f)
