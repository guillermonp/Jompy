from jompy.constants.constants_si import r_gas, r_gas_ev
import math


class Fick1(object):
    """Steady-state diffusion """

    def __init__(self, d, c2, c1, thick):
        """
        rate of diffusion independent of time

            Diffusion: [L^2 / time] (e.g. cm^2/s)
            Concentration: [M / L^3] (e.g. g/cm^3)
            Thick: (x2 - x1) [L] (e.g. cm)
            Flux: [M / (L^2 times)]

        Flux in x-direction: cm^2/s * g/cm^3 * 1/cm = g/(cm^2 s)

        :param d: diffusion coefficient
        :param c2: concentration 2
        :param c1: concentration 1
        :param thick:
        """
        self._C1 = c1
        self._C2 = c2
        self._D = d
        self._thick = thick

    def flux(self):
        return - self._D * (self._C2 - self._C1) / self._thick

    @property
    def diffusivity(self):
        return self._D

    @property
    def concentration_1(self):
        return self._C1

    @property
    def concentration_2(self):
        return self._C2

    @property
    def thick_dx(self):
        return self._thick


class Fick2(object):
    """ Non-steady state diffusion"""

    def __init__(self):
        pass


class DiffusionFactors(object):
    def __init__(self, unit='J'):
        self.unit = unit

        if self.unit == 'J':
            self._R = r_gas.value
        elif self.unit == 'eV':
            self._R = r_gas_ev.value
        else:
            raise TypeError('unit {0} is not accepted. '
                            'Units accepted: J and eV'.format(unit))

    def diffusion_coef(self, d0, q_d, t):
        """
        Effect of temperature to diffusion

        :param d0: Initial diffusion coefficient
        :param q_d: Activation energy (J)
        :param t: Absolute temperature (K)
        """
        return d0 * math.exp(-q_d / (self._R * t))

    def arrhenius(self, d, temp):
        """
        ln D = ln D0 - Qd/R * (1/T)
        :param d:
        :param temp: array of temperatures
        :return:
        """
        pass