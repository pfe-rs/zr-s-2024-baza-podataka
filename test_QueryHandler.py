from QueryHandler import *

# def test_parser(path):

#     assert QueryHandler.parseInput(path) == expected_output[path]


# expected_output = {}
qh = QueryHandler()
qh.parseInput("query-samples/create.json")
qh.parseInput("query-samples/insert.json")


