from RowClass import *

def Evaluate(log, row): # Example evaluation function for testing purposes
    if row["id"] % 2 == 0:
        return False
    return True

class Table:
    def __init__(self, name):
        self.mapRows = {}
        self.tableName = name
        self.maxId=0

    def getRow(self, rowId):
        if type(rowId)!=int:
            raise ValueError("Id needs to be an integer")
        if not (id in self.mapRows):
            raise IndexError("Requested id does not exist")

        self._checkExistance(rowId)
        return self.mapRows[rowId]

    def insertRow(self, row):
        if type(row) != Row:
            raise TypeError("Row value needs to be a row")

        if "id" in row:
            if type(row["id"]) != int:
                raise ValueError("Id needs to be an integer")

            id = row["id"]
        else:
            id = self.maxId+1
        
        if id in self.mapRows:
            raise ValueError("The row with that id already exists")

        row["id"]=id

        self.maxId = math.max(self.maxId, id)
        self.mapRows[id]=row
        return True

    def deleteRow(self, rowId):
        if type(rowId)!=int:
            raise ValueError("Id needs to be an integer")
        if not (id in self.mapRows):
            raise IndexError("Requested id does not exist")
        
        del self.mapRows[rowId]
        return True 
    
    def changeRow(self, rowId, newRow):
        if type(newRow) != Row:
            raise TypeError("Row value needs to be a row")
        
        if "id" in newRow:
            raise ValueError("You cannot change id of a row")
        
        oldRow = self.getRow(rowId)
        for key, value in newRow:
            oldRow.changeAttribute(key, value)
        return True
    
    def getName(self):
        return self.tableName
    
    def selectRows(self, logicalExpression):
        resultTable = Table("ResultTable")
        for key, value in self.mapRows:
            if Evaluate(logicalExpression, value):
                resultTable[key] = value

        return resultTable