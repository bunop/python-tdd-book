#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 11:55:08 2018

@author: Paolo Cozzi <cozzi@ibba.cnr.it>
"""

from django.urls import resolve
from django.test import TestCase

from lists.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
