import unittest

from prime_factors import PrimeFactor


class PrimeTest(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.prime_factor = PrimeFactor()

    def test_prime_factor(self):
        tests = [
            {"target": 1, "expect": []},
            {"target": 2, "expect": [2]},
            {"target": 3, "expect": [3]},
            {"target": 4, "expect": [2, 2]},
            {"target": 9, "expect": [3, 3]},
            {"target": 12, "expect": [2, 2, 3]},
            {"target": 100, "expect": [2, 2, 5, 5]},
            {"target": 1000, "expect": [2, 2, 2, 5, 5, 5]},
            {"target": 23344342, "expect": [2, 7, 79, 21107]},
            {"target": 233443242, "expect": [2, 3, 3, 3, 4323023]},
            {"target": 2334432243, "expect": [3, 11, 13, 311, 17497]},
        ]
        for test in tests:
            with self.subTest(f"factor {test["target"]}"):
                self.assertEqual(test["expect"], self.prime_factor.of(test["target"]))
