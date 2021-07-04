import logging
from os.path import join
from pathlib import Path
import time
from . import FORMAT
from src.pyman import utils
from unittest import TestCase, main


class TestUtils(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.logger = logging.getLogger(cls.__name__)

    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        info = FORMAT % (TestUtils.__name__,
                         self.id().split('.')[-1], t)
        self.logger.info(info)

    def test_get_template_path(self):
        expected = join(
            Path(__file__).parent.parent,
            'templates',
            'common',
            'Makefile')
        result = utils.get_template_path('common', 'Makefile')
        self.assertEqual(result, expected)

    def test_read_file(self):
        file_path = utils.get_template_path('common', 'Makefile')
        content = utils.parse_file(file_path)
        self.logger.info(content)


if __name__ == "__main__":
    main()
