try:
    from psutil import virtual_memory, swap_memory
    
except:
    pass

from .exception import *
from .objtype import *

class m:
    def mem(self):
        try:
            yee = virtual_memory()
            return [yee.total, yee.used, yee.free]
        
        except NameError:
            raise ModuleError("psutil must be installed to use beetroot.mem(). Use pip install psutil or pip install beetroot[ram].")
        
    def swapmem(self):
        try:
            yee = swap_memory()
            return [yee.total, yee.used, yee.free]
        
        except NameError:
            raise ModuleError("psutil must be installed to use beetroot.mem(). Use pip install psutil or pip install beetroot[ram].")
mem = m()
del m