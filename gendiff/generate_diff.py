from gendiff.diff import get_diff
from gendiff.parse import load_content
from gendiff.format import stylish, plain

FORMAT = {
    "stylish": stylish,
    "plain": plain
}


def generate_diff(file_path1, file_path2, format_name):
    return FORMAT[format_name](get_diff(
        load_content(file_path1),
        load_content(file_path2)
    ))
