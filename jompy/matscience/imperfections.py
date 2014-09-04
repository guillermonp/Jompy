from jompy.constants.constants_si import k_boltzmann, k_boltzmann_ev
import math


class PointDefects(object):
    def __init__(self, unit='J'):
        """
        :param unit: J or eV
        :return:
        """
        if unit == 'J':
            self.k = k_boltzmann.value
        elif unit == 'eV':
            self.k = k_boltzmann_ev.value
        else:
            raise TypeError('unit {0} is not accepted. '
                            'Units accepted: J and eV'.format(unit))

    def vacancies(self, n, q, t):
        """
        :param n: Number of lattice sites
        :param q: Activation energy - energy for vacancy formation
        :param t: Temperature (K)
        :return: number of vacancies
        """
        return n * math.exp(-q/(self.k * t))

    def frenkel_defect(self, n, q, t):
        """
        Neighboring cation vacancy and cation interstitial
        :return:
        """
        return n * math.exp(-q/(2*self.k * t))

    def activation_energy(self):
        pass

    @staticmethod
    def defect_concentration(n, nv):
        """
        concentration = Nv/N
            N = number of lattice sites
            Nv = number of vacancies
        :return:
        """
        return nv/n

    def composition_by_mass(self):
        pass

    def composition_by_mole(self):
        pass