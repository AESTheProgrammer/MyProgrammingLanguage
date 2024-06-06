from Expression import Expression


class LessThan(Expression):
    left: Expression
    right: Expression

    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.left} < {self.right}"
