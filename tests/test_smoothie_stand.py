#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 11:39:55 2025

@author: enzo
"""

from kattis.smoothie_stand import smoothie_stand


def test_sample1() :
    """
    Simple test for smoothie stand

    Returns
    -------
    None.

    """
    k = 3
    ingredients = [5, 10, 10]
    recipes = [
        [1, 4, 1, 5],
        [3, 3, 3, 3]
        ]
    expected = 10
    assert smoothie_stand(k, ingredients, recipes) == expected


def test_sample2() :
    """
    Testing when most valuable recipe should not be picked.

    Returns
    -------
    None.

    """
    k = 4
    ingredients = [10, 9, 8, 7]
    recipes = [
        [0, 1, 2, 4, 10],
        [3, 1, 1, 2, 4],
        [2, 0, 3, 3, 5]
        ]
    expected = 12
    assert smoothie_stand(k, ingredients, recipes) == expected
