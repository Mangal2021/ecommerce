from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ecom_test/__init__.py
from ecom_test import __version__ as version

setup(
	name="ecom_test",
	version=version,
	description="asdf",
	author="asdf",
	author_email="abc@def.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
