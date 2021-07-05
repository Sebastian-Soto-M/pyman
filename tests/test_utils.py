import logging
from os import remove
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
        makefile_path = join(
            Path(__file__).parent.parent,
            'templates',
            'common',
            'Makefile')
        cls.makefile_path = f'{makefile_path}.bak'
        utils.copy_file(makefile_path, cls.makefile_path)

    @classmethod
    def tearDownClass(cls):
        remove(cls.makefile_path)

    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        info = FORMAT % (TestUtils.__name__,
                         self.id().split('.')[-1], t)
        self.logger.info(info)

    def test_get_template_path(self):
        expected = self.makefile_path
        result = utils.get_template_path('common', 'Makefile.bak')
        self.assertEqual(result, expected)

    def test_parse_file(self):
        content = utils.parse_file(self.makefile_path)
        expected = 'PYTHON=$[python]'
        lines = content.split('\n')
        self.assertEqual(lines[0], expected)

    def test_replace_var(self):
        utils.replace_var(self.makefile_path, 'python', 'py')
        content = utils.parse_file(self.makefile_path)
        expected = 'PYTHON=py'
        lines = content.split('\n')
        self.assertEqual(lines[0], expected)


if __name__ == "__main__":
    main()
