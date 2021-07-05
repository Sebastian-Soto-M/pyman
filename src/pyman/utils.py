from os.path import join
import shutil
from pathlib import Path
from typing import Any


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


def replace_var(file_path: str, var_name: str,
                value: Any):
    to_replace = f'$[{var_name}]'
    with open(file_path, 'r') as file:
        text = file.read()

    text = text.replace(to_replace, value)
    with open(file_path, 'w') as file:
        file.write(text)


def copy_file(origin: str, target: str):
    shutil.copyfile(origin, target)
