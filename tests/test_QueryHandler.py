from src.QueryHandler import *
import os
# def test_parser(path):

#     assert QueryHandler.parseInput(path) == expected_output[path]


## todo, napraviti da pytest radi ovde i takodje napraviti da se threaduje parseInput sa mutexima


qh = QueryHandler()

print(qh.readInputFromFile(os.getcwd() + "/tests/query-samples/create.json"))
print(qh.readInputFromFile(os.getcwd() + "/tests/query-samples/insert.json"))
print(qh.readInputFromFile(os.getcwd() + "/tests/query-samples/select.json"))
print(qh.readInputFromFile(os.getcwd() + "/tests/query-samples/delete.json"))
print(qh.readInputFromFile(os.getcwd() + "/tests/query-samples/insert.json"))
print(qh.readInputFromFile(os.getcwd() + "/tests/query-samples/update.json"))
print(qh.readInputFromFile(os.getcwd() + "/tests/query-samples/drop.json"))



