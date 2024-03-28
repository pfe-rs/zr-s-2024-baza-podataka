import pytest
from RowClass import *


red1=Row()
red2=Row()
red3=Row()
red4=Row()
red5=Row()
red6=Row()
red7=Row()
red8=Row()
red9=Row()


def test_addAttribute():
    row = Row()
    row.addAttribute("ime", "Petar")
    assert row.getAttribute("ime") == "Petar"

def test_checkAttribute():
    row = Row()
    with pytest.raises(TypeError):
        row.addAttribute(123, "Petar")

def test_thereIsAlreadyKey():
    row = Row()
    row.addAttribute("ime", "Petar")
    with pytest.raises(IndexError):
        row.addAttribute("ime", "Petar")

def test_deleteAttribute():
    row = Row()
    row.addAttribute("ime", "Petar")
    row.deleteAttribute("ime")
    assert row.getAttribute("ime") is None

def test_deleteAttributeAndInvalideKey():
    row = Row()
    with pytest.raises(TypeError):
        row.deleteAttribute(123)

def test_deleteAttributeAndThereIsNoKey():
    row = Row()
    with pytest.raises(IndexError):
        row.deleteAttribute("veranda")

def test_changeAttribute():
    row = Row()
    row.addAttribute("ime", "Petar")
    row.changeAttribute("ime", "Nemanja")
    assert row.getAttribute("ime") == "Nemanja"

def test_changeAtributeAndInvalideKey():
    row = Row()
    with pytest.raises(TypeError):
        row.changeAttribute(123, "Petar")

def test_changeAtributeAndNewKeyTOAdd():
    row = Row()
    row.changeAttribute("ime", "Nemanja")
    a = row.getAttribute("ime")
    assert row.getAttribute("ime") == "Nemanja"


test_addAttribute()
test_checkAttribute()
test_thereIsAlreadyKey()
test_deleteAttribute()
test_deleteAttributeAndInvalideKey()
test_deleteAttributeAndThereIsNoKey()
test_changeAttribute()
test_changeAtributeAndInvalideKey()
test_changeAtributeAndNewKeyTOAdd()
