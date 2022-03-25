from setuptools import setup, find_packages
import re

## read and format version from file
VERSIONFILE = r"phenopype/contrib/phenodeep/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

## setup
setup(
    name="phenodeep",
    # packages=find_packages(),
    ## not sure these are needed:
    packages=[
        "phenodeep", 
        "phenopype.contrib.phenodeep"
        ],
    package_dir={
        "phenodeep": "phenopype/contrib/phenodeep",
        "phenopype.contrib.phenodeep": "phenopype/contrib/phenodeep"
        },
    # namespace_packages=['phenopype'],
    install_requires=[
        "phenopype>=3.*",
        "tensorflow==2.6.0",
        "keras==2.6.0",
    ],
    version=verstr,
    license="LGPL",
    description="A mlmorph module for phenopype",
)

