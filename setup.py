from setuptools import setup, find_packages

REPO_BASE_URL = "https://github.com/Sebastian-Soto-M/pyman"
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pyman",
    version="0.0.1",
    author="Sebastian Soto Madrigal",
    author_email="s.m.sebastian.n@gmail.com",
    description="Python helper for package & project creation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=REPO_BASE_URL,
    project_urls={
        "Bug Tracker": f"{REPO_BASE_URL}/issues",
        "Pull Requests": f"{REPO_BASE_URL}/pulls",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
)
