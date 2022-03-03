from .exception import *

class stopwatch:
    """Stopwatch thingy"""
    def __init__(self):
        import time
        
        self.st = 0
        self.et = 0
        
    def start(self):
        """Starts the stopwatch"""
        import time
        
        self.st = time.perf_counter()
        return 0
    
    def stop(self):
        """Stops the stopwatch and return the elapsed time in ms"""
        import time
        
        self.et = time.perf_counter()
        return round((self.et - self.st) * 1000)