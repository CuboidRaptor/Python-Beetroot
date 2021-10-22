#Imports
import sys

from setuptools import setup

#Exception class
class VersionError(Exception):
    pass

#Python2 and Python1 are absolutely illegal
if not sys.version.startswith("3"):
    raise VersionError("Python version is not supported.")

#Setting up...
setup(
    name="Beet",
    version="1.0.5",
    packages=[
        "beet"
    ]
)