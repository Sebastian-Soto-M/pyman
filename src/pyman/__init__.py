from typing import Any
from argparse import Namespace
from .shared.models import CLI, Argument


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


OPTIONS = cli_options()
