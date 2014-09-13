from jompy.constants.constants_si import r_gas
import math


class SDiffusion(object):
    """Steady-state diffusion """
    def __init__(self):
        self._R = r_gas

    def fick_1law(self, d, dc, dx):
        """
        Fick's first law states that the flux is proportional to the
        negative concentration gradient.
        D (diffusion coefficient) is the proportionality constant.
        """
        pass

    @staticmethod
    def fick_1law_linear(d, c2, c1, thick):
        """
        rate of diffusion independent of time

            Diffusion: [L^2 / time] (e.g. cm^2/s)
            Concentration: [M / L^3] (e.g. g/cm^3)
            Thick: (x2 - x1) [L] (e.g. cm)

        Flux in x-direction: cm^2/s * g/cm^3 * 1/cm = g/(cm^2 s)

        :param d: diffusion coefficient
        :param c2: concentration 2
        :param c1: concentration 1
        :param thick:
        """
        return - d * (c2 - c1) / thick

    def diffusion_coef(self, d0, q_d, t):
        """
        Effect of temperature to diffusion

        :param d0: Initial diffusion coefficient
        :param q_d: Activation energy (J)
        :param t: Absolute temperature (K)
        """
        return d0 * math.exp(-q_d / (self._R * t))


class NSDiffusion(object):
    """ Non-steady state diffusion"""
    def __init__(self):
        pass

    def fick_2law(self):
        pass


class DiffusionFactors(object):
    def __init__(self):
        pass