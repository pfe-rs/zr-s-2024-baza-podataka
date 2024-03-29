from src.DataBaseClass import *
from src.RowClass import *
from src.LogicalExpressionClass import *

import threading 

class QueryHandler:
    mutex = threading.Lock()

    def __init__(self):
        if self.db == None:
            self.db = DataBase()

    def readInputFromFile(self, path:str):
        with open(path, "r") as file:
            self.parseInput(file.read())

    def parseInput(self, jsonInput:str):
        self.mutex.acquire()

        returnval = "" 
        input = json.loads(jsonInput)
        # print(input) ## da vidimo da je sve okej i sta je query, samo test print za sad
        # eval( "__" + input["type"] + "__" ) ### evo eval da bane ima sta da hakuje
        ## salim se bane nista od toga

        # funkcija = locals()["__" + input["type"] + "__"] ## dobro msm mozes i ovako
        # funkcija() ### nahhhh ovo ce biti prekomplikovano ovako
        funkcija = input["type"]
        tabela = input["table"]
        try: 
            where = input["where"] ## ako ima where polje
        except:
            pass

        # bez switch-a zbog verzije pythona
        if funkcija == "create":
            returnval = self.__create__(tabela)
        if funkcija == "drop":
            returnval = self.__drop__(tabela)
        if funkcija == "insert":
            tempRow = Row()
            cols = input["row"]
            for key in cols:
                tempRow.addAttribute(key,cols[key])
            returnval = self.__insert__(tempRow, tabela)
        
        if funkcija == "delete":
            tempExpression = LogicalExpression(where)
            returnval = self.__delete__( tabela, tempExpression)

        if funkcija == "update":
            tempRow = Row()
            cols = input["row"]
            for key in cols:
                tempRow.addAttribute(key,cols[key])
            tempExpression = LogicalExpression(where)
            returnval = self.__update__(tempRow, tabela, tempExpression)

        if funkcija == "select":
            tempExpression = LogicalExpression(where)
            returnval = self.__select__(tabela, tempExpression)
        

        self.mutex.release()
        return returnval
            
    
    def __create__(self, tableName : str):
        status = self.db.createTable(tableName)
        return f"addition {status}"


    
    def __drop__(self, tableName):
        status = self.db.dropTable(tableName)
        return f"drop {status}"

    
    def __insert__(self, row : Row, tableName : str):
        table = self.db.getTable(tableName)
        status = table.insertRow(row)
        return f"insert {status}"


    
    def __select__(self, tableName : str, logicalExpression : LogicalExpression):
        table = self.db.getTable(tableName)
        result = table.selectRows(logicalExpression)
        # print(result.toJSON())
        return result.toJSON()

    
    
    def __delete__(self, tableName:str, logicalExpression):
        table = self.db.getTable(tableName)
        status = table.deleteRows(logicalExpression)
        return f"delete {status}"

    def __update__(self, newRow, tableName: str, logicalExpression):
        table = self.db.getTable(tableName)
        status = table.updateRows(logicalExpression,newRow)
        return f"update {status}"


'''

    
    def parseOutput():
    


    

    
    def __checkExpression__():

    
    def validateExpression():
'''