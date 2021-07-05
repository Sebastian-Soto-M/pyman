import logging
import shutil
from os.path import join

from src.pyman.shared.models.project import Project
from . import FORMAT
from pathlib import Path
import time
from unittest import TestCase, main
from src.pyman.shared.models.exceptions import FileExistsError


class TestProject(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.tmp_folder = Path(join(Path.home().parent.parent, 'tmp', 'tests'))
        cls.tmp_folder.mkdir(exist_ok=True)
        cls.logger = logging.getLogger(cls.__name__)
        cls.project = Project(
            'pyman',
            str(cls.tmp_folder)
        )

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp_folder)
        cls.logger.debug(f'Removed all folders in: {cls.tmp_folder}')

    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        info = FORMAT % (TestProject.__name__,
                         self.id().split('.')[-1], t)
        self.logger.info(info)

    def test_create_basic_structure(self):
        self.project.create_basic_structure()
        self.logger.debug(f'Creating folder: {self.project.root_path}')
        expected = Path(self.project.root_path).exists()
        self.assertEqual(True, expected)

    def test_create_basic_structure_exception(self):
        self.assertRaises(
            FileExistsError,
            self.project.create_basic_structure())
