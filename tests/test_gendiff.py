from gendiff import generate_diff
import pytest
import os.path

test_cases = [
    ("file1.json", "file2.json", "simple_stylish.txt", "stylish"),
    ("file1.yaml", "file2.yaml", "simple_stylish.txt", "stylish"),
    ("file1_nested.json", "file2_nested.json", "nested_stylish.txt", "stylish"),
    ("file1_nested.yaml", "file2_nested.yaml", "nested_stylish.txt", "stylish"),
    ("file1.json", "file2.json", "simple_plain.txt", "plain"),
    ("file1.yaml", "file2.yaml", "simple_plain.txt", "plain"),
    ("file1_nested.json", "file2_nested.json", "nested_plain.txt", "plain"),
    ("file1_nested.yaml", "file2_nested.yaml", "nested_plain.txt", "plain"),
    ("file1.json", "file2.json", "simple_json.txt", "json"),
    ("file1.yaml", "file2.yaml", "simple_json.txt", "json"),
    ("file1_nested.json", "file2_nested.json", "nested_json.txt", "json"),
    ("file1_nested.yaml", "file2_nested.yaml", "nested_json.txt", "json")
]


def get_filepath(filename, filetype):
    current_directory = os.path.dirname(os.path.abspath(filename))
    if filetype == "fixture":
        return os.path.join(current_directory, "fixtures", filename)
    elif filetype == "result":
        return os.path.join(current_directory, "fixtures", "expected", filename)


@pytest.mark.parametrize("file1, file2, expected, format_name", test_cases)
def test_universal_case(file1, file2, expected, format_name):
    try:
        with open(get_filepath(expected, "result")) as simple_stylish:
            result = "\n".join(simple_stylish.read().splitlines())
    except FileNotFoundError:
        return "File doesn't exist"
    assert generate_diff(
        get_filepath(file1, "fixture"),
        get_filepath(file2, "fixture"),
        format_name) == result
