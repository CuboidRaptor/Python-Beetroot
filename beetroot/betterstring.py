import re

from .exception import *
from .text import *

class betterstring:
    """BetterString class"""
    def __init__(self, str_):
        self.string = str_
        
    def zalgo(self, **kwargs):
        craziness = float(
            kwargs.get(
                "crazy",
                1.0
            )
        )
        return text.zalgo(self.__str__(), crazy=craziness)
    
    def udown(self):
        return text.udown(self.__str__())
    
    def rouxls(self):
        return text.rouxls(self.__str__())
    
    def spamton(self):
        return text.spamton(self.__str__())
    
    def allfilters(self, **kwargs):
        craziness = float(
            kwargs.get(
                "crazy",
                1.0
            )
        )
        return text.zalgo(text.udown(text.spamton(text.rouxls(self.__str__()))))
        
    def replace(self, a, b, **kwargs):
        count = int(
            kwargs.get(
                "count",
                0
            )
        )
        flags = " | ".join(
            kwargs.get(
                "flags",
                []
            )
        )
        out = ""
        if flags == "":
            out = eval(f"re.sub(\"\"\"{a}\"\"\", \"\"\"{b}\"\"\", \"\"\"{self.__str__()}\"\"\", count={count})")
            
        else:
            out = eval(f"re.sub(\"\"\"{a}\"\"\", \"\"\"{b}\"\"\", \"\"\"{self.__str__()}\"\"\", count={count}, flags={flags})")
            
        return out
    
    def remove(self, a, **kwargs):
        count = int(
            kwargs.get(
                "count",
                0
            )
        )
        flags = " | ".join(
            kwargs.get(
                "flags",
                []
            )
        )
        out = ""
        if flags == "":
            out = eval(f"re.sub(\"\"\"{a}\"\"\", \"\", \"\"\"{self.__str__()}\"\"\", count={count})")
            
        else:
            out = eval(f"re.sub(\"\"\"{a}\"\"\", \"\", \"\"\"{self.__str__()}\"\"\", count={count}, flags={flags})")
            
        return out
    
    def upper(self):
        return self.__str__().upper()
    
    def title(self):
        return self.__str__().title()
    
    def lower(self):
        return self.__str__().lower()
    
    def split(self, sep=" "):
        return self.__str__().split(sep)
    
    def strip(self):
        return self.__str__().strip()
    
    def to_whitespace(self):
        return self.replace(".", " ")
    
    def to_null(self):
        out = ""
        for i in range(0, len(self.__str__())):
            out = "".join([out, "\x00"])
            
        return out
        
    def __str__(self):
        return self.string
    
    def __int__(self):
        try:
            return int(self.string)
        
        except ValueError:
            try:
                out = 0
                for item in list(self.string):
                    out += ord(str(item))
                    
                return out
            
            except TypeError:
                return ord("\x00")
            
    def __float__(self):
        return float(self.__int__())
    
    def __list__(self):
        return [
            self.__str__()
        ]
    
    def __dict__(self):
        return {
            self.__str__(): None
        }
    
    def __set__(self):
        return {
            self.__str__()
        }
    
    def __tuple__(self):
        return (
            self.__str__()
        )
    
    __repr__ = __str__