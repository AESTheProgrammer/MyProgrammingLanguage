from typing import List

from Expression import Expression


class FunctionCall(Expression):
    id: str
    arguments: List[Expression] = []

    def __init__(self, id: str, args: List[Expression] = None):
        self.id = id
        self.arguments = args

    def __str__(self):
        return f"{self.id}({', '.join(map(lambda x: str(x), self.arguments))})"
