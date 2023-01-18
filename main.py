#

class UniPoly:
    # Unipoly creates univariate polynomials with integer coefficients
    # Version 1

    def __init__(self, coefficient, indeterminate, exponent):
        # Create a UniPoly monomial.

        # Validate that the coefficients is an int.
        if not isinstance(coefficient, int):
            raise ValueError("The coefficient for a UniPoly must be an int.")
        
        # Validate that the exponent is a non-negative int.
        if not isinstance(exponent, int) or exponent < 0:
            raise ValueError("The exponent for a UniPoly must be a non-negative int.")

        # Validate that the indeterminate is an alphabetic string of length 1.
        if (not isinstance(indeterminate, str) or len(indeterminate) != 1 or not indeterminate[0].isalpha()):
            raise ValueError("The indeterminate for a UniPoly must be an alphabetic string of length 1.")
        
        self.coefficient = coefficient
        self.indeterminate = indeterminate
        self.exponent = exponent
    
    def __repr__(self):
        # Create the object representation of the polynomial
        return f"UniPoly({self.coefficient}, " + f"{repr(self.indeterminate)}, {self.exponent})"

    def __str__(self):
        # Create the displayable string form of the polynomial
        return f"{self.coefficient}*" + f"{self.indeterminate}**{self.exponent}"

    