# -*- coding: utf-8 -*-
# Copyright 2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import unittest

from zpl2 import Zpl2


class TestZpl2(unittest.TestCase):

    def setUp(self):
        self.zpl = Zpl2()

    def test_init_encoding(self):
        """ It should set encoding """
        self.assertEqual(self.zpl.encoding, 'utf-8')

    def test_init_buffer(self):
        """ It should set the buffer. """
        self.assertEqual(self.zpl._buffer, [])
