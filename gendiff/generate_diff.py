from gendiff.stylize.format import stringify
from gendiff.parse import load_content


def generate_diff(file1, file2):
    file1_content = load_content(file1)
    file2_content = load_content(file2)

    keys_all = set(file1_content.keys()) | set(file2_content.keys())
    keys_sorted = sorted(list(keys_all))
    diff_list = []
    diff_list.append("{")
    for key in keys_sorted:
        if key in file1_content and key in file2_content:
            if file1_content[key] == file2_content[key]:
                diff_list.append(f'    {key}: {stringify(file1_content[key])}')
            else:
                diff_list.append(f'  - {key}: {stringify(file1_content[key])}')
                diff_list.append(f'  + {key}: {stringify(file2_content[key])}')
        elif key in file1_content:
            diff_list.append(f'  - {key}: {stringify(file1_content[key])}')
        elif key in file2_content:
            diff_list.append(f'  + {key}: {stringify(file2_content[key])}')
    diff_list.append("}")

    return '\n'.join(diff_list)
