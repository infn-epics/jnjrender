# setup.py

from setuptools import setup, find_packages

setup(
    name="jnja2yaml",
    version="0.1.0",
    packages=find_packages(),
    description="A utility to render Jinja2 templates into YAML",
    author="Andrea Michelotti",
    install_requires=[
        "jinja2",
        "pyyaml",
    ],
    entry_points={
        "console_scripts": [
            "jnja2yaml=jnja2yaml.cli:main",
        ],
    },
)
