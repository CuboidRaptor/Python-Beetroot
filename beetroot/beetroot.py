#Beetroot, a general purpose library for all sorts of uses.

#Imports
import sys

from .exception import *

if not str(sys.version).startswith("3"):
    #HOW DARE YOU USE PYTHON2 IDIOT. or python4, if that ever exists
    #well I mean, if it's like a massive database or smth and you don't wanna migrate 1k+ lines of code then I understand, BUT STILL.
    raise VersionError("Python version is not supported.")

#More imports
import platform
import getpass
import socket
import uuid
import hashlib
import webbrowser
import datetime

try:
    import ujson as json
    
except (ModuleNotFoundError, ImportError):
    try:
        import simplejson as json
        
    except (ModuleNotFoundError, ImportError):
        import json
    

from pathlib import Path as p

from .metadata import *
from .random import *
from .stopwatch import *
from .file import *
from .tts import *
from .objtype import *

#Constants
gen = mrandom.SystemRandom()
sys.setrecursionlimit(32767)
    
def strhash(str_, secure=True):
    """Hash Function that uses MD5 or SHA512."""
    
    if objtype(secure) != "bool":
        raise InvalidHashSecurityValue("Argument \"secure\" can only be boolean")
    
    if objtype(b) != "bytes":
        raise InvalidHashTypeError("Argument \"str_\" can only be string or non-bytestring object")
    
    if secure:
        return hashlib.sha512(str(str_).encode("iso-8859-1")).hexdigest()
    
    elif not secure:
        return hashlib.md5(str(str_).encode("iso-8859-1")).hexdigest()
        
    else:
        raise UnknownError("¯\_(ツ)_/¯")
    
def bhash(b, secure=True):
    """Hash Function that uses MD5 or SHA512."""
    
    if objtype(secure) != "bool":
        raise InvalidHashSecurityValue("Argument \"secure\" can only be boolean")
    
    if objtype(b) != "bytes":
        raise InvalidHashTypeError("Argument \"b\" can only be bytestring")
    
    if secure:
        return hashlib.sha512(b).hexdigest()
    
    elif not secure:
        return hashlib.md5(b).hexdigest()
        
    else:
        raise UnknownError("¯\_(ツ)_/¯")
        
def test():
    """Test"""
    print("Hello, world!")
    return 0
    
def quicksort(array):
    """Quicksort algorithm"""

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        
        for x in array:
            if x < pivot:
                less.append(x)
                
            elif x == pivot:
                equal.append(x)
                
            elif x > pivot:
                greater.append(x)
                
        return quicksort(less) + equal + quicksort(greater)
    
    else:
        return array

def lsep(str_, sep=" "):
    """Seperates string str_ by seperator sep whilst avoiding all strings containing whitespace"""
    a = str_.split(sep)
    
    out = []
    for i in range(0, len(a)):
        if (not a[i].isspace()) and a[i] != "":
            out.append(a[i])
            
    return out

def execfile(file):
    """Executes a python .py script"""
    with open(p(file), "r", encoding="iso-8859-1") as f:
        exec(f.read())
        f.close()
        
    return 0

def systemstats():
    """Returns info about system and hardware"""
    return [getpass.getuser(), platform.system(), platform.version(), platform.machine(), platform.node(), socket.gethostbyname(socket.gethostname()), ':'.join(("%012X" % uuid.getnode())[i:i+2] for i in range(0, 12, 2)).lower()]

def unline(str_):
    """Makes multi-line strings single-line"""
    return str(str_).replace("\n", "\\n").replace("\t", "\\t").replace("\r", "\\r").replace("\a", "\\a").replace("\b", "\\b")

def reline(str_):
    """Reverses beetroot.unline()"""
    return str(str_).replace("\\n", "\n").replace("\\t", "\t").replace("\\r", "\r").replace("\\a", "\a").replace("\\b", "\b")

def beetroot():
    """BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT BEETROOT-"""
    while True:
        get_beetrolled = True
        print("""

██████╗░███████╗███████╗████████╗██████╗░░█████╗░░█████╗░████████╗
██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝
██████╦╝█████╗░░█████╗░░░░░██║░░░██████╔╝██║░░██║██║░░██║░░░██║░░░
██╔══██╗██╔══╝░░██╔══╝░░░░░██║░░░██╔══██╗██║░░██║██║░░██║░░░██║░░░
██████╦╝███████╗███████╗░░░██║░░░██║░░██║╚█████╔╝╚█████╔╝░░░██║░░░
╚═════╝░╚══════╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░░╚════╝░░░░╚═╝░░░""", end="", flush=True)
        time.sleep(0.5)
        
    return 69420

def totally_not_a_rickroll():
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ", new=0)
    return "".join(["U JUST GOT RICKROLLED IN ", str(datetime.datetime.now().year)])