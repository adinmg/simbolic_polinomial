#

class UniPoly:
    # Unipoly creates univariate polynomials with integer coefficients
    # Version 3

    def __init__(self, coefficient=1, indeterminate='x', exponent=0):
        # Create a UniPoly monomial.

        # Create a UniPoly object from an integer coefficient, string indeterminate, and 
        # non-negative integer exponent

        # Validate that the coefficients is an int.
        if not isinstance(coefficient, int):
            raise ValueError("The coefficient for a UniPoly must be an int.")
        
        # Validate that the exponent is a non-negative int.
        if not isinstance(exponent, int) or exponent < 0:
            raise ValueError("The exponent for a UniPoly must be a non-negative int.")

        # Validate that the indeterminate is an alphabetic string of length 1.
        if (not isinstance(indeterminate, str) or len(indeterminate) != 1 or not indeterminate[0].isalpha()):
            raise ValueError("The indeterminate for a UniPoly must be an alphabetic string of length 1.")
        
        # The 'variable' for the polynomial.
        self.indeterminate = indeterminate

        # The terms in the polynomial. Each key is an int exponent and each value is the int coefficient.
        if coefficient != 0:
            self.terms = {exponent: coefficient}
        else:
            self.terms = dict()
    
    def __neg__(self):
        # Negate the polynomial term-wise unless its is already 0.
        if not self.terms:
            return self
        
        new_poly = UniPoly(0, self.indeterminate)
        for exponent in self.terms:
            new_poly.terms[exponent] = -self.terms[exponent]

        return new_poly

    def __repr__(self):
        # Create the object representation of the polynomial
        return str(self)

    def __str__(self):
        # Do a very rough and incomplete conversion to str.

        if not self.terms:
            return '0'
        
        print_terms = [
                f"{self.terms[exponent]}*{self.indeterminate}**{exponent}"
                for exponent in sorted(self.terms, reverse=True)
                ]
        
        return " + ".join(print_terms)

