import unittest

from tornado_app.handlers.monte_carlo_handler import monte_carlo_estimate


class TestMonteCarlo(unittest.TestCase):

    def test_monte_carlo(self):

        n = 10000000
        response = monte_carlo_estimate(n)

        self.assertAlmostEqual(float(response), 3.141, None, "", 0.001)
