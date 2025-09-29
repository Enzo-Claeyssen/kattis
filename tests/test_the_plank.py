#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 11:49:50 2025

@author: enzo
"""

from kattis.the_plank import theplank


def test_sample1() :
    """
    Simple test for plank solution
    """
    length = 4
    expected = 7
    assert theplank(length) == expected
