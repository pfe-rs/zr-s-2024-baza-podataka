import pytest
from RowClass import *
from TableClass import *
from LogicalExpressionClass import *


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
'''
def test_selectRows():
    testTabela=MakeTestTable()

    expression={"operation":">",
            "left":{"column":"godine"},
            "rigth":{"value":25}
        }

    uslov = LogicalExpression(expression)
    uslovljenaTabela = testTabela.selectRows(uslov)
    assert len(uslovljenaTabela.mapRows) == 0

def test_updateRows():
    testTabela=MakeTestTable()
    uslov = LogicalExpression("godine", ">", 25)
    promena = {"ime": "Zare", "godine": 60}
    testTabela.updateRows(uslov, promena)
    assert testTabela.getRow(1)["ime"] == "Milica"
    assert testTabela.getRow(2)["ime"] == "Zare"
    assert testTabela.getRow(3)["ime"] == "Nemanja"

def test_deleteRows():
    testTabela=MakeTestTable()
    uslov = LogicalExpression("godine", ">", 25)
    testTabela.deleteRows(uslov)
    assert len(testTabela.mapRows) == 1
'''

test_getRow()
test_deleteRow()
test_insertRow()
test_changeRow()
#test_selectRows()
#test_updateRows()
#test_deleteRows()