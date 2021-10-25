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

def ga():
    with open(p("./beetroot/metadata.py"), "r", encoding="iso-8859-1") as f:
        code = f.read().split("\n")
        
        version = ""
        author = ""
        ae = ""
        url = ""
        for item in code:
            if item.startswith("__author__"):
                yeet = item.split("\"")
                author = str(yeet[1])
                
            elif item.startswith("__version__"):
                yeet = item.split("\"")
                version = str(yeet[1])
                
            elif item.startswith("__authoremail__"):
                yeet = item.split("\"")
                ae = str(yeet[1])
                
            elif item.startswith("__url__"):
                yeet = item.split("\"")
                url = str(yeet[1])
            
        return [version, author, ae, url]
    
def readme():
    with open(p("./README.rst"), "r", encoding="iso-8859-1") as f:
        return str(f.read())

#Setting up...
setup(
    name="Beetroot",
    version=ga()[0],
    packages=[
        "beetroot"
    ],
    description="A General Purpose Utility package for Python 3",
    url=ga()[3],
    author=ga()[1],
    author_email=ga()[2],
    license="GNU GPLv3",
    install_requires=[
    ],
    long_description=readme(),
    long_description_content_type="text/x-rst",
    extras_require={
        "tts": [
            "pyttsx3>=2.90"
        ],
        "all": [
            "pyttsx3>=2.90"
        ]
    }
)