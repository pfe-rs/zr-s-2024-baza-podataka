from src.QueryHandler import *
import os

queryHandler1 = QueryHandler()
queryHandler1


def test_ParseInputCreate():
    queryHandler1=QueryHandler()
    assert queryHandler1.parseInput("""
{
    "type":"create",
    "table":"students"
}
    """) == "addition True"

def test_ParseInputDrop():
    queryHandler1=QueryHandler()
    queryHandler1.parseInput("""
{
    "type":"create",
    "table":"students"
}
    """) 
    assert queryHandler1.parseInput('''{
    "type":"drop",
    "table":"students"
}''') == "drop True"

def test_ParseInputInsert():
    queryHandler1=QueryHandler()
    queryHandler1.parseInput("""
    {
        "type":"create",
        "table":"students"
    }
    """) 
    assert (queryHandler1.parseInput("""
    {
        "type":"insert",
        "table":"students",
        "row":{"name":"mika","last_name":"pera", "age": 22,"hobies":"pfe"}
    }
        """) ) == "insert True"

def test_ParseInputSelect():
    queryHandler1=QueryHandler()
    queryHandler1.parseInput("""
    {
        "type":"create",
        "table":"students"
    }
    """)
    queryHandler1.parseInput("""
    {
        "type":"insert",
        "table":"students",
        "row":{"name":"mika","last_name":"pera", "age": 22,"hobies":"pfe i tako to"}
    }
        """)
    #autput=json.loads(autput)
    assert queryHandler1.parseInput('''
    {   
        "type":"select",
        "columns":["name"],
        "table":"students",
        "where":{
            "operation":"OR",
                "left":{"operation":">",
                    "left":{"column":"age"},
                    "right":{"constant":18}
                },
                "right":{"operation":"==",
                    "left":{"column":"name"},
                    "right":{"constant":"mika"}
                }
        }
    }
        ''') == '{"1": {"name": "mika", "last_name": "pera", "age": 22, "hobies": "pfe i tako to", "id": 1}}'
def test_ParseInputDeleteIfThereIsNo():
    queryHandler1=QueryHandler()
    queryHandler1.parseInput("""
    {
        "type":"create",
        "table":"students"
    }
    """) 

    assert (queryHandler1.parseInput("""
    {
        "type":"delete",
        "table":"students",
        "where":{
                "operation":"==",
                    "left":{"column":"id"},
                    "right":{"constant":1}
                }
    }
        """) ) == "delete False"

def test_ParseInputDeleteIfThereIs():
    queryHandler1=QueryHandler()
    queryHandler1.parseInput("""
    {
        "type":"create",
        "table":"students"
    }
    """)
    queryHandler1.parseInput("""
    {
        "type":"insert",
        "table":"students",
        "row":{"name":"mika","last_name":"pera", "age": 22,"hobies":"pfe"}
    }
        """)
    assert (queryHandler1.parseInput("""
    {
        "type":"delete",
        "table":"students",
        "where":{
                "operation":"==",
                    "left":{"column":"id"},
                    "right":{"constant":1}
                }
    }
        """) ) == "delete True"

def test_ParseInputUpdateIfThereIs():
    queryHandler1=QueryHandler()
    queryHandler1.parseInput("""
    {
        "type":"create",
        "table":"students"
    }
    """) 
    queryHandler1.parseInput("""
    {
        "type":"insert",
        "table":"students",
        "row":{"name":"mika","last_name":"pera", "age": 22,"hobies":"pfe"}
    }
        """)
    assert queryHandler1.parseInput("""
    {
        "type":"update",
        "table":"students",
        "row":{"name":"djordje","last_name":"marjanovic", "age": 14},
        "where":{
        "operation":"OR",
            "left":{"operation":">",
                "left":{"column":"age"},
                "right":{"constant":10}
            },
            "right":{"operation":"==",
                "left":{"column":"name"},
                "right":{"constant":"mika"}
            }
    }
    }
        """) == "update True"



def test_ParseInputUpdateIfThereIsNo():
    queryHandler1=QueryHandler()
    queryHandler1.parseInput("""
    {
        "type":"create",
        "table":"students"
    }
    """) 
    queryHandler1.parseInput("""
    {
        "type":"insert",
        "table":"students",
        "row":{"name":"mika","last_name":"pera", "age": 22,"hobies":"pfe"}
    }
        """)
    assert queryHandler1.parseInput("""
    {
        "type":"update",
        "table":"students",
        "row":{"name":"djordje","last_name":"marjanovic", "age": 14},
        "where":{
        "operation":"OR",
            "left":{"operation":">",
                "left":{"column":"age"},
                "right":{"constant":10}
            },
            "right":{"operation":"==",
                "left":{"column":"name"},
                "right":{"constant":"lazar"}
            }
    }
    }
        """) == "update True"

def test_ParseInputJoin():
    queryHandler1=QueryHandler()
    queryHandler1.parseInput("""
    {
        "type":"create",
        "table":"students"
    }
    """) 
    queryHandler1.parseInput("""
    {
        "type":"insert",
        "table":"students",
        "row":{"ime":"Milica", "godine": 19}
    }
        """)
    queryHandler1.parseInput("""
    {
        "type":"insert",
        "table":"students",
        "row":{"ime":"Marince", "godine": 17}
    }
        """)
    queryHandler1.parseInput("""
    {
        "type":"insert",
        "table":"students",
        "row":{"ime":"Nemanja", "godine": 18}
    }
        """)
    


    queryHandler1.parseInput("""
    {
        "type":"create",
        "table":"studentsCity"
    }
    """) 

    queryHandler1.parseInput("""
    {
        "type":"insert",
        "table":"studentsCity",
        "row":{"ime":"Milica", "grad": "Loznica"}
    }
        """)
    queryHandler1.parseInput("""
    {
        "type":"insert",
        "table":"studentsCity",
        "row":{"ime":"Marince", "grad": "Nis"}
    }
        """)
    queryHandler1.parseInput("""
    {
        "type":"insert",
        "table":"studentsCity",
        "row":{"ime":"Nemanja", "grad": "Sombor"}
    }
        """)
    

    queryHandler1.parseInput("""
    {
        "type":"create",
        "table":"CityDesc"
    }
    """) 

    queryHandler1.parseInput("""
    {
        "type":"insert",
        "table":"CityDesc",
        "row":{"opis":"Zapad", "grad": "Loznica"}
    }
        """)
    queryHandler1.parseInput("""
    {
        "type":"insert",
        "table":"CityDesc",
        "row":{"opis":"Jug", "grad": "Nis"}
    }
        """)
    queryHandler1.parseInput("""
    {
        "type":"insert",
        "table":"CityDesc",
        "row":{"opis":"Sever", "grad": "Sombor"}
    }
        """)
    


    assert queryHandler1.parseInput('''
    {
        "type":"select",
        "table":"students",
        "join":{"table":"studentsCity", "field":"ime", "join":{"table":"CityDesc", "field":"grad"}},
        "where":"True"
    }
        ''') == '{"1": {"ime": "Milica", "godine": 19, "grad": "Loznica", "opis": "Zapad", "id": 1}, "2": {"ime": "Marince", "godine": 17, "grad": "Nis", "opis": "Jug", "id": 2}, "3": {"ime": "Nemanja", "godine": 18, "grad": "Sombor", "opis": "Sever", "id": 3}}'

test_ParseInputJoin()
test_ParseInputDrop()
test_ParseInputCreate()
test_ParseInputInsert()
test_ParseInputSelect()
test_ParseInputDeleteIfThereIsNo()
test_ParseInputDeleteIfThereIs()
test_ParseInputUpdateIfThereIs()



qh = QueryHandler()


'''
print(qh.readInputFromFile(os.getcwd() + "/tests/query-samples/create.json"))
print(qh.readInputFromFile(os.getcwd() + "/tests/query-samples/insert.json"))
print(qh.readInputFromFile(os.getcwd() + "/tests/query-samples/select.json"))

print(qh.readInputFromFile(os.getcwd() + "/tests/query-samples/create2.json"))
print(qh.readInputFromFile(os.getcwd() + "/tests/query-samples/insert2.json"))
print(qh.readInputFromFile(os.getcwd() + "/tests/query-samples/select-join.json"))


print(qh.readInputFromFile(os.getcwd() + "/tests/query-samples/delete.json"))
print(qh.readInputFromFile(os.getcwd() + "/tests/query-samples/insert.json"))
print(qh.readInputFromFile(os.getcwd() + "/tests/query-samples/update.json"))
print(qh.readInputFromFile(os.getcwd() + "/tests/query-samples/drop.json"))

'''

