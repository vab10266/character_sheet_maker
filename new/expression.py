import random


class Expression(object):
    def evaluate(self, ctx):
        raise NotImplementedError

    def describe(self):
        raise NotImplementedError

    def __add__(self, oth):
        return Sum(self, oth)

    def __sub__(self, oth):
        return Diff(self, oth)

    def __mul__(self, oth):
        return Prod(self, oth)
    
    def __floordiv__(self, oth):
        return IDiv(self, oth)


class CellRef(Expression):
    def __init__(self, cell):
        self.cell = cell

    def evaluate(self, ctx):
        return ctx[self.cell].expr.evaluate(ctx)

    def describe(self):
        return self.cell


class BinOp(Expression):
    def __init__(self, expr1, expr2, op, op_rep):
        self.expr1 = expr1
        self.expr2 = expr2
        self.op = op
        self.op_rep = op_rep

    def evaluate(self, ctx):
        return self.op(self.expr1.evaluate(ctx), self.expr2.evaluate(ctx))

    def describe(self):
        return f'({self.expr1.describe()} {self.op_rep} {self.expr2.describe()})'


class Sum(BinOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, (lambda a, b: a + b), '+')


class Diff(BinOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, (lambda a, b: a - b), '-')


class Prod(BinOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, (lambda a, b: a * b), '*')


class Max(BinOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, (lambda a, b: max(a, b)), 'max')


class Min(BinOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, (lambda a, b: min(a, b)), 'min')


class IDiv(BinOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, (lambda a, b: a // b), '//')


class DiceThrow(Expression):
    def __init__(self, num_throws, num_sides):
        self.num_throws = num_throws
        self.num_sides = num_sides

    def evaluate(self, ctx):
        return sum(
            random.randint(1, self.num_sides.evaluate(ctx))
            for _
            in range(self.num_throws.evaluate(ctx)))

    def describe(self):
        return f'{self.num_throws.describe()}d{self.num_sides.describe()}'


class Int(Expression):
    def __init__(self, value):
        self.value = value

    def evaluate(self, _):
        return self.value

    def describe(self):
        return f'{self.value}'

class String(Expression):
    def __init__(self, value):
        self.value = value

    def evaluate(self, _):
        return self.value

    def describe(self):
        return f'{repr(self.value)}'


if __name__ == '__main__':
    one = Int(1)
    six = Int(6)
    four = Int(4)
    expr = DiceThrow(one, six) + DiceThrow(one, four)
    print(expr.describe())
    print(expr.evaluate({}))
