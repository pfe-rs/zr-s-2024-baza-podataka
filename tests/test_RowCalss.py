import pytest
from src.RowClass import *

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


def test_toJSON():
    row = Row()
    row.changeAttribute("ime", "Nemanja")
    row.changeAttribute("prezime", "majski")
    row.changeAttribute("godiste", 2005)
    a = row.toJSON()
    assert row.toJSON() == '{"ime": "Nemanja", "prezime": "majski", "godiste": 2005}'



test_addAttribute()
test_checkAttribute()
test_thereIsAlreadyKey()
test_deleteAttribute()
test_deleteAttributeAndInvalideKey()
test_deleteAttributeAndThereIsNoKey()
test_changeAttribute()
test_changeAtributeAndInvalideKey()
test_changeAtributeAndNewKeyTOAdd()
test_toJSON()