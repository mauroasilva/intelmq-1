# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest

import intelmq.lib.test as test
from intelmq.bots.parsers.turris.parser import TurrisGreylistParserBot


class TestTurrisGreylistParserBot(test.BotTestCase, unittest.TestCase):
    """
    A TestCase for TurrisGreylistParserBot.
    """

    @classmethod
    def set_bot(cls):
        cls.bot_reference = TurrisGreylistParserBot
        cls.default_input_message = {'__type': 'Report'}

if __name__ == '__main__':
    unittest.main()
