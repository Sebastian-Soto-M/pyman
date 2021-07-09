from setuptools import find_packages, setup

REPO_BASE_URL = '$[repo_url]'
with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='$[name]',
    version='0.0.1',
    author='$[author]',
    author_email='$[author_email]',
    description='$[description]',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=REPO_BASE_URL,
    project_urls={
        'Bug Tracker': f'{REPO_BASE_URL}/issues',
        'Pull Requests': f'{REPO_BASE_URL}/pulls',
    },
    classifiers=[
        'Programming Language :: Python :: $[python_version]',
        'Operating System :: OS Independent',
    ],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    python_requires='>=$[python_version]',
)
