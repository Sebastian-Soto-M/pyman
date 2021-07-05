from os.path import join
from pathlib import Path


class Project:
    def __init__(self, name: str, path: str):
        self.name = name
        self.path = Path(path)
        self.root_path = Path(join(self.path, self.name))

    def create_basic_structure(self):
        self.root_path = Path(join(self.path, self.name))
        if self.root_path.exists():
            raise FileExistsError
        else:
            self.root_path.mkdir(exist_ok=True)
