try:
    from youtube_search import YoutubeSearch
    
except (ModuleNotFoundError, ImportError):
    pass

from .exception import *
from .objtype import *

class y:
    def search(self, term):
        results = YoutubeSearch(f"{term}", max_results=1).to_dict()
        results = results[0]
        u = "https://www.youtube.com" + results["url_suffix"]
        return u
    
yt = y()
del y
