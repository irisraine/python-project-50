import json

LEFT_BRACE = "{"
RIGHT_BRACE = "}"
INDENT = "    "
ADD = "  + "
DELETE = "  - "


def stylish(diff, depth=1):
    format_stylish = f"{LEFT_BRACE}\n"
    for item in diff:
        key, value, action = item['key'], item['value'], item['action']
        if isinstance(item['value'], list):
            format_stylish += f"{indentor(depth, action)}{key}: "
            format_stylish += f"{stylish(value, depth + 1)}\n"
        elif isinstance(value, dict):
            format_stylish += f"{indentor(depth, action)}{key}: {LEFT_BRACE}\n"
            format_stylish += get_tree(value, depth + 1)
            format_stylish += f"{indentor(depth)}{RIGHT_BRACE}\n"
        else:
            value = value.strip('"')
            format_stylish += f"{indentor(depth, action)}{key}: {value}\n"
    format_stylish += f"{indentor(depth - 1)}{RIGHT_BRACE}"
    return format_stylish


def get_tree(raw, depth=0):
    tree = ""
    for key, value in raw.items():
        if isinstance(value, dict):
            tree += f"{indentor(depth)}{key}: {LEFT_BRACE}\n"
            tree += f"{get_tree(value, depth + 1)}"
            tree += f"{indentor(depth)}{RIGHT_BRACE}\n"
        else:
            value = json.dumps(value).strip('"')
            tree += f"{indentor(depth)}{key}: {value}\n"
    return tree


def indentor(depth, mode="unchanged"):
    if mode == "added":
        return INDENT * (depth - 1) + ADD
    if mode == "deleted":
        return INDENT * (depth - 1) + DELETE
    if mode == "unchanged":
        return INDENT * depth
