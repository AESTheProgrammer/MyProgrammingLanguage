from Expression import Expression


class Number(Expression):
    num: int

    def __init__(self, num: int):
        self.num = num

    def __str__(self):
        return str(self.num)