from jompy.matscience.imperfections import (PointDefects, comp_by_mass, Grain)

defects = PointDefects('eV')

# Number of vacancies and vacancy concentration
vacancies = defects.vacancies(n=8e28, q_v=0.9, t=1273)
edc = defects.equilibrium_concentration(q_v=0.9, t=1293)
prob = defects.vacant_probability(q_v=0.9, t=1273)

print('vacancies = {0} \n'
      'equilibrium concentration of defects = {1:.4%} \n'
      'Probability of finding site in vacant = {2:.4%}'.
      format(vacancies, edc, prob))

# Number of Frenkel defects per cubic meter in zinc oxide at 1000ºC.
# Activation energy = 2.51 eV, density for ZnO = 5.55 g/cm3 at that temperature.
lattice_sites_volume = defects.lattice_sites(density=5.55, molar_mass=81.41)
# lattice sites per cubic meter
l_sites_m3 = lattice_sites_volume * 1e6
frenkel_defects = defects.frenkel_defect(n=l_sites_m3, q_v=2.51, t=1273)

print("frenkel defects = ", frenkel_defects)


# composition / concentration
total_comp = comp_by_mass(m_a=4, m_b=5)
print(total_comp)


# Grain size determination
grain_avg = Grain.grain_average(g_size=6)
grain_size = Grain.grain_size_number(g_avg=45)
grain_avg_magnification = Grain.magnification_avg(factor=85, g_size=6.5)
grain_size_magnification = Grain.magnification_size(factor=85, g_avg=62.6)

print(grain_avg, grain_size)
print(grain_avg_magnification, grain_size_magnification)