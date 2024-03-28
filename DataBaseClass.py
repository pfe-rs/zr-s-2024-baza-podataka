from TableClass import *

class DataBase:
    def __init__(self):
        self._mapTables={}

    @staticmethod
    def _check(x):
        if type(x) != Table:
            raise ValueError("Atribute name needs to be table - map of dictionarys")
    
    @staticmethod
    def _checkName(x):
        if type(x) != str:
            raise ValueError("Name of the table need to be a string")

    '''
    DodatiNakonKonstrukcijeParseInputa()

    def loadDataBase(self):
        temp = input("Please enter your information!!   ") 
        try: 
            with open('ispis.txt', 'w') as ispit: 
            ispis.write(temp) 
        except Exception as e: 
            print("There is a Problem", str(e)) 

    def saveDataBase(self):
    '''
    
    def createTable(self,tableName):
        self._checkName(tableName)
        if tableName in self._mapTables:
            raise IndexError("There is already table named " + tableName)
        
        self._mapTables[tableName] = Table(tableName)
        return True
    
    def dropTable(self,tableName):
        self._checkName(tableName)
        if not (tableName in self._mapTables):
            raise IndexError("There is no table named" + tableName)
        
        del self._mapTables[tableName]
        return True
        
    def getTable(self, tableName):
        self._checkName(tableName)
        return self._mapTables[tableName]
        
    