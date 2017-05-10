from unittest import TestCase, skip
from unittest.mock import MagicMock, patch, call

from calculators.longputstrategy import LongPutStrategy
from model.optionleg import OptionLeg
from payoffcalculator import PayOffCalculator


class PayOffCalculatorTest(TestCase):

    def test_register_strategy(self):
        calc = PayOffCalculator()
        strategy = LongPutStrategy()

        calc.register_strategy(strategy)

        self.assertEqual(calc.strategy_map[strategy.STRATEGY_NAME],
                         strategy,
                         "The strategy must be registered in the strategy map")

    @patch("payoffcalculator.LongPutStrategy", autospec=True)
    @patch("payoffcalculator.LongCallStrategy", autospec=True)
    def test_calculate(self, longCallMock, longPutMock):
        pass
