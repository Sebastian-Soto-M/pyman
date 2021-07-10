import logging
import shutil
from os.path import join
from pathlib import Path
from unittest import TestCase

from src.pyman.shared.models.project import BasicProject, Project

from . import TimedTestCase


class TestBasicProject(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.tmp_folder = Path(join(Path.home().parent.parent, 'tmp', 'tests'))
        cls.logger = logging.getLogger(cls.__name__)
        cls.project: Project = BasicProject('pyman', str(cls.tmp_folder))
        cls.ttc = TimedTestCase()

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp_folder)
        cls.logger.debug(f'Removed all folders in: {cls.tmp_folder}')

    def setUp(self):
        self.ttc.start()

    def tearDown(self):
        self.ttc.tear_down(self.logger, TestBasicProject.__name__,
                           self.id().split('.')[-1])

    def test_create_module(self):
        mod = self.project.create_module(['mod_test'])
        result = [f.name for f in mod.iterdir()]
        expected = ['__init__.py']
        self.assertEqual(result, expected)

    def test_create_module_with_main(self):
        mod = self.project.create_module(['mod_w_main_test'], True)
        result = [f.name for f in mod.iterdir()]
        expected = ['__init__.py', '__main__.py']
        self.assertEqual(result, expected)

    def test_create_basic_structure(self):
        self.project.create()
        self.logger.debug(f'Creating folder: {self.project.root_path}')
        result = Path(self.project.root_path).exists()
        self.assertEqual(result, True)
