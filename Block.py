from typing import Union

from Expression import Expression
from Statement import Statement

execTypes = Union[Expression | Statement]


class Block(Statement):
    expressions: [execTypes]

    def __init__(self):
        self.expressions = []

    def add_expr(self, e: execTypes):
        self.expressions.append(e)

    def __str__(self):
        res = "{\n"
        for e in self.expressions:
            res += f'{e}\n'
        res += "}"
        return res
