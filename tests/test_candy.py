#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 11:14:00 2025

@author: enzo
"""

from kattis.candy import candy


def test_sample1() :
    """
    Simple test

    Returns
    -------
    None.

    """
    n, f, t = 6, 2, 27
    stock = [10, 4, 20, 6, 3, 3]
    expected = (True, 1)
    assert candy(n, f, t, stock) == expected

def test_sample2() :
    """
    Second test

    Returns
    -------
    None.

    """
    n, f, t = 6, 5, 5000000000
    stock = [1000000000, 1000000000, 0, 1000000000, 1000000000, 1000000000]
    expected = (True, 3)
    assert candy(n, f, t, stock) == expected

def test_sample3() :
    """
    Detecting impossible cases

    Returns
    -------
    None.

    """
    n, f, t = 3, 2, 100
    stock = [20, 30, 60]
    expected = (False, -1)
    assert candy(n, f, t, stock) == expected

def test_sample4() :
    """
    Limit case

    Returns
    -------
    None.

    """
    n, f, t = 1, 1, 100
    stock = [100]
    expected = (True, 0)
    assert candy(n, f, t, stock) == expected
