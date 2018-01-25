from setuptools import setup
#Nasty hack to get version without importing currently uninstalled module
import re
import os.path as path
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
    license="BSD License"
)