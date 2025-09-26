#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 11:07:34 2025

@author: enzo
"""

import pytest
from kattis.bocchinorokku import sorting_bocchinorokku



def test_sample1() :
    assert sorting_bocchinorokku(5, [3, 9, 4, 1, 7]) == [1, 4, 2, 0, 3]

def test_sample2() :
    assert sorting_bocchinorokku(7, [1, 3, 5, 7, 2, 4, 6]) == [0, 2, 4, 6, 1 ,3, 5]