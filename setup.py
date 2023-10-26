from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in axistalent8848/__init__.py
from axistalent8848 import __version__ as version

setup(
	name="axistalent8848",
	version=version,
	description="Axis Talent App",
	author="Prashant Kamble",
	author_email="prashantkamble@8848digital.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
