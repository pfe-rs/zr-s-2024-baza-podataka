import pytest
from LogicalExpressionClass import *

row = Row()
row.addAttribute("name","pera")
row.addAttribute("surname","peric")
row.addAttribute("age",20)
row.addAttribute("salary",100000)
row.addAttribute("hobby","watching birds")


def test_invalidOperator1():
    exp={"operation":"OR",
        "left":{"operation":">",
            "left":{"column":"age"},
            "right":{"constant":18}
        },
        "right":{"operation":"=",
            "left":{"column":"name"},
            "right":{"constant":"ime"}
        }}
    with pytest.raises(SyntaxError):
        a= LogicalExpression(exp)

def test_invalidOperator2():
    exp={"operation":"XOR",
        "left":{"operation":">",
            "left":{"column":"age"},
            "right":{"constant":18}
        },
        "right":{"operation":"==",
            "left":{"column":"name"},
            "right":{"constant":"ime"}
        }}
    with pytest.raises(SyntaxError):
        a= LogicalExpression(exp)

def test_invalidExpression1():
    exp={"operation":"OR",
        "left":{"operation":">",
            "left":{"column":"age"},
            "rigth":{"constant":18}
        },
        "right":{"operation":"==",
            "left":{"column":"name"},
            "right":{"constant":"ime"}
        }}
    with pytest.raises(SyntaxError):
        a= LogicalExpression(exp)

def test_invalidExpression2():
    exp={"operration":"OR",
        "left":{"operation":">",
            "left":{"column":"age"},
            "rigth":{"constant":18}
        },
        "right":{"operation":"==",
            "left":{"column":"name"},
            "rigth":{"constant":"ime"}
        }}
    with pytest.raises(SyntaxError):
        a= LogicalExpression(exp)

def test_singleExpression1():
    exp={"operation":"==",
            "left":{"column":"name"},
            "right":{"constant":"pera"}
        }
    a = LogicalExpression(exp)
    assert(a.evaluate(row)==True)

def test_singleExpression2():
    exp={"operation":">=",
            "left":{"column":"age"},
            "right":{"constant":20}
        }
    a = LogicalExpression(exp)
    assert(a.evaluate(row)==True)

def test_multiExpressionAnd1():
    exp={"operation":"AND",
            "left":{
                "operation":"==",
                "left":{"column":"surname"},
                "right":{"constant":"peric"}
                },
            "right":{"operation":"AND",
                "left":{
                    "operation":"<",
                    "left":{"column":"salary"},
                    "right":{"constant":100001}
                    },
                "right":{"operation":"AND",
                    "left":{
                        "operation":"<=",
                        "left":{"column":"age"},
                        "right":{"constant":20}
                        },
                    "right":{"operation":"AND",
                        "left":{
                            "operation":">",
                            "left":{"column":"age"},
                            "right":{"constant":19}
                            },
                        "right":{
                            "operation":">=",
                            "left":{"column":"salary"},
                            "right":{"constant":100000}
                        }
                    }
                }
            }
        }
    a=LogicalExpression(exp)
    assert(a.evaluate(row)==True)

def test_multiExpressionAnd2():
    exp={"operation":"AND",
        "left":{
            "operation":">",
            "left":{"column":"age"},
            "right":{"constant":20}
            },
        "right":{
            "operation":">",
            "left":{"column":"surname"},
            "right":{"constant":"aleksic"}
        }
    }
    a=LogicalExpression(exp)
    assert(a.evaluate(row)==False)

def test_multiExpressionOr1():
    exp={"operation":"OR",
            "left":{
                "operation":"==",
                "left":{"column":"hobby"},
                "right":{"constant":"watchingbirds"}
                },
            "right":{"operation":"OR",
                "left":{
                    "operation":">=",
                    "left":{"column":"salary"},
                    "right":{"constant":100001}
                    },
                "right":{"operation":"OR",
                    "left":{
                        "operation":"<=",
                        "left":{"column":"name"},
                        "right":{"constant":"Per"}
                        },
                    "right":{"operation":"OR",
                        "left":{
                            "operation":">",
                            "left":{"column":"age"},
                            "right":{"constant":21}
                            },
                        "right":{
                            "operation":">=",
                            "left":{"column":"salary"},
                            "right":{"constant":100001}
                        }
                    }
                }
            }
        }
    a=LogicalExpression(exp)
    assert(a.evaluate(row)==False)

def test_multiExpressionOr2():
    exp={"operation":"OR",
        "left":{
            "operation":"==",
            "left":{"column":"age"},
            "right":{"constant":19}
            },
        "right":{
            "operation":"<",
            "left":{"column":"surname"},
            "right":{"constant":"quebec"}
        }
    }
    a=LogicalExpression(exp)
    assert(a.evaluate(row)==True)

test_invalidOperator1()
test_invalidOperator2()
test_invalidExpression1()
test_invalidExpression2()
test_singleExpression1()
test_singleExpression2()
test_multiExpressionAnd1()
test_multiExpressionAnd2()
test_multiExpressionOr1()
test_multiExpressionOr2()