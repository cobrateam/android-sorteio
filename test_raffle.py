import unittest
import mocker
from nose.tools import assert_equals

class RafflerTestCase(unittest.TestCase):

    def test_should_receive_a_min_and_a_max_number_for_raffle(self):
        "should receive a mininum and a maximum numbers for raffle"
        from raffle import Raffler
        raffler = Raffler(min=1, max=200)
        assert_equals(raffler.min, 1)
        assert_equals(raffler.max, 200)

class UITestCase(mocker.MockerTestCase):

    def tearDown(self):
        self.mocker.reset()

    def test_should_contain_a_button_for_raffle(self):
        "should contain a button for raffle"
