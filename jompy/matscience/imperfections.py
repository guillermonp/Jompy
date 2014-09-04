from jompy.constants.constants_si import k_boltzmann, k_boltzmann_ev
from jompy.functions.core import sigmoid
import math


class PointDefects(object):
    """

    """
    def __init__(self, unit='J'):
        """
        :param unit: J or eV
        """
        if unit == 'J':
            self.k = k_boltzmann.value
        elif unit == 'eV':
            self.k = k_boltzmann_ev.value
        else:
            raise TypeError('unit {0} is not accepted. '
                            'Units accepted: J and eV'.format(unit))

    def vacancies(self, n, q_v, t):
        """
        :param n: Number of lattice sites
        :param q_v: Activation energy - energy for vacancy formation
        :param t: Temperature (K)
        :return: number of vacancies
        """
        return n * math.exp(-q_v/(self.k * t))

    def vacant_probability(self, q_v, t):
        """
        Probability of finding site in vacant is given by
            P = sigmoid(-Qv/(kT))
        """
        return sigmoid(-q_v/(self.k * t))

    def frenkel_defect(self, n, q_v, t):
        """ Neighboring cation vacancy and cation interstitial """
        return n * math.exp(-q_v/(2*self.k * t))

    def schottky_defect(self):
        pass

    def exp_q_v(self):
        """
        Obtain activation energy experimental
        """
        pass

    @staticmethod
    def defect_concentration(n, n_v):
        """
        concentration = Nv/N
            N = number of lattice sites
            Nv = number of vacancies
        """
        return n_v/n

    def composition_by_mass(self):
        pass

    def composition_by_mole(self):
        pass