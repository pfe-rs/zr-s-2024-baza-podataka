import pytest
from src.RowClass import *
from src.TableClass import *
from src.LogicalExpressionClass import *


def MakeTestTable():
    table = Table("Test")
    r1=Row()
    r2=Row()
    r3=Row()
    r1.addAttribute("id",1)
    r1.addAttribute("ime","Milica")
    r1.addAttribute("godine",19)
    r2.addAttribute("id",2)
    r2.addAttribute("ime","Marince")
    r2.addAttribute("godine",17)
    r3.addAttribute("id",3)
    r3.addAttribute("ime","Nemanja")
    r3.addAttribute("godine",18)

    table.insertRow(r1)
    table.insertRow(r2)
    table.insertRow(r3)

    return table

def MakeSecondTestTable():
    table = Table("Test2")
    r1=Row()
    r2=Row()
    r3=Row()
    r1.addAttribute("id",1)
    r1.addAttribute("ime","Milica")
    r1.addAttribute("grad","Loznica")
    r2.addAttribute("id",2)
    r2.addAttribute("ime","Marince")
    r2.addAttribute("grad", "Nis")
    r3.addAttribute("id",3)
    r3.addAttribute("ime","Nemanja")
    r3.addAttribute("grad","Sombor")

    table.insertRow(r1)
    table.insertRow(r2)
    table.insertRow(r3)

    return table

def MakeThirdTestTable():
    table = Table("Test2")
    r1=Row()
    r2=Row()
    r3=Row()
    r1.addAttribute("id",1)
    r1.addAttribute("opis","Zapad")
    r1.addAttribute("grad","Loznica")
    r2.addAttribute("id",2)
    r2.addAttribute("opis","Jug")
    r2.addAttribute("grad", "Nis")
    r3.addAttribute("id",3)
    r3.addAttribute("opis","Sever")
    r3.addAttribute("grad","Sombor")
    table.insertRow(r1)
    table.insertRow(r2)
    table.insertRow(r3)

    return table




def test_getRow():
    testTabela=MakeTestTable()
    r123=Row()
    r123=testTabela.getRow(1)
    assert r123._dictionary == {"id": 1, "ime": "Milica", "godine": 19}

def test_deleteRow():
    testTabela=MakeTestTable()
    testTabela.deleteRow(1)
    with pytest.raises(IndexError):
        testTabela.getRow(1)

def test_insertRow():
    testTabela=MakeTestTable()
    r4=Row()
    r4.addAttribute("id",4)
    r4.addAttribute("ime","Paja")
    r4.addAttribute("godine",40)

    testTabela.insertRow(r4)
    assert testTabela.getRow(4).getAttribute("ime") == "Paja"

def test_changeRow():
    testTabela=MakeTestTable()
    promena=Row()
    promena.addAttribute("ime", "Milutin")
    promena.addAttribute("godine", 86)
    testTabela.changeRow(2, promena)

    assert testTabela.getRow(2).getAttribute("ime") == "Milutin"
    assert testTabela.getRow(2).getAttribute("godine") == 86

def test_selectRows():
    testTabela=MakeTestTable()

    expression={"operation":">",
            "left":{"column":"godine"},
            "right":{"constant":25}
        }

    uslov = LogicalExpression(expression)
    uslovljenaTabela = testTabela.selectRows(uslov)
    assert len(uslovljenaTabela.mapRows) == 0

def test_updateRows():
    testTabela=MakeTestTable()
    expression={"operation":">",
            "left":{"column":"godine"},
            "right":{"constant":18}
        }
    uslov = LogicalExpression(expression)
    promena=Row()
    promena.addAttribute("ime", "Milutin")
    promena.addAttribute("godine", 86)
    testTabela.updateRows(uslov, promena)
    assert testTabela.getRow(1).getAttribute("ime") == "Milutin"
    assert testTabela.getRow(2).getAttribute("ime") == "Marince"
    assert testTabela.getRow(3).getAttribute("ime") == "Nemanja"

def test_deleteRows():
    testTabela=MakeTestTable()
    expression={"operation":">",
            "left":{"column":"godine"},
            "right":{"constant":25}
        }
    uslov = LogicalExpression(expression)
    testTabela.deleteRows(uslov)
    assert len(testTabela.mapRows) == 3

def test_toJSON():
    testTabela=MakeTestTable()
    a = testTabela.toJSON()

def test_joinTwoTables():
    table1=MakeTestTable()
    table2=MakeSecondTestTable()
    resultTable=Table.joinTwoTables(table1, table2, "ime")

    assert len(resultTable.getAsDictionary()) == 3  
    assert resultTable.getRow(1).getAttribute("ime") == "Milica"
    assert resultTable.getRow(1).getAttribute("godine") == 19
    assert resultTable.getRow(1).getAttribute("grad") == "Loznica"
    assert resultTable.getRow(2).getAttribute("ime") == "Marince"
    assert resultTable.getRow(2).getAttribute("godine") == 17
    assert resultTable.getRow(2).getAttribute("grad") == "Nis"
    assert resultTable.getRow(3).getAttribute("ime") == "Nemanja"
    assert resultTable.getRow(3).getAttribute("godine") == 18
    assert resultTable.getRow(3).getAttribute("grad") == "Sombor"

def test_joinThreetables():
    table1=MakeTestTable()
    table2=MakeSecondTestTable()
    table3=MakeThirdTestTable()

    tables=[table1,table2,table3]
    attributes=["ime","grad"]
    resultTable=Table.joinTables(tables, attributes)

    assert len(resultTable.getAsDictionary()) == 3  
    assert resultTable.getRow(1).getAttribute("ime") == "Milica"
    assert resultTable.getRow(1).getAttribute("godine") == 19
    assert resultTable.getRow(1).getAttribute("grad") == "Loznica"
    assert resultTable.getRow(1).getAttribute("opis") == "Zapad"
    assert resultTable.getRow(2).getAttribute("ime") == "Marince"
    assert resultTable.getRow(2).getAttribute("godine") == 17
    assert resultTable.getRow(2).getAttribute("grad") == "Nis"
    assert resultTable.getRow(2).getAttribute("opis") == "Jug"
    assert resultTable.getRow(3).getAttribute("ime") == "Nemanja"
    assert resultTable.getRow(3).getAttribute("godine") == 18
    assert resultTable.getRow(3).getAttribute("grad") == "Sombor"
    assert resultTable.getRow(3).getAttribute("opis") == "Sever"

def test_joinTwoTablesButNoAttributeInBouth():
    table1=MakeTestTable()
    table2=MakeThirdTestTable()
    resultTable=Table.joinTwoTables(table1, table2, "ime")
    rez=Table("Result")
    assert len(resultTable.getAsDictionary()) == 0






test_toJSON()
test_getRow()
test_deleteRow()
test_insertRow()
test_changeRow()
test_selectRows()
test_updateRows()
test_deleteRows()
test_joinTwoTables()
test_joinThreetables()
test_joinTwoTablesButNoAttributeInBouth()