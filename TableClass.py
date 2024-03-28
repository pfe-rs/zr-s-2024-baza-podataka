from RowClass import *
import numpy
from LogicalExpressionClass import *

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

        if row.getAttribute("id") != None:
            if type(row.getAttribute("id")) != int:
                raise ValueError("Id needs to be an integer")

            id = row.getAttribute("id")
        else:
            id = self.maxId+1
        
        if id in self.mapRows:
            raise ValueError("The row with that id already exists")

        row.changeAttribute("id",id)

        self.maxId = numpy.max(self.maxId, id)
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
        
        if newRow.getAttribute("id") != None:
            raise ValueError("You cannot change id of a row")
        
        oldRow = self.getRow(rowId)
        for key, value in newRow:
            oldRow.changeAttribute(key, value)
        return True
    
    def getName(self):
        return self.tableName
    
    def selectRows(self, logicalExpression):
        if type(logicalExpression) != LogicalExpression:
            raise TypeError("Logical expression needs to be of class logical expression")


        resultTable = Table("ResultTable")
        for key, value in self.mapRows:
            if logicalExpression.evaluate(value):
                resultTable[key] = value

        return resultTable
    
    def updateRows(self, logicalExpression, newRow):
        toUpdate = self.selectRows(logicalExpression)

        for key, _ in toUpdate:
            self.changeRow(key, newRow)

    def deleteRows(self, logicalExpression):
        toDelete = self.selectRows(logicalExpression)

        for key, _ in toDelete:
            self.deleteRow(key)        
