#Dependency function of like almost every class
"""I originally wanted this to be just for objtype(),
but now I have other global functions and nowhere to put them,
and changing the name would've been too hard with my
one billion files."""
import io

from .exception import *

def objtype(obj):
    return str(type(obj))[8:-2]

class suppress(object):
    """Forcibly suppress stdout and stderr, however
    errors and stack traces will still show"""
    def __init__(self):
        import sys

        self.old_stdout = sys.stdout
        self.old_stderr = sys.stderr

    class StdDummy:
        def __init__(self):
            self.closed = False

        def write(self, *args, **kwargs):
            pass

        def writelines(self, *args, **kwargs):
            pass

        def close(self, *args, **kwargs):
            pass

    def __enter__(self):
        import sys

        sys.stdout = self.StdDummy()
        sys.stderr = self.StdDummy()

    def __exit__(self, *args, **kwargs):
        import os
        import sys

        sys.stdout = self.old_stdout
        sys.stderr = self.old_stderr

class progBar:
    """Progress bar. Don't print output between progressing/"""
    def __init__(self, num):
        import os
        import sys
        
        self.cur = 0
        self.end = num
        sys.stdout.write("[")
        
        if self.end == "inf":
            pass
        
        else:
            for i in range(0, self.end):
                sys.stdout.write(" ")
            
        sys.stdout.write("]")
        
    def progress(self):
        import os
        import sys
        
        if self.end == "inf":
            sys.stdout.write("\b \b")
            sys.stdout.write("#")
            self.cur += 1
            sys.stdout.write("]")
            
            return 0
            
        if self.cur < self.end:
            for i in range(0, (self.end-self.cur)+1):
                sys.stdout.write("\b \b")
                
            sys.stdout.write("#")
            self.cur += 1
            
            for i in range(0, self.end-self.cur):
                sys.stdout.write(" ")
                
            sys.stdout.write("]")
            
            return 0
        
        else:
            return 1