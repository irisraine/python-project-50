import json
import yaml


def load_content(file):
    if file.endswith(".json"):
        loader = json.load
    elif file.endswith((".yaml", ".yml")):
        loader = yaml.safe_load
    else:
        raise Exception("Unsupported file format")

    with open(file) as current_file:
        return loader(current_file)
