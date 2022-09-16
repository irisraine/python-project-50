import json


def stringify(value):
    if value == "!none":
        return None
    return json.dumps(value) if not isinstance(value, dict) else value
