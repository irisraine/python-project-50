from gendiff.helpers.stringify import stringify


def plain_format(diff, path=""):
    formatter = ""
    for item in diff:
        key, value = item['key'], normalize(item['value'])
        action = item['action']
        if action == "nested":
            formatter += plain_format(value, path=path + f"{key}.") + "\n"
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
        raw_value = stringify(raw_value).strip('"')
        return f"'{raw_value}'"
    elif isinstance(raw_value, bool) or not raw_value:
        return stringify(raw_value).strip('"')
    else:
        return raw_value

