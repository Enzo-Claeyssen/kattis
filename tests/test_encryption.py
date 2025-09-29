#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 11:33:18 2025

@author: enzo
"""

from kattis.encryption import encryption


def test_sample1() :
    """
    Testing when no common character

    Returns
    -------
    None.

    """
    s  = "aaa"
    d = "bbb"
    common = ""
    expected = "aaabbb"
    assert encryption(s, d, common) == expected


def test_sample2() :
    """
    Simple test for encryption

    Returns
    -------
    None.

    """
    s  = "abac"
    d = "adbdc"
    common = "abc"
    expected = "adbadc"
    assert encryption(s, d, common) == expected
