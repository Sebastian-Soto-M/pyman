import shutil
from os.path import join
from pathlib import Path
from typing import Any, Union

from src.pyman.shared.models.enums import FileTemplates


class FileManager:
    @staticmethod
    def get_template_path(dir: str, file: Union[str, FileTemplates]) -> str:
        """
        Returns the template file requested from the templates folder
        """
        if isinstance(file, FileTemplates):
            return join(Path(__file__).parent.parent.parent,
                        'templates', dir, file.value)
        return join(Path(__file__).parent.parent.parent,
                    'templates', dir, file)

    @staticmethod
    def parse_file(file_path: str) -> str:
        """ Retruns the contents of a file """
        with open(file_path, 'r') as template:
            data = template.read()
        return data

    @staticmethod
    def replace_variables(file_path: str, vars_to_replace: dict[str, Any]):
        """
        Replaces the var_name instances in the file specified with the
        value defined

        var_name = python | value = py
        $[python] -> py
        """
        with open(file_path, 'r') as file:
            text = file.read()

        for k, v in vars_to_replace.items():
            text = text.replace(f'$[{k}]', str(v))

        with open(file_path, 'w') as file:
            file.write(text)

    @staticmethod
    def copy_file(origin: str, target: str) -> str:
        """ Returns the path of the copied file """
        shutil.copyfile(origin, target)
        return target

    @staticmethod
    def touch_file(file_path: str) -> Path:
        file = Path(file_path)
        file.touch()
        return file
