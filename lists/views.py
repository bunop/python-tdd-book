#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 11:55:08 2018

@author: Paolo Cozzi <cozzi@ibba.cnr.it>
"""

from django.http import HttpResponse


# Create your views here.
def home_page(request):
    return HttpResponse('<html><title>To-Do lists</title></html>')
