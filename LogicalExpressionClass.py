from RowClass import *

class LogicalExpression:
    validOperators=["OR","AND"]
    validComparators=["==",">=",">","<","<="]
    
    def __init__(self, value):
        if not self._checkValidity(value):
            raise SyntaxError("The expression syntax is invalid")
        self.expression = value
    
    @staticmethod
    def _evalRecursion(exp, row):
        operation = exp["operation"]
        if operation in LogicalExpression.validOperators:
            leftValue = LogicalExpression._evalRecursion(exp["left"],row)
            rightValue = LogicalExpression._evalRecursion(exp["right"],row)

            if operation == "OR":
                return leftValue or rightValue
            if operation == "AND":
                return leftValue and rightValue
            raise NotImplementedError("The operation '" + operation + "' is considered valid, but not implemented")
        
        if operation in LogicalExpression.validComparators:
            leftValue = row.getAttribute(exp["left"]["column"])
            rightValue = exp["rigth"]["constant"] 

            if operation == "==":
                return leftValue == rightValue
            if operation == ">":
                return leftValue > rightValue
            if operation == ">=":
                return leftValue >= rightValue
            if operation == "<":
                return leftValue < rightValue
            if operation == "<=":
                return leftValue <= rightValue
            
            raise NotImplementedError("The comparator '" + operation + "' is considered valid, but not implemented")

        raise Exception("The logical expression was evaluated as correct by check function, but evaluation function is unable to compute it correctly")

    def evalute(self, row):
        if type(row) != row:
            raise TypeError("Logical expressions need to be evaluated on rows")
        return LogicalExpression._evalRecursion(self.expression, row)

    @staticmethod
    def _checkValidity(value):
        if value == None:
            return False

        operation = value["operation"]

        if operation == None:
            return False
        
        if operation in LogicalExpression.validOperators:
            left = LogicalExpression._checkValidity(value["left"])
            right = LogicalExpression._checkValidity(value["left"])
            return left and right
        
        if operation in LogicalExpression.validComparators:
            left = value["left"]
            right = value["right"]
            
            if left == None or right==None:
                return False

            if not ("column" in left):
                return False
            try:
                Row.checkAttribute(left["column"])
            except:
                return False
            
            if not ("constant" in right):
                return False
            
            try:
                Row.checkValue(right["constant"])
            except:
                return False

            return True
        
        return False
    
