from setuptools import setup
from setuptools.command.test import test as TestCommand
#Nasty hack to get version without importing currently uninstalled module
import re
import os.path as path
import sys
init_file = open(path.join(path.dirname(__file__), "dns_ui_sdk", "__init__.py")).read()
version = re.findall(r'=.*?$', init_file)[0].split("\"")[1]


setup(
    name="dns-ui-sdk",
    version=version,
    description="Wrapper for the opera DNS-UI",
    author="Vladimir Pershin pershin87@yandex.ru",
    url="https://github.com/operasoftware/dns-ui/",
    packages = ["dns_ui_sdk"],
    install_requires=["requests >=2.2.1"],
    tests_require=['pytest>=2.6.4', 'pytest-cov>=2.1.0', 'pytest-pep8>=1.0.6'],
    license="BSD License"
)