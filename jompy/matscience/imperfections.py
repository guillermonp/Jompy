from jompy.constants.constants_si import k_boltzmann, k_boltzmann_ev, n_avogrado
from jompy.functions.core import sigmoid, n_comb_k
import math


class PointDefects(object):
    """
    Point defects disturbs the crystal pattern modifying the properties.
    Point defects can be classified between intrinsic and extrinsic defects.

    intrinsic defects:
        An intrinsic defect is formed when an atom is missing from a position
        that should be filled in the crystal, creating a vacancy, or when an
        atom occupies an interstitial site where no atom would ordinarily appear,
        causing an interstitialcy.

    extrinsic defects:
        The extrinsic defects are solutes or impurities depending if they were
        intentionally added to the material. We can distinguish between
        substitutional solute (impurity) or interstitial solute.
    """

    def __init__(self, unit='J'):
        """
        :param unit: J or eV
        """
        self.unit = unit

        if self.unit == 'J':
            self.k_b = k_boltzmann.value
        elif self.unit == 'eV':
            self.k_b = k_boltzmann_ev.value
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
        return n * math.exp(-q_v / (self.k_b * t))

    def equilibrium_concentration(self, q_v, t):
        """
        Ratio of vacant sites to occupied sites
            N = number of lattice sites
            Nv = number of vacancies

            Nv/N = exp(-Qv/(kT))
        """
        return math.exp(-q_v / (self.k_b * t))

    def vacant_probability(self, q_v, t):
        """
        Probability of finding site in vacant is given by
            P = sigmoid(-Qv/(kT))
        """
        return sigmoid(-q_v / (self.k_b * t))

    def frenkel_defect(self, n, q_v, t):
        """
        Frenkel defect:
            a neutral defect that is made up of a paired vacancy and interstitial.
            Neighboring cation vacancy and cation interstitial
        """
        return n * math.exp(-q_v / (2 * self.k_b * t))

    def schottky_defect(self, n, q_v, t):
        """
        Schottky defect:
            A neutral defect that involves paired vacancies on the cation
            an anion sublattices.
        """
        return n * math.exp(-q_v / (2 * self.k_b * t))

    @staticmethod
    def lattice_sites(density, molar_mass):
        """
        Number of lattice sites per volume

        :param density:  g/cm^3
        :param molar_mass: g/mol
        return: lattice sites / volume(cm^3, m^3..density unit)
        """
        return n_avogrado.value * density / molar_mass

    @staticmethod
    def w_vacancies(n, n_v):
        """
        Number of ways to arrange the vacancies

        :param n: total number of lattice sites
        :param n_v: number of vacancies
        """
        return n_comb_k(n, n_v)

    @staticmethod
    def w_interstitial(n, n_i):
        """
        Number of ways to arrange the interstitials

        :param n: total number of lattice sites
        :param n_i: number of interstitial sites
        """
        return n_comb_k(n, n_i)

    def w_configurations(self, n, n_v, n_i):
        """
        Total number of configurations:
            W = Wv * Wi
        This measure is utilizes to compute the entropy change.

        :param n: total number of lattice sites
        :param n_v: number of vacancies
        :param n_i: number of interstitial sites
        """
        return self.w_interstitial(n, n_i) * self.w_vacancies(n, n_v)

    def entropy_change(self, w):
        """
        delta(Sc) is the change in configurational entropy and is positive.
        Equilibrium concentration of defects is found by minimizing delta(G)

        delta(G) = n * delta(Gf) - T * delta(Sc)
            where:
            G = free energy
            Gf = energy per Frenkel defect pairs

        delta(Sc) = k ln(W)
            where W = w_configurations()
        """
        return self.k_b * math.log(w)

    def gibbs_free_energy(self, n, n_v, q_v):
        """
        Enthalpy change for the formation of a single defect is
        the activation energy (Qv) therefore for generate n defects
        the change is n * Qv. Thus, Gibbs free energy:
            delta(G) = n * Qv - 2 * k * ln(W)

            where we are assuming that n_i = n_v
            (number of interstitial sites = number of vacancies)
        """
        return n_v * q_v - 2 * self.w_vacancies(n, n_v)

    def __repr__(self):
        return 'Point defects, unit={0}'.format(self.unit)


def comp_by_mass(m_a, m_b):
    """
    Weight percent

    :param m_a: mass of component A
    :param m_b: mass of component B
    """
    total_weight = m_a + m_b
    comp_a = m_a / total_weight * 100
    comp_b = m_b / total_weight * 100

    return [comp_a, comp_b]


def comp_by_mole(n_a, n_b):
    """
    Atomic percent

    :param n_a: number of moles of component A
    :param n_b: number of moles of component B
    """
    total_moles = n_a + n_b
    comp_a = n_a / total_moles * 100
    comp_b = n_b / total_moles * 100

    return [comp_a, comp_b]


def number_moles(mass, atomic_mass):
    """
    Number of moles of a determined mass of a hypothetical element.

    :param mass: mass (g)
    :param atomic_mass: atomic mass (e.g. C (carbon) = 12.011)
    """
    return mass / atomic_mass