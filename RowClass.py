import math

class Row:
    def __init__(self):
        self._dictionary = {}
    
    @staticmethod
    def _checkAttribute(x):
        if type(x) != str:
            raise TypeError("Atribute name needs to be a string")
    
    @staticmethod
    def _checkValue(x):
        if type(x) != str and type(x) != int:
            raise TypeError("Value needs to be a string or an integer")
    
    def addAttribute(self, key, val):
        self._checkAttribute(key)
        self._checkValue(val)

        if key in self._dictionary:
            raise IndexError("The atribute '" + key + "' already exists")
        
        self._dictionary[key] = val

        return True

    def deleteAttribute(self, key):
        self._checkAttribute(key)

        if not (key in self._dictionary):
            raise IndexError("The atribute '" + key + "' dost not exist")
        
        del self._dictionary[key]
        return True
        
    def changeAttribute(self, key, value):
        
        self._checkAttribute(key)
        self._checkValue(value)
        
        if not (key in self._dictionary):
            self.addAttribute(key, value)
        else:
            self._dictionary[key] = value
    
    def getAttribute(self, key):
        self._checkAttribute(key)
        
        if not (key in self._dictionary):
            return None
        
        return self._dictionary[key]