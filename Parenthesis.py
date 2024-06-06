from Expression import Expression


class Parenthesis(Expression):
    expr: Expression = None

    def __init__(self, expr: Expression):
        self.expr = expr

    def __str__(self):
        return f"({self.expr})"
