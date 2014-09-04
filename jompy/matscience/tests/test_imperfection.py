from jompy.matscience.imperfections import PointDefects

defects = PointDefects('eV')
vacancies = defects.vacancies(n=8e28, q=0.9, t=1273)
defect_ratio = defects.defect_concentration(n=8e28, nv=vacancies)