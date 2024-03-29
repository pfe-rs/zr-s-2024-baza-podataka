from src import QueryHandler

# def test_parser(path):

#     assert QueryHandler.parseInput(path) == expected_output[path]


## todo, napraviti da pytest radi ovde i takodje napraviti da se threaduje parseInput sa mutexima


qh = QueryHandler()
print(qh.parseInput("query-samples/create.json"))
print(qh.parseInput("query-samples/insert.json"))
print(qh.parseInput("query-samples/select.json"))
print(qh.parseInput("query-samples/insert.json"))
print(qh.parseInput("query-samples/delete.json"))
print(qh.parseInput("query-samples/update.json"))


print(qh.parseInput("query-samples/drop.json"))

