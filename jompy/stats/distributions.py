import numpy as np
from jompy.functions import utils


class Weibull(object):
    def __init__(self, data, alpha, beta):
        self.a = alpha
        self.b = beta
        self.data = data
        self.sample = []

        # check
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

    def pdf(self):
        pass

    def cdf(self):
        pass

    def quantile(self):
        pass

    def mean(self):
        pass

    def median(self):
        pass

    def mode(self):
        pass

    def variance(self):
        pass

    def skewness(self):
        pass

    def kurtosis(self):
        pass

    def failure_rate(self):
        pass

    def ml(self):
        """ Maximum likelihood """
        pass

    def cfd(self):
        """ Cumulative failure distribution """
        sample_size = len(self.sample)
        failure_rank = np.array([i + 1 for i in range(sample_size)])
        if sample_size < 100:
            return self.bernard_approx(failure_rank, sample_size)
        else:
            return self.mean_ranks(failure_rank, sample_size)

    @staticmethod
    def bernard_approx(rank, size):
        return (rank - 0.3)/(size + 0.4)

    @staticmethod
    def mean_ranks(rank, size):
        return rank / (size + 1)