from unittest import TestCase
from unittest.mock import patch, call

from controller import Controller


class ControllerTest(TestCase):

    @patch("controller.LongUnderlying")
    @patch("controller.PayoffPlotter")
    @patch("controller.PayOffCalculator", autospec=True)
    def test_initialization(self, calculator,
                            plotter,
                            longUnderlying):
        pass

    @patch("controller.PayoffPlotter", autospec=True)
    @patch("controller.PayOffCalculator", autospec=True)
    def test_get_strategy_payoff(self, calculator, plotter):
        pass

