from gendiff import generate_diff
from gendiff.parse import load_content
from gendiff.format import stylish

json_simple1 = load_content("fixtures/file1.json")
json_simple2 = load_content("fixtures/file2.json")
yaml_simple1 = load_content("fixtures/file1.yaml")
yaml_simple2 = load_content("fixtures/file2.yaml")
json_nested1 = load_content("fixtures/file1_nested.json")
json_nested2 = load_content("fixtures/file2_nested.json")
yaml_nested1 = load_content("fixtures/file1_nested.yaml")
yaml_nested2 = load_content("fixtures/file2_nested.yaml")


def test_simple_diff():
    try:
        with open("fixtures/expected/simple_stylish.txt") as simple_stylish:
            result = "\n".join(simple_stylish.read().splitlines())
    except FileNotFoundError:
        return "File doesn't exist"
    assert stylish(generate_diff(json_simple1, json_simple2)) == result
    assert stylish(generate_diff(yaml_simple1, yaml_simple2)) == result


def test_nested_diff():
    try:
        with open("fixtures/expected/nested_stylish.txt") as nested_stylish:
            result = "\n".join(nested_stylish.read().splitlines())
    except FileNotFoundError:
        return "File doesn't exist"
    assert stylish(generate_diff(json_nested1, json_nested2)) == result
    assert stylish(generate_diff(yaml_nested1, yaml_nested2)) == result
