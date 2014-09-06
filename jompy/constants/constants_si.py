from .constant import Constant

"""SI base units: http://en.wikipedia.org/wiki/International_System_of_Units"""

k_boltzmann = Constant('Boltzmann constant', 1.3806488e-23, 'si', 'J/K', 'm^2*kg/(s^2*K)')
k_boltzmann_ev = Constant('Boltzmann constant', 8.6173324e-5, 'si', 'eV/K')

r_gas = Constant('Gas constant - ideal gas constant', 8.3144621, 'si', 'J/K')
n_avogrado = Constant("Avogrado's number", 6.02214129e23, 'si', '1/mol')