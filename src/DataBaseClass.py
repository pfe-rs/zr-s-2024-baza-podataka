from src.DataBaseClass import *

class DataBase:
    def __init__(self):
        self._mapTables={}

    @staticmethod
    def _check(x):
        if type(x) != Table:
            raise ValueError("Attribute name needs to be table")
    
    @staticmethod
    def _checkName(x):
        if type(x) != str:
            raise ValueError("Name of the table need to be a string")


    ### ostavljeno za kasnije kad se bude radila serijalizacija table i row objekta
    def saveDataBase(self, path):
        try:
            with open(path, "w") as izlaz:
                mp = self.toJSON()
                mapa_tabela = json.dump(mp,izlaz)
        except:
            print("error in saving db")

    # def loadDataBase(self, path):
    #     temp = input("Please enter your information!!   ") 
    #     try: 
    #         with open('ispis.txt', 'w') as ispit: 
    #         ispis.write(temp) 
    #     except Exception as e: 
    #         print("There is a Problem", str(e)) 


    
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
        if not (tableName in self._mapTables):
            raise IndexError("There is no table named" + tableName)
        return self._mapTables[tableName]

    def getAsDictionary(self):
        a = self._mapTables
        tableDict = {}
        for key, value in self._mapTables.items():
            a = value.getAsDictionary()
            tableDict[key]=value.getAsDicitonary()
       
        print(tableDict)
        return tableDict   
      
    def toJSON(self):
        dict = self.getAsDictionary()
        return json.dumps(dict)