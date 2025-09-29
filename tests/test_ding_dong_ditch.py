#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 11:24:13 2025

@author: enzo
"""

from kattis.ding_dong_ditch import ding_dong_ditch



def test_sample1() :
    """
    Simple test

    Returns
    -------
    None.

    """
    n, q = 4, 2
    angers = [3, 2, 1, 4]
    expectations = [3, 1]
    expected = [6, 1]
    assert ding_dong_ditch(n, q, angers, expectations) == expected


def test_sample2() :
    """
    Second test

    Returns
    -------
    None.

    """
    n, q = 5, 1
    angers = [12, 2, 14, 6, 9]
    expectations = [3]
    expected = [17]
    assert ding_dong_ditch(n, q, angers, expectations) == expected
