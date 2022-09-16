from gendiff.format.stringify import stringify


def generate_diff(contents1, contents2):
    keys_common = sorted(set(contents1.keys()) | set(contents2.keys()))
    diff = []

    for key in keys_common:
        value1 = stringify(contents1.get(key, "!none"))
        value2 = stringify(contents2.get(key, "!none"))

        if isinstance(value1, dict) and isinstance(value2, dict):
            diff.append(item(key, generate_diff(value1, value2), "unchanged"))
        elif value1 == value2:
            diff.append(item(key, value1, "unchanged"))
        elif not value2:
            diff.append(item(key, value1, "deleted"))
        elif not value1:
            diff.append(item(key, value2, "added"))
        else:
            diff.append(item(key, value1, "deleted"))
            diff.append(item(key, value2, "added"))
    return diff


def item(key, value, action):
    return {
        "key": key,
        "value": value,
        "action": action
    }
