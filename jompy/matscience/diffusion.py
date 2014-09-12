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

    def diffusion_coef(self, d0, q_d, t):
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