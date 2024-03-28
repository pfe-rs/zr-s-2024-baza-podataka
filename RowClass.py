import math
import json


class Row:
    def __init__(self):
        self._dictionary = {}
    
    @staticmethod
    def checkAttribute(x):
        if type(x) != str:
            raise TypeError("Atribute name needs to be a string")
    
    @staticmethod
    def checkValue(x):
        if type(x) != str and type(x) != int:
            raise TypeError("Value needs to be a string or an integer")
    
    def addAttribute(self, key, val):
        self.checkAttribute(key)
        self.checkValue(val)

        if key in self._dictionary:
            raise IndexError("The atribute '" + key + "' already exists")
        
        self._dictionary[key] = val

        return True

    def deleteAttribute(self, key):
        self.checkAttribute(key)

        if not (key in self._dictionary):
            raise IndexError("The atribute '" + key + "' dost not exist")
        
        del self._dictionary[key]
        return True
        
    def changeAttribute(self, key, value):
        
        self.checkAttribute(key)
        self.checkValue(value)
        
        if not (key in self._dictionary):
            self.addAttribute(key, value)
        else:
            self._dictionary[key] = value
    
    def getAttribute(self, key):
        self.checkAttribute(key)
        
        if not (key in self._dictionary):
            return None
        
        return self._dictionary[key]