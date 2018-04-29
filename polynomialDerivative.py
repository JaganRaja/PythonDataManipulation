import numpy as np
import matplotlib.pyplot as plt


class Polynomial:

    def __init__(self, *coefficients):
        """ input: coefficients are in the form a_n, ...a_1, a_0 
        """
        # for reasons of efficiency we save the coefficients in reverse order,
        # i.e. a_0, a_1, ... a_n
        self.coefficients = coefficients[::-1] # tuple is also turned into list

    # method to return the canonical string representation of a polynomial
    def __repr__(self):
        return "Polynomial" + str(self.coefficients)

    def __call__(self, x):    
        res = 0
        for index, coeff in enumerate(self.coefficients):
            res += coeff * x** index
        return res 


    def degree(self):
        return len(self.coefficients)
    

    @staticmethod
    def zip_longest(iter1, iter2, fillchar=None):    
        for i in range(max(len(iter1), len(iter2))):
            if i >= len(iter1):
                yield (fillchar, iter2[i])
            elif i >= len(iter2):
                yield (iter1[i], fillchar)
            else:
                yield (iter1[i], iter2[i])
            i += 1   
    

    def __add__(self, other):
        c1 = self.coefficients
        c2 = other.coefficients
        res = [sum(t) for t in Polynomial.zip_longest(c1, c2)]
        return Polynomial(*res)

    def __sub__(self, other):
        c1 = self.coefficients
        c2 = other.coefficients

        res = [t1-t2 for t1, t2 in Polynomial.zip_longest(c1, c2)]
        return Polynomial(*res)

    def derivative(self):
        derived_coeffs = []
        exponent = 1
        for i in range(1, len(self.coefficients)):
            derived_coeffs.append(self.coefficients[i] * exponent)
            exponent += 1
        return Polynomial(*derived_coeffs)

    def __str__(self):
        res = ""
        for i in range(len(self.coefficients)-1, -1, -1):
            res +=  str(self.coefficients[i]) + "x^" + str(i) + " + "
        if res.endswith(" + "):
            res = res[:-3]
        return res

p = Polynomial(-0.8, 2.3, 0.5, 1, 0.2)

p_der = p.derivative()

X = np.linspace(-2, 3, 50, endpoint=True)

F = p(X)
F_derivative = p_der(X)
plt.plot(X, F, label="F")
plt.plot(X, F_derivative, label="F_der")

plt.legend()
plt.show()