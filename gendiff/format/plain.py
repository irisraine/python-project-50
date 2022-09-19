import re


def plain(diff, path=""):
    formatter = ""
    for item in diff:
        key, value = item['key'], normalize(item['value'])
        action = item['action']
        if action == "nested":
            formatter += plain(value, path=path + f"{key}.") + "\n"
        elif action == "added":
            formatter += f"Property '{path}{key}' was added with value: "
            formatter += f"{value}\n"
        elif action == "deleted":
            formatter += f"Property '{path}{key}' was removed\n"
        elif action == "updated":
            formatter += f"Property '{path}{key}' was updated. "
            formatter += f"From {value[0]} to {value[1]}\n"
    return formatter.strip()


def normalize(raw_value):
    if isinstance(raw_value, dict):
        return "[complex value]"
    elif isinstance(raw_value, tuple):
        return normalize(raw_value[0]), normalize(raw_value[1])
    elif isinstance(raw_value, str):
        if re.match("(true)|(false)|(null)|([0-9]+)", raw_value):
            return raw_value
        else:
            raw_value = raw_value.strip('"')
            return f"'{raw_value}'"
    else:
        return raw_value
