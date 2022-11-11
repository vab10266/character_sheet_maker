class Cell(object):
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr
    
    def copy(self):
        return Cell(self.name, self.expr)


