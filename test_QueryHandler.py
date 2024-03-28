from QueryHandler import *

# def test_parser(path):

#     assert QueryHandler.parseInput(path) == expected_output[path]
5

# expected_output = {}
qh = QueryHandler()
print(qh.parseInput("query-samples/create.json"))
print(qh.parseInput("query-samples/insert.json"))
print(qh.parseInput("query-samples/select.json"))

print(qh.parseInput("query-samples/drop.json"))

