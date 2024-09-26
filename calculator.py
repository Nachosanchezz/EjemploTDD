class Calculator:
    def _init_(self):
        self.value = 0

    def add(self, x):
        self.value += x
        return self.value

    def subtract(self, x):
        self.value -= x
        return self.value

    def multiply(self, x):
        self.value *= x
        return self.value

    def divide(self, x):
        if x == 0:
            raise ValueError("Np se puede dividir por 0.")
        self.value /= x
        return self.value