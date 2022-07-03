from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in births_and_deaths_registration/__init__.py
from births_and_deaths_registration import __version__ as version

setup(
	name="births_and_deaths_registration",
	version=version,
	description="Births and Deaths Registration System",
	author="IoT Communications (Pty) Ltd",
	author_email="info@iotcomms.co.bw",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
