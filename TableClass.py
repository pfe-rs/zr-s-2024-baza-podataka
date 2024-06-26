from RowClass import *
from LogicalExpressionClass import *

class Table:
    def __init__(self, name):
        self.mapRows = {}
        self.tableName = name
        self.maxId=0

    def getRow(self, rowId):
        if type(rowId)!=int:
            raise ValueError("Id needs to be an integer")
        
        if not (rowId in self.mapRows):
            raise IndexError("Requested id does not exist")

        return self.mapRows[rowId]

    def insertRow(self, row):
        if type(row) != Row:
            raise TypeError("Row value needs to be a row")

        if row.getAttribute("id") != None:
            if type(row.getAttribute("id")) != int:
                raise ValueError("Id needs to be an integer")

            id = row.getAttribute("id")
        else:
            id = self.maxId+1
        
        if id in self.mapRows:
            raise ValueError("The row with that id already exists")

        row.changeAttribute("id",id)

        if id > self.maxId:
            self.maxId = id 
        self.mapRows[id]=row
        return True

    def deleteRow(self, rowId):
        if type(rowId)!=int:
            raise ValueError("Id needs to be an integer")
        if not (rowId in self.mapRows):
            raise IndexError("Requested id does not exist")
        
        del self.mapRows[rowId]
        return True 
    
    def changeRow(self, rowId, newRow):
        if type(newRow) != Row:
            raise TypeError("Row value needs to be a row")
        
        if newRow.getAttribute("id") != None:
            raise ValueError("You cannot change id of a row")
        
        oldRow = self.getRow(rowId)
        
        for key, value in newRow.getDicitonary().items():
            oldRow.changeAttribute(key, value)
        return True
    
    def getName(self):
        return self.tableName
    
    def selectRows(self, logicalExpression):
        if type(logicalExpression) != LogicalExpression:
            raise TypeError("Logical expression needs to be of class logical expression")


        resultTable = Table("ResultTable")
        for key, value in self.mapRows.items():
            if logicalExpression.evaluate(value):
                resultTable.insertRow(value)

        return resultTable
    
    def updateRows(self, logicalExpression, newRow):
        toUpdate = self.selectRows(logicalExpression)
        row=Row()
        for row in toUpdate.mapRows.values():
            self.changeRow(row.getAttribute("id"), newRow)

    def deleteRows(self, logicalExpression):
        toDelete = self.selectRows(logicalExpression)

        for row in toDelete.mapRows.values():
            self.deleteRow(row.getAttribute("id"))

    def getAsDictionary(self):
        rowDict={}
        for key, value in self.mapRows.items():
            rowDict[key]=value.getDicitonary()
        finalDict={}
        finalDict[self.getName()]=rowDict
        return finalDict
    
    def toJSON(self):
        dict = self.getAsDictionary()
        return json.dumps(dict)
