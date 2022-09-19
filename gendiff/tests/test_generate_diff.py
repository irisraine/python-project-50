from gendiff import generate_diff


def test_simple_stylish_diff():
    try:
        with open("fixtures/expected/simple_stylish.txt") as simple_stylish:
            result = "\n".join(simple_stylish.read().splitlines())
    except FileNotFoundError:
        return "File doesn't exist"
    assert generate_diff(
        "fixtures/file1.json",
        "fixtures/file2.json",
        "stylish") == result
    assert generate_diff(
        "fixtures/file1.yaml",
        "fixtures/file2.yaml",
        "stylish") == result


def test_nested_stylish_diff():
    try:
        with open("fixtures/expected/nested_stylish.txt") as nested_stylish:
            result = "\n".join(nested_stylish.read().splitlines())
    except FileNotFoundError:
        return "File doesn't exist"
    assert generate_diff(
        "fixtures/file1_nested.json",
        "fixtures/file2_nested.json",
        "stylish") == result
    assert generate_diff(
        "fixtures/file1_nested.yaml",
        "fixtures/file2_nested.yaml",
        "stylish") == result


def test_simple_plain_diff():
    try:
        with open("fixtures/expected/simple_plain.txt") as simple_plain:
            result = "\n".join(simple_plain.read().splitlines())
    except FileNotFoundError:
        return "File doesn't exist"
    assert generate_diff(
        "fixtures/file1.json",
        "fixtures/file2.json",
        "plain") == result
    assert generate_diff(
        "fixtures/file1.yaml",
        "fixtures/file2.yaml",
        "plain") == result


def test_nested_plain_diff():
    try:
        with open("fixtures/expected/nested_plain.txt") as nested_plain:
            result = "\n".join(nested_plain.read().splitlines())
    except FileNotFoundError:
        return "File doesn't exist"
    assert generate_diff(
        "fixtures/file1_nested.json",
        "fixtures/file2_nested.json",
        "plain") == result
    assert generate_diff(
        "fixtures/file1_nested.yaml",
        "fixtures/file2_nested.yaml",
        "plain") == result
