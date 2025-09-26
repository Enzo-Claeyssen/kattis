#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 11:36:37 2025

@author: enzo
"""

import pytest
from kattis.nafnatalning import nafnatalning


def test_sample1() :
    n, P = 2, 5
    number_names = [2, 3]
    expected = 2
    assert nafnatalning(n, P, number_names) == expected


def test_sample2() :
    n, P = 10, 5
    number_names = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    expected = 9
    assert nafnatalning(n, P, number_names) == expected