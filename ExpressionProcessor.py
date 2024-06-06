from Block import Block
from Expression import Expression
from FunctionCall import FunctionCall
from FunctionDeclaration import FunctionDeclaration
from IfStmt import IfStmt
from LessThan import LessThan
from Multiplication import Multiplication
from Parenthesis import Parenthesis
from Subtraction import Subtraction
from Division import Division
from Addition import Addition
from Variable import Variable
from Number import Number
from VariableDeclaration import VariableDeclaration
from Statement import Statement

from typing import List, Dict, Union, Set

# possible value types supported in the language
valueTypes = Union[int]
execTypes = Union[Expression | Statement]


class ExpressionProcessor:
    li: [execTypes] = []
    values: List[Dict[str, valueTypes]] = [{}]  # Symbol Table
    funcs: Dict[str, FunctionDeclaration] = {}

    def __init__(self, li: [execTypes]):
        self.li = li

    def getEvalResult(self, e: execTypes):
        result = 0
        if isinstance(e, Number):
            # print("is instance of NUMBER")
            result = e.num
        elif isinstance(e, Parenthesis):
            # print("is instance of PARANTHESIS")
            result = self.getEvalResult(e.expr)
        elif isinstance(e, Variable):
            # print("is instance of VARIABLE")
            # print(self.values[-1])
            for symbolTable in self.values:
                if e.id in symbolTable:
                    result = symbolTable[e.id]
                    break
        elif isinstance(e, Multiplication):
            # print("is instance of MULTIPLICATION")
            left = self.getEvalResult(e.left)
            right = self.getEvalResult(e.right)
            result = left * right
        elif isinstance(e, Division):
            # print("is instance of DIVISION")
            left = self.getEvalResult(e.left)
            right = self.getEvalResult(e.right)
            result = left / right
        elif isinstance(e, Addition):
            # print("is instance of ADDITION")
            left = self.getEvalResult(e.left)
            right = self.getEvalResult(e.right)
            result = left + right
        elif isinstance(e, Subtraction):
            # print("is instance of SUBTRACTION")
            left = self.getEvalResult(e.left)
            right = self.getEvalResult(e.right)
            result = left - right
        elif isinstance(e, LessThan):
            # print("is instance of LESSTHAN")
            left = self.getEvalResult(e.left)
            right = self.getEvalResult(e.right)
            result = int(left < right)
        elif isinstance(e, FunctionCall):
            # print("is instance of FUNCTIONCALL")
            self.getEvalResult(self.funcs[e.id].block)
        elif isinstance(e, IfStmt):
            # print("is instance of IFSTMT")
            result = [str(e)]
            ifJump, ifThen = self.getEvalResult(e.condition), None
            if ifJump:
                # self.values.append(dict())
                result.extend(self.getEvalResult(e.then))
            else:
                result.append(str(e.then))
        elif isinstance(e, VariableDeclaration):
            # print("is instance of VARIABLEDECLARATION")
            self.values[-1][e.id] = e.value
            result = [str(e)]
        elif isinstance(e, FunctionDeclaration):
            # print("is instance of FUNCTIONDECLARATION")
            self.funcs[e.id] = e
            result = [str(e)]
        elif isinstance(e, Block):
            # print("is instance of BLOCK")
            self.values.append(dict())
            result = ["{"]
            for exp in e.expressions:
                if isinstance(exp, Statement):
                    evaluation = self.getEvalResult(exp)
                    result.extend(evaluation)
                elif isinstance(exp, Expression):
                    input = exp.__str__()
                    evaluation = self.getEvalResult(exp)
                    result.append(input + " is " + str(evaluation))
            result.append("}")
            self.values.pop()
        return result

    def getEvaluationResult(self):
        # print(self.li)
        evaluations = []
        for e in self.li:
            if isinstance(e, Statement):
                result = self.getEvalResult(e)
                evaluations.extend(result)
            elif isinstance(e, Expression):
                input = e.__str__()
                result = self.getEvalResult(e)
                evaluations.append(input + " is " + str(result))
        evaluations.append("def main()")
        result = self.getEvalResult(self.funcs['main'].block)
        evaluations.extend(result)
        return evaluations
