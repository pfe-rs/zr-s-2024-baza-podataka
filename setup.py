from setuptools import find_packages
from setuptools import setup

setup(
    name='pfedb',
    version='0.1.0',
    packages=find_packages(),
    package_dir={'':'.','pfedb': 'src','db_tests':'tests'}
)