import math


def sigmoid(z):
    return 1/(1 + math.exp(-z))


def n_comb_k(n, k):
    return math.factorial(n)/(math.factorial(k) * math.factorial(n - k))