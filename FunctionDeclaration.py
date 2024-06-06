from typing import List, Tuple

from Statement import Statement
from Block import Block


class FunctionDeclaration(Statement):
    block: Block
    id: str
    parameters: List[Tuple[str, str]]

    def __init__(self, funcId: str, block: Block, params: List[Tuple[str, str]]):
        self.id = funcId
        self.block = block
        self.parameters = params

    def __str__(self):
        return f"def {self.id}" \
               f" ({','.join([type + ' ' + name for type, name in self.parameters])})" \
               f"\n{self.block}\n"

    def getParamCount(self):
        return len(self.parameters)
