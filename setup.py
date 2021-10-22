#Imports
import sys

#Python2 and Python1 are absolutely illegal
if not sys.version.startswith("3"):
    raise VersionError("Python version is not supported.")

import codecs
import os.path

from setuptools import setup
from pathlib import Path as p

#Exception classes
class VersionError(Exception):
    pass

class AuthorError(Exception):
    pass

def gv():
    with open(p("./beet/__init__.py"), "r", encoding="iso-8859-1") as f:
        code = f.read().split("\n")
        
        for item in code:
            if item.startswith("__version__"):
                yeet = item.split("\"")
                return str(yeet[1])
            
        raise VersionError("Cannot find version from source")

def ga():
    with open(p("./beet/__init__.py"), "r", encoding="iso-8859-1") as f:
        code = f.read().split("\n")
        
        for item in code:
            if item.startswith("__author__"):
                yeet = item.split("\"")
                return str(yeet[1])
            
        raise AuthorError("Cannot find version from source")

#Setting up...
setup(
    name="Beet",
    version=gv(),
    packages=[
        "beet"
    ],
    description="A General Purpose Utility package for python",
    url="https://github.com/CuboidRaptor/Python-Beet",
    author=ga(),
    author_email="fanjas112358@gmail.com",
    license="GNU GPLv3",
    install_requires=[
    ]
)