from jompy.matscience.imperfections import PointDefects,  Grain
import unittest


class TestVacancies(unittest.TestCase):
    def setUp(self):
        self.defects = PointDefects('eV')

    def test_unit(self):
        self.assertEqual(self.defects.units, 'eV')

    def test_vacancies(self):
        vacancies = self.defects.vacancies(n=8e28, q_v=0.9, t=1273)
        self.assertTrue(vacancies > 2.1878e25)

    def test_equilibrium_concentration(self):
        edc = self.defects.equilibrium_concentration(q_v=0.9, t=1293)
        self.assertAlmostEquals(edc, 0.00031047)

    def test_vacant_prob(self):
        prob = self.defects.vacant_probability(q_v=0.9, t=1273)
        self.assertAlmostEquals(prob, 0.0002734)


class TestGrain(unittest.TestCase):
    def setUp(self):
        self.grain = Grain()

    def test_grain_avg(self):
        pass

    def test_grain_size(self):
        pass

if __name__ == "__main__":
    TestVacancies()
    TestGrain()