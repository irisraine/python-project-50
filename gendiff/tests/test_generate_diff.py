from gendiff import generate_diff


def test_generate_diff():
    try:
        with open("fixtures/expected/json_plain_result.txt") as json_plain:
            result = "\n".join(json_plain.read().splitlines())
    except FileNotFoundError:
        return "File doesn't exist"

    assert generate_diff("fixtures/file1.json", "fixtures/file2.json") == result
    assert generate_diff("fixtures/file1.yaml", "fixtures/file2.yaml") == result
