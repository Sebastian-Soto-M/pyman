from setuptools import find_packages, setup

REPO_BASE_URL = 'https://github.com/Sebastian-Soto-M/pyman'
with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='pyman',
    version='0.0.1',
    author='Sebastian Soto Madrigal',
    author_email='s.m.sebastian.n@gmail.com',
    description='Python helper for package & project creation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=REPO_BASE_URL,
    project_urls={
        'Bug Tracker': f'{REPO_BASE_URL}/issues',
        'Pull Requests': f'{REPO_BASE_URL}/pulls',
    },
    classifiers=[
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Code Generators'
        'License :: OSI Approved :: MIT License',
    ],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    python_requires='>=3.9',
)
