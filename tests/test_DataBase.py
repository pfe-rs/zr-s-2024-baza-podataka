from src.DataBaseClass import *
import pytest

def MakeTestDataBase():
    testBase=DataBase()
    return testBase


def test_createTable():
    testBase=MakeTestDataBase()
    testBase.createTable("test")
    assert "test" in testBase._mapTables

def test_createTableAndTableAlreadyExist():
    testBase=MakeTestDataBase()
    testBase.createTable("test")
    with pytest.raises(IndexError):
        testBase.createTable("test")

def test_dropTable():
    testBase=MakeTestDataBase()
    testBase.createTable("test")
    testBase.dropTable("test")
    assert "test" not in testBase._mapTables

def test_dropTableAndThereIsNoTable():
    testBase=MakeTestDataBase()
    with pytest.raises(IndexError):
        testBase.dropTable("test")

def test_getTable():
    testBase=MakeTestDataBase()
    testBase.createTable("test")
    table = testBase.getTable("test")
    assert table is not None

def test_getTableIfThereIsNot():
    testBase=MakeTestDataBase()
    with pytest.raises(IndexError):
        testBase.getTable("test")

def test_saveDataBase():
    testBase=MakeTestDataBase()
    testBase.createTable("test")
    testBase.saveDataBase("test.json")
    # db.saveDataBase(path)




test_createTable()
test_createTableAndTableAlreadyExist()
test_dropTable()
test_dropTableAndThereIsNoTable()
test_getTable()
test_getTableIfThereIsNot()
test_saveDataBase()