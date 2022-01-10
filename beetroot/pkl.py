import os

from .exception import *

class pkl:
    def pkl(self, fpath, obj):
        try:
            import cPickle as pickle
            
        except (ModuleNotFoundError, ImportError):
            import pickle
            
        with open(fpath, "wb") as f:
            pickle.dump(obj, f)
            f.close()
            
        return 0
    
    def unpkl(self, fpath):
        try:
            import cPickle as pickle
            
        except (ModuleNotFoundError, ImportError):
            import pickle
            
        with open(fpath, "rb") as f:
            out = pickle.load(f)
            f.close()
            return out
        
pkl = pkl()