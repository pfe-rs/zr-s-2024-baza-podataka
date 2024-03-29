from src.RowClass import *
from src.LogicalExpressionClass import *

class Table:
    def __init__(self, name):
        self.mapRows = {}
        self.tableName = name
        self.maxId=0

    @staticmethod
    def joinTwoTables(table1,table2,attribute):
        if type(table1) != Table:
            raise TypeError("Table 1 needs to be a table")
        if type(table2) != Table:
            raise TypeError("Table 2 needs to be a table")

        resultTable= Table("Result")
        
        for row1 in table1.mapRows.values():
            val1 = row1.getAttribute(attribute)
            if val1 == None:
                continue
            for row2 in table2.mapRows.values():
                val2 = row2.getAttribute(attribute)
                if val2 == None:
                    continue
                if val1 != val2:
                    continue

                dict1 = row1.getDictionary()
                dict2 = row2.getDictionary()
                del dict1["id"]
                del dict2["id"]

                newRow = Row()
                for key, value in dict1.items():
                    newRow.changeAttribute(key,value)
                for key, value in dict2.items():
                    newRow.changeAttribute(key,value)

                resultTable.insertRow(newRow)
        return resultTable

    @staticmethod
    def joinTables(tables,attributes):
        if len(tables)<=1:
            raise ValueError("You need to join at least 2 tables")
        if(len(attributes)+1!=len(tables)):
            raise ValueError("Therer needs to be 1 more joining attributes than tables")
        org = tables[0]
        for i in range(1,len(tables)):
            org=Table.joinTwoTables(org,tables[i],attributes[i-1])
        return org

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

        for key, value in newRow.getDictionary().items():
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
            rowDict[key]=value.getDictionary()
        return rowDict
    
    def toJSON(self):
        dict = self.getAsDictionary()
        return json.dumps(dict)
