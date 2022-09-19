from gendiff.diff import get_diff
from gendiff.parse import load_content
from gendiff.format import stylish_format, plain_format, json_format

FORMAT = {
    "stylish": stylish_format,
    "plain": plain_format,
    "json": json_format
}


def generate_diff(file_path1, file_path2, format_name="stylish_format"):
    return FORMAT[format_name](get_diff(
        load_content(file_path1),
        load_content(file_path2)))
