import math
import cmath


def sigmoid(z):
    return 1/(1 + math.exp(-z))


def gamma(z):
    """
    Gamma function:

    Lanczos approximation implementation.e
    Numerical Recipes in C (2nd ed. Cambridge University Press 1992)
    """
    g = 5

    p0 = float(1.000000000190015)
    p1 = float(76.18009172947146)
    p2 = float(-86.50532032941677)
    p3 = float(24.01409824083091)
    p4 = float(-1.231739572450155)
    p5 = float(1.208650973866179e-3)
    p6 = float(-5.395239384953e-6)

    coefs = [p0, p1, p2, p3, p4, p5, p6]

    z = complex(z)
    if z.real < 0.5:
        #Recursion method: reflection formula
        return cmath.pi / (cmath.sin(cmath.pi * z) * gamma(1 - z))
    else:
        ax_1 = cmath.sqrt(cmath.pi * 2) / z
        ax2_sum = coefs[0]
        for i in range(1, g + 2):
            ax2_sum += coefs[i] / (z + i)
        t = z + g + 0.5
        ax_3 = (t ** (z + 0.5)) * cmath.exp(-t)
        return ((ax_1 * ax2_sum) * ax_3).real


# combinations and permutations
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def n_comb_k(n, k):
    return math.factorial(n)/(math.factorial(k) * math.factorial(n - k))