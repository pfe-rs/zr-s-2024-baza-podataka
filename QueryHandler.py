from DataBaseClass import *

class QueryHandler:
    def __init__(self):
        self.db = DataBase()

    def parseInput(self, path:str):
        with open(path) as f:
            input = json.load(f)
            print(f"{path} loaded successfully")
            print(input) ## da vidimo da je sve okej i sta je query, samo test print za sad
            # eval( "__" + input["type"] + "__" ) ### evo eval da bane ima sta da hakuje
            ## salim se bane nista od toga

            # funkcija = locals()["__" + input["type"] + "__"] ## dobro msm mozes i ovako
            # funkcija() ### nahhhh ovo ce biti prekomplikovano ovako

            funkcija = input["type"]
            tabela = input["table"]

            # bez switch-a zbog verzije pythona
            if funkcija == "create":
                self.__create__(tabela)
            if funkcija == "drop":
                self.__drop__(tabela)
            if funkcija == "insert":
                tempRow = Row()
                cols = input["row"]
                for key in cols:
                    tempRow.addAttribute(key,cols[key])
                self.__insert__(tempRow,tabela)

    
    def __create__(self, tableName: str):
        self.db.createTable(tableName)


    
    def __drop__(self, tableName):
        self.db.dropTable(tableName)

    
    def __insert__(self, row:Row, tableName:str):
        table = self.db.getTable(tableName)
        table.insertRow(row)

    
    def __select__(self, DataListOfKeys, tableName:str, logicalExpression):
        table = self.db.getTable(tableName)
        table.selectRows(logicalExpression)

    
    
    def __delete__(self, tableName:str, logicalExpression):
        table = self.db.getTable(tableName)
        table.deleteRows(logicalExpression)


    
    def __update__(self, row, tableName: str, logicalExpression):
        table = self.db.getTable(tableName)
        table.updateRows(logicalExpression)


'''

    
    def parseOutput():
    


    

    
    def __checkExpression__():

    
    def validateExpression():
'''