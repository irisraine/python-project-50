from gendiff import generate_diff
import pytest
import os

test_cases = [
    ("file1.json", "file2.json", "expected/simple_stylish.txt", "stylish"),
    ("file1.yaml", "file2.yaml", "expected/simple_stylish.txt", "stylish"),
    ("file1_nested.json", "file2_nested.json", "expected/nested_stylish.txt", "stylish"),
    ("file1_nested.yaml", "file2_nested.yaml", "expected/nested_stylish.txt", "stylish"),
    ("file1.json", "file2.json", "expected/simple_plain.txt", "plain"),
    ("file1.yaml", "file2.yaml", "expected/simple_plain.txt", "plain"),
    ("file1_nested.json", "file2_nested.json", "expected/nested_plain.txt", "plain"),
    ("file1_nested.yaml", "file2_nested.yaml", "expected/nested_plain.txt", "plain"),
    ("file1.json", "file2.json", "expected/simple_json.txt", "json"),
    ("file1.yaml", "file2.yaml", "expected/simple_json.txt", "json"),
    ("file1_nested.json", "file2_nested.json", "expected/nested_json.txt", "json"),
    ("file1_nested.yaml", "file2_nested.yaml", "expected/nested_json.txt", "json")
]


def get_fixture_path(local_filename):
    return os.path.join('tests/fixtures', local_filename)


@pytest.mark.parametrize("file1, file2, expected, formatter", test_cases)
def test_universal_case(file1, file2, expected, formatter):
    with open(get_fixture_path(expected), 'r') as result:
        result_content = "\n".join(result.read().splitlines())
    assert generate_diff(
        get_fixture_path(file1),
        get_fixture_path(file2),
        formatter) == result_content
