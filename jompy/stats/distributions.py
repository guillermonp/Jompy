from jompy.functions import utils
from jompy.functions.core import gamma
import numpy as np
import math


class Weibull(object):
    def __init__(self, alpha, beta):
        self.a = alpha
        self.b = beta

    def pdf(self, x):
        """
        pdf computes the probability density at x for a Weilbull distribution
        with scale alpha and exponent beta
        """

        return (self.a / self.b) * (x / self.b) ** (self.a - 1) * math.exp(-(x/self.b) ** self.a)

    def cdf(self, x):
        """
        cdf computes the cumulative distribution function at x.
        """

        return 1 - math.exp(-(x / self.b) ** self.a)

    def failure_rate(self, x):
        """
        Failure rate or hazard function:
        Is the frequency with which a component fails, expressed, for example, in failures per hour.
        """

        return (self.a / self.b) * (x / self.b) ** (self.a - 1)

    def quantile(self, p):
        """
        The quantile function computes inverse cumulative distribution.
        """

        return self.b * (- math.log(1 - p)) ** (1 / self.a)

    def mean(self):
        """
        Mean of a Weibull random variable.
        """

        return self.b * gamma(1 + 1 / self.a)

    def variance(self):
        """
        Variance of a Weibull random variable.
        """

        return (self.b ** 2) * gamma(1 + 2 / self.a) - self.mean() ** 2

    def median(self):
        """
        Median of a Weibull random variable
        """

        return self.b * math.log(2) ** (1 / self.a)

    def std(self):
        """
        Standard deviation - self.variance
        """

        return math.sqrt(self.variance())

    def mode(self):
        if self.a > 1:
            return self.b * ((self.a - 1) / self.a) ** (1 / self.a)
        else:
            return 0

    def skewness(self):
        """
        Compute skewness: simplified expression from
        http://mathworld.wolfram.com/WeibullDistribution.html
        """

        ex1 = self.b ** 3 * gamma(1 + 3 / self.a)
        ex2 = 3 * self.mean() * self.variance() - self.mean() ** 3

        return (ex1 - ex2) / (self.variance() ** (3/2))

    def kurtosis(self):
        """
        Compute kurtosis:
        http://mathworld.wolfram.com/WeibullDistribution.html
        """
        n1 = -6 * gamma(1 + 1 / self.a) ** 4
        n2 = 12 * (gamma(1 + 1 / self.a) ** 2) * gamma(1 + 2 / self.a)
        n3 = 3 * gamma(1 + 2 / self.a) ** 2
        n4 = 4 * gamma(1 + 1 / self.a) * gamma(1 + 3 / self.a)
        n5 = gamma(1 + 4 / self.a)

        return (self.b ** 4) * (n1 + n2 - n3 - n4 + n5) / (self.variance() ** 2)


class WeibullAnalysis(Weibull):
    def __init__(self, data, alpha, beta):
        super().__init__(alpha, beta)

        self.data = data
        self.sample = []

        # check if input date is in ascending order
        self.initial_check()

    def initial_check(self):
        """
        Data must be in ascending order, otherwise modify input array 1D.
        """

        try:
            _data = np.asarray(self.data)
            if utils.is_sorted(_data):
                self.sample = _data
            else:
                self.sample = np.sort(_data)

        except Exception as err:
            print("incorrect input data, check format. {}".format(err.args[0]))

    def cfd(self):
        """
        Cumulative failure distribution
        """

        sample_size = len(self.sample)
        failure_rank = np.array([i + 1 for i in range(sample_size)])

        if sample_size < 100:
            return self.bernard_approx(failure_rank, sample_size)
        else:
            return self.mean_ranks(failure_rank, sample_size)

    @classmethod
    def bernard_approx(cls, rank, size):
        return (rank - 0.3)/(size + 0.4)

    @classmethod
    def mean_ranks(cls, rank, size):
        return rank / (size + 1)