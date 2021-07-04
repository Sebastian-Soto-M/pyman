from os.path import join
from typing import Any
from pathlib import Path
from argparse import ArgumentParser, Namespace
from typing import Optional, Set
from pydantic import BaseModel

FORMAT = '| %-20s\t=>\t%-30s[%.3f]'


class Argument:
    def __init__(self, flag: str, name: str, help: str,
                 type: type = bool, choices: Optional[Set[str]] = None):
        self.__flag = flag
        self.__name = name
        self.help = help
        self.type = type
        self.choices = choices

    @property
    def flag(self):
        return f'-{self.__flag}'

    @property
    def name(self):
        return f'--{self.__name}'


class CLI(BaseModel):
    name: str
    arguments: Optional[Set[Argument]]
    flags: Optional[Set[Argument]]
    values: Optional[Namespace]

    def __parse_data(self) -> Namespace:
        parser = ArgumentParser(self.name)
        self.__parse_flags(parser)
        self.__parse_args(parser)
        return parser.parse_args()

    def __parse_args(self, parser: ArgumentParser):
        if self.arguments is not None:
            for a in self.arguments:
                parser.add_argument(a.flag, a.name,
                                    type=a.type, default=False, choices=a.choices)

    def __parse_flags(self, parser: ArgumentParser):
        if self.flags is not None:
            for f in self.flags:
                parser.add_argument(f.flag, f.name, help=f.help,
                                    action='store_true', default=False)

    def read(self) -> Namespace:
        return self.__parse_data() if self.values is None else self.values

    class Config:
        arbitrary_types_allowed = True


def templates_path(dir: str, file: str) -> str:
    file_path = join(Path(__file__).parent.parent, 'templates', dir, file)
    with open(file_path, 'r') as template:
        data = template.read()
    return data


def cli_options() -> Namespace:
    options: dict[str, Any] = {
        "name": "Pyman (Code generator tool)",
        "flags": set(),
        "arguments": {
            Argument(
                't', 'type', 'The type of generated code that will be generated',
                str, {'package', 'api', 'common'})
        }
    }
    return CLI(**options).read()


opts = cli_options()

print(opts)
