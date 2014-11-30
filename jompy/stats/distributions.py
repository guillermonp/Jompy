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

    def quantile(self):
        pass

    def mean(self):
        return self.b * gamma(1 + 1 / self.a)

    def median(self):
        return self.b * math.log(2) ** (1 / self.a)

    def variance(self):
        return (self.b ** 2) * gamma(1 + 2 / self.a) - self.mean() ** 2

    def mode(self):
        if self.a > 1:
            return self.b * ((self.a - 1) / self.a) ** (1 / self.a)
        else:
            return 0

    def skewness(self):
        ax_1 = gamma(1 + 3 / self.a) + 2 * (gamma(1 + 1 / self.a) ** 3)
        ax_2 = 3 * (gamma(1 + 2 / self.a) * gamma(1 + 1 / self.a))

        return (self.b ** 3) * (ax_1 - ax_2)

    def kurtosis(self):
        pass

    def kurtosis_excess(self):
        pass

    def ml(self):
        """ Maximum likelihood """
        pass


class WeibullAnalysis(Weibull):
    def __init__(self, data, alpha, beta):
        super().__init__(alpha, beta)

        self.data = data
        self.sample = []

        # check if input date is in ascending order
        self.initial_check()

    def initial_check(self):
        """
            data must be in ascending order
            array 1D
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
        """ Cumulative failure distribution """

        sample_size = len(self.sample)
        failure_rank = np.array([i + 1 for i in range(sample_size)])

        if sample_size < 100:
            return self.bernard_approx(failure_rank, sample_size)
        else:
            return self.mean_ranks(failure_rank, sample_size)

    def failure_rate(self):
        pass

    @classmethod
    def bernard_approx(cls, rank, size):
        return (rank - 0.3)/(size + 0.4)

    @classmethod
    def mean_ranks(cls, rank, size):
        return rank / (size + 1)