from Statement import Statement


class VariableDeclaration(Statement):
    id: str
    type: str
    value: int

    def __init__(self, id:str, type:str, value:int):
        self.id = id
        self.type = type
        self.value = value

    def __str__(self):
        return f"{self.id}: {self.type} = {self.value}"