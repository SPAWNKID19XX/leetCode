class Calculator():
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b

    def sum(self, a, b):
        return a + b
    #
    def mult(self, a, b):
        return a * b
    #
    def div(self, a, b):
        if b != 0:
            return a / b
        raise ValueError("Div by zero error")
    #
    def minus(self, a, b):
        return a - b


