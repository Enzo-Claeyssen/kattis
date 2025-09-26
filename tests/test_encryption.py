#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 11:33:18 2025

@author: enzo
"""

import pytest
from kattis.encryption import encryption


def test_sample1() :
    s  = "aaa"
    d = "bbb"
    common = ""
    expected = "aaabbb"
    assert encryption(s, d, common) == expected


def test_sample2() :
    s  = "abac"
    d = "adbdc"
    common = "abc"
    expected = "adbadc"
    assert encryption(s, d, common) == expected