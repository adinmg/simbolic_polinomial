#

class UniPoly:
    def __init__(self, coefficient, indeterminate, exponent):
        self.coefficient = coefficient
        self.indeterminate = indeterminate
        self.exponent = exponent
    
    def __str__(self):
        return f"{self.coefficient}*{self.indeterminate}**{self.exponent}"
