import logging
import sys
logging_mode = logging.DEBUG

"""
import logging
import sys

from tests.test_project import TestProject
from tests.test_section import TestSection
from tests.utils import cli_options

TESTS = {
    'project': TestProject,
    'section': TestSection
}


CLI_OPTS = cli_options(TESTS.keys())

logging_mode = logging.INFO if not CLI_OPTS.verbose else logging.DEBUG
"""

FORMAT = '| %-20s\t=>\t%-30s[%.3f]'
logging.basicConfig(level=logging_mode, stream=sys.stdout,
                    format='%(levelname)s\t%(message)s')
