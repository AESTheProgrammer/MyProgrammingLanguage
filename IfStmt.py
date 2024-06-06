from Expression import Expression
from Block import Block
from Statement import Statement


class IfStmt(Statement):
    condition: Expression
    then: Block

    def __init__(self, expr: Expression, block: Block):
        self.condition = expr
        self.then = block

    def __str__(self):
        return f"if ({self.condition})"
