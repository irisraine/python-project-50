import json
from gendiff.stylize.format import stringify


def generate_diff(file_path1, file_path2):
    try:
        with open(file_path1) as json1:
            json1_content = json.load(json1)
        with open(file_path2) as json2:
            json2_content = json.load(json2)
    except FileNotFoundError:
        return "File doesn't exist"

    keys_all = set(json1_content.keys()) | set(json2_content.keys())
    keys_sorted = sorted(list(keys_all))
    diff_list = []
    diff_list.append("{")
    for key in keys_sorted:
        if key in json1_content and key in json2_content:
            if json1_content[key] == json2_content[key]:
                diff_list.append(f'    {key}: {stringify(json1_content[key])}')
            else:
                diff_list.append(f'  - {key}: {stringify(json1_content[key])}')
                diff_list.append(f'  + {key}: {stringify(json2_content[key])}')
        elif key in json1_content:
            diff_list.append(f'  - {key}: {stringify(json1_content[key])}')
        elif key in json2_content:
            diff_list.append(f'  + {key}: {stringify(json2_content[key])}')
    diff_list.append("}")

    return '\n'.join(diff_list)