from os.path import join
import shutil
from pathlib import Path
from typing import Any


class FileManager:
    @staticmethod
    def get_template_path(dir: str, file: str) -> str:
        return join(
            Path(__file__).parent.parent.parent,
            'templates',
            dir,
            file)

    @staticmethod
    def parse_file(file_path: str) -> str:
        with open(file_path, 'r') as template:
            data = template.read()
        return data

    @staticmethod
    def replace_var(file_path: str, var_name: str,
                    value: Any):
        to_replace = f'$[{var_name}]'
        with open(file_path, 'r') as file:
            text = file.read()

        text = text.replace(to_replace, value)
        with open(file_path, 'w') as file:
            file.write(text)

    @staticmethod
    def copy_file(origin: str, target: str):
        shutil.copyfile(origin, target)

    @staticmethod
    def touch_file(file_path: str) -> Path:
        file = Path(file_path)
        file.touch()
        return file
