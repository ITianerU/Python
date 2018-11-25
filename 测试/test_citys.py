import unittest
from city_functions import cityCountryPopulation

class Test_city(unittest.TestCase):
    def test_city_country(self):
        result = cityCountryPopulation("北京", "中国")
        self.assertEqual("北京,中国", result)

    def test_city_country_population(self):
        result = cityCountryPopulation("北京", "中国", "40000000")
        self.assertEqual("北京,中国-人口40000000", result)