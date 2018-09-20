#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 11:55:08 2018

@author: Paolo Cozzi <cozzi@ibba.cnr.it>
"""

from django.test import TestCase


class SmokeTest(TestCase):

    def test_bad_maths(self):
        self.assertEqual(1 + 1, 3)
