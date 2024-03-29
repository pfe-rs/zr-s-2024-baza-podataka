from src.QueryHandler import *

handler = QueryHandler()
handler.parseInput("""
    {
    "type":"create",
    "table":"polaznici"
    }
""")

handler.parseInput("""
    {
    "type":"insert",
    "table":"polaznici",
    "row":{"ime":"Milica", "godine": 19}
    }
""")

changeEven="""
    {
    "type":"update",    
    "table":"polaznici",
    "row":{"godine": 19},
    "where":{
        "operation":"==",
        "left":{"column":"godine"},
        "right":{"constant":18}
    }}
    """
changeOdd="""
    {
    "type":"update",    
    "table":"polaznici",
    "row":{"godine": 19},
    "where":{
        "operation":"==",
        "left":{"column":"godine"},
        "right":{"constant":18}
    }}
    """

def funk(sta):
    if sta % 2 == 0:
        handler.parseInput(changeEven)
        handler.parseInput(changeOdd)
        handler.parseInput(changeEven)
        handler.parseInput(changeOdd)
    if sta % 2 == 1:
        handler.parseInput(changeOdd)
        handler.parseInput(changeEven)
        handler.parseInput(changeOdd)
        handler.parseInput(changeEven)

threads= []
for i in range(1000):
    t = threading.Thread(target=funk,args=[i])
    threads.append(t)

for x in threads:
    x.start()
for x in threads:
    x.join()


