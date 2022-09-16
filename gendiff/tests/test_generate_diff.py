from gendiff import generate_diff
from gendiff.parse import load_content
from gendiff.format import stylish


def test_simple_stylish_diff():
    try:
        with open("fixtures/expected/simple_stylish.txt") as simple_stylish:
            result = "\n".join(simple_stylish.read().splitlines())
    except FileNotFoundError:
        return "File doesn't exist"
    assert stylish(generate_diff(
        load_content("fixtures/file1.json"),
        load_content("fixtures/file2.json"))) == result
    assert stylish(generate_diff(
        load_content("fixtures/file1.yaml"),
        load_content("fixtures/file2.yaml"))) == result


def test_nested_stylish_diff():
    try:
        with open("fixtures/expected/nested_stylish.txt") as nested_stylish:
            result = "\n".join(nested_stylish.read().splitlines())
    except FileNotFoundError:
        return "File doesn't exist"
    assert stylish(generate_diff(
        load_content("fixtures/file1_nested.json"),
        load_content("fixtures/file2_nested.json"))) == result
    assert stylish(generate_diff(
        load_content("fixtures/file1_nested.yaml"),
        load_content("fixtures/file2_nested.yaml"))) == result
