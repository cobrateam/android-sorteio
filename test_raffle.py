# -*- coding: utf-8 -*-

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

    def test_should_notify_user_of_the_raffled_number(self):
        "should notify user of the raffled number"
        number = 510
        droid = self.mocker.mock()
        droid.notify("O número sorteado foi: %d!" % number)
        self.mocker.result("user notified")
        self.mocker.replay()

        from raffle import notify_raffled_number
        notify_raffled_number(droid, number)

        self.mocker.verify()
