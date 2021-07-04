from os.path import join
from pathlib import Path


def get_template_path(dir: str, file: str) -> str:
    return join(
        Path(__file__).parent.parent.parent,
        'templates',
        dir,
        file)


def parse_file(file_path: str) -> str:
    with open(file_path, 'r') as template:
        data = template.read()
    return data
