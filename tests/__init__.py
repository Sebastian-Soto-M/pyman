import logging
import sys
import time

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


class TimedTestCase:
    __start_time: float = 0.0
    __end_time: float = 0.0

    def start(self):
        self.__start_time = time.time()

    def __end(self):
        self.__end_time = time.time() - self.__start_time

    def __log(self, logger: logging.Logger, class_name: str, id: str):
        logger.info(
            FORMAT % (class_name, id.split('.')[-1], self.__end_time)
        )

    def tear_down(self, logger: logging.Logger, class_name: str, id: str):
        self.__end()
        self.__log(logger, class_name, id)
