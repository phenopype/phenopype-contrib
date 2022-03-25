from setuptools import setup, find_packages
import re

## read and format version from file
VERSIONFILE = r"phenopype/contrib/phenomorph/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

## setup
setup(
    name="phenomorph",
    url="https://github.com/agporto/ml-morph",
    author="Arthur Porto",
    author_email="agporto@gmail.com",
    # packages=find_packages(),
    ## not sure these are needed:
    packages=[
        "phenomorph",
        # "phenopype.contrib",
        # "phenopype.contrib.phenomorph"
        ],
    package_dir={
        "phenomorph": "phenopype/contrib/phenomorph",
        # "phenopype.contrib": "phenopype/contrib",
        # "phenopype.contrib.phenomorph": "phenopype/contrib/phenomorph"
        },
    # namespace_packages=['phenopype'],
    install_requires=[
        "phenopype>=3.*",
        "dlib@https://github.com/phenopype/phenopype-dependencies/blob/main/wheels/dlib-19.23.99-cp37-cp37m-win_amd64.whl?raw=true",
    ],
    version=verstr,
    license="LGPL",
    description="A mlmorph module for phenopype",
)

