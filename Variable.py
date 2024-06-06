from Expression import Expression


class Variable(Expression):
    id: str

    def __init__(self, id:str):
        self.id = id

    def __str__(self):
        return self.id