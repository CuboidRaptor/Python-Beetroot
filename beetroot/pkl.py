import os

from .exception import *

class pkl:
    def pkl(self, obj, fpath=os.path.abspath(r".\\pkl.pkl")):
        try:
            import cPickle as pickle
            
        except (ModuleNotFoundError, ImportError):
            import pickle
            
        with open(fpath, "wb") as f:
            pickle.dump(obj, f)
            f.close()
            
        return 0
    
    def unpkl(self, fpath=os.path.abspath(".\\pkl.pkl")):
        try:
            import cPickle as pickle
            
        except (ModuleNotFoundError, ImportError):
            import pickle
            
        with open(fpath, "rb") as f:
            out = pickle.load(f)
            f.close()
            return out
        
pkl = pkl()