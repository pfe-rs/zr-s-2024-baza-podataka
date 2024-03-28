from DataBaseClass import *

class QueryHandler:
    @staticmethod
    def parseInput(path:str):
        with open(path) as f:
            input = json.load(f)
            # print(input)
            # print(type(input))
            print(f"{path} loaded successfully")

    @staticmethod
    def __create__(tableName: str):
        DataBase.createTable(tableName)


    @staticmethod
    def __drop__(tableName):
        DataBase.dropTable(tableName)

    @staticmethod
    def __insert__(row:Row, tableName:str):
        table = DataBase.getTable(tableName)
        table.insertRow(row)

    @staticmethod
    def __select__(DataListOfKeys, tableName:str, logicalExpression):
        table = DataBase.getTable(tableName)
        table.selectRows(logicalExpression)

    
    @staticmethod
    def __delete__(tableName:str, logicalExpression):
        table = DataBase.getTable(tableName)
        table.deleteRows(logicalExpression)


    @staticmethod
    def __update__(row, tableName: str, logicalExpression):
        table = DataBase.getTable(tableName)
        table.updateRows(logicalExpression)


'''

    @staticmethod
    def parseOutput():
    


    

    @staticmethod
    def __checkExpression__():

    @staticmethod
    def validateExpression():
'''