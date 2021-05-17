import os
import re
from setuptools import setup, find_packages


def parse_requirements(file):
    with open(os.path.join(os.path.dirname(__file__), file)) as req_file:
        return [line.strip() for line in req_file if '/' not in line]


def get_version():
    with open(os.path.join(os.path.dirname(__file__), 'sr', '__init__.py')) as file:
        return re.findall("__version__ = \'(.*)\'", file.read())[0]


setup(
    name='sr',
    python_requires='>=3.6',
    version=get_version(),
    description='EO Research - Super Resolution',
    url='https://github.com/sentinel-hub/multi-temporal-super-resolution',
    author='Sinergise EO research team',
    author_email='eoresearch@sinergise.com',
    packages=find_packages(),
    install_requires=parse_requirements('requirements.txt'),
    extras_require={
        'DEV': parse_requirements('requirements-dev.txt')
    },
    zip_safe=False
)