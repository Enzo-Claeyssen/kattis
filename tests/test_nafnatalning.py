#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 11:36:37 2025

@author: enzo
"""

from kattis.nafnatalning import nafnatalning


def test_sample1() :
    """
    Simple test

    Returns
    -------
    None.

    """
    n, p = 2, 5
    number_names = [2, 3]
    expected = 2
    assert nafnatalning(n, p, number_names) == expected


def test_sample2() :
    """
    Only one name for each origin

    Returns
    -------
    None.

    """
    n, p = 10, 5
    number_names = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    expected = 9
    assert nafnatalning(n, p, number_names) == expected
