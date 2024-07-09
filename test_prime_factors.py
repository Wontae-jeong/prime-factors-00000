import unittest

from prime_factors import PrimeFactor


class PrimeTest(unittest.TestCase):
    def test_prime_factor_1(self):
        prime_factor = PrimeFactor()
        self.assertEqual([], prime_factor.of(1))
