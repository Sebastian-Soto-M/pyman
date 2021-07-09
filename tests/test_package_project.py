import logging
import shutil
from os.path import join
from pathlib import Path
from unittest import TestCase

from src.pyman.shared.models.project import PackageSetup

from . import TimedTestCase

example_setup = {
    'name': 'pyman_test_package',
    'author': 'Sebastian Soto Madrigal',
    'author_email': 's.m.sebastian.n@gmail.com',
    'description': 'test for package example',
    'repo_url': 'https://github.com/Sebastian-Soto-M/test_pyman',
    'python_version': 3.8
}


class TestPackageSetup(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.tmp_folder = Path(join(Path.home().parent.parent, 'tmp', 'tests'))
        cls.logger = logging.getLogger(cls.__name__)
        cls.pkg_setup: PackageSetup = PackageSetup(**example_setup)
        cls.ttc = TimedTestCase()
        cls.tmp_folder.mkdir(exist_ok=True)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp_folder)
        cls.logger.debug(f'Removed all folders in: {cls.tmp_folder}')

    def setUp(self):
        self.ttc.start()

    def tearDown(self):
        self.ttc.tear_down(self.logger, TestPackageSetup.__name__,
                           self.id().split('.')[-1])

    def test_create_file(self):
        new_file_path = self.pkg_setup.create_file(str(self.tmp_folder))
        self.assertEqual(Path(new_file_path).exists(), True)
