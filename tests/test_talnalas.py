#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 11:43:39 2025

@author: enzo
"""

import pytest
from kattis.talnalas import talnalas


def test_sample1() :
    n, m = 4, 5
    initial = "1234"
    objective = "1337"
    lucky = [
        "1234",
        "1337",
        "1236",
        "2234",
        "1336",
        "1235",
        "0234"
        ]
    expected_size = 4
    expected_path = [
        "1234",
        "1235",
        "1236",
        "1336",
        "1337"
        ]
    assert talnalas(n, m, initial, objective, lucky) == (True, expected_size, expected_path)


def test_sample2() :
    n, m = 1, 8
    initial = "2"
    objective = "8"
    lucky = [
        "2",
        "8",
        "1",
        "9",
        "6",
        "4",
        "5",
        "3",
        "0",
        "7"
        ]
    expected_size = 4
    expected_path = [
        "2",
        "1",
        "0",
        "9",
        "8"
        ]
    assert talnalas(n, m, initial, objective, lucky) == (True, expected_size, expected_path)


def test_sample3() :
    n, m = 8, 4
    initial = "85362837"
    objective = "63812736"
    lucky = [
        "85362837",
        "63812736",
        "13248765",
        "89816432",
        "85362838",
        "81234876"
        ]
    expected_size = 0
    expected_path = []
    assert talnalas(n, m, initial, objective, lucky) == (False, expected_size, expected_path)