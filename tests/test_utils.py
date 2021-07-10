import logging
import time
from os import remove
from os.path import join
from pathlib import Path
from unittest import TestCase

from src.pyman.shared.models.enums import ETemplate
from src.pyman.utils import FileManager

from . import FORMAT


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
        FileManager.copy_file(makefile_path, cls.makefile_path)

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
        expected = self.makefile_path.split('.')[0]
        result = FileManager.get_template_path(ETemplate.MAKEFILE)
        self.assertEqual(result, expected)

    def test_parse_file(self):
        content = FileManager.parse_file(self.makefile_path)
        expected = 'PYTHON=$[python]'
        lines = content.split('\n')
        self.assertEqual(lines[0], expected)

    def test_replace_var(self):
        FileManager.replace_variables(self.makefile_path, {'python': 'py'})
        content = FileManager.parse_file(self.makefile_path)
        expected = 'PYTHON=py'
        lines = content.split('\n')
        self.assertEqual(lines[0], expected)
