"""
Python solution for the following kattis problem :
    https://open.kattis.com/problems/bocchinorokku
"""

import marimo


app = marimo.App(width="medium")


@app.function
def sorting_bocchinorokku(n, weights) :
    """
    https://open.kattis.com/problems/bocchinorokku

    There are n rocks of different weights.
    Weights of the ith rock is accessible through weights[i]

    We want to know for each rock, how many other rock weigh less.


    Parameters
    ----------
    n : Integer
        Number of rocks
    weights : Array of Integer
        The weight of each rock

    Returns
    -------
    answer : Array of Integer
        answer[i] is the number of rock that weigh less than the ith rock.

    """
    answer = [0 for _ in range(n)]
    sorted_weights = weights.copy()
    sorted_weights.sort()

    map_to_old_index = {} # Maps a rock's weight to it's index in weights
    for i in range(n) :
        map_to_old_index[weights[i]] = i

    for i in range(n) :
        answer[map_to_old_index[sorted_weights[i]]] = i

    return answer


@app.cell
def _():
    """
    Cell for notebook to test function

    Returns
    -------
    None.

    """
    n = 3
    weights = [2, 3, 0]
    print(sorting_bocchinorokku(n, weights))
