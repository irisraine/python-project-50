import json


def stringify(value):
    return json.dumps(value) if not isinstance(value, dict) else value
