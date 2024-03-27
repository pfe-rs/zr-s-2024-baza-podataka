class row:
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
    
    def addAttribute(self,name,val):
        self._checkAttribute(name)
        self._checkValue(val)

        if name in self._dictionary:
            raise IndexError("The atribute '" + name + "' already exists")
        
        self._dictionary[name] = val
    
    def deleteAttribute(self, name):
        self._checkAttribute(name)

        if name in self._dictionary:
            del self._dictionary[name]
        
    def changeAttribute(self, name, value):
        self._checkAttribute(name)
        self._checkValue(value)
        
        if not (name in self._dictionary):
            raise IndexError("The atribute '" + name + "' does not exist")
        self._dictionary[name] = value
    
    def getAttribute(self, name):
        self._checkAttribute(name)
        
        if not (name in self._dictionary):
            return None
        
        return self._dictionary[name]