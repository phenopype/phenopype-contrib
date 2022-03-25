from setuptools import setup, find_packages
import re

## read and format version from file
VERSIONFILE = "_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))
    
## setup
setup(
    name="phenopype-contrib",
    url="https://www.phenopype.org",
    maintainer="Moritz Lürig",
    maintainer_email="moritz.luerig@gmail.com",
    author="Arthur Porto; Moritz Lürig",
    author_email="agporto@gmail.com; moritz.luerig@gmail.com",
    # packages=find_packages(),
    # not sure these are needed:
    packages=[
        "phenopype",
        "phenopype.contrib"
    ],
    package_dir={
        "phenopype": r"phenomorph\phenopype",
        "phenopype.contrib": "phenomorph\phenopype\contrib"
    },
    # namespace_packages=['phenopype'],
    install_requires=[
        "phenopype>=3.*",
        # "phenomorph"
        f"phenomorph @ file://localhost/{os.getcwd()}\phenomorph"
    ],
    version=verstr,
    license="LGPL",
    description="A mlmorph module for phenopype",
) 