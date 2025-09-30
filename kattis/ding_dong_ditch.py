"""
Python solution for the following kattis problem :
    https://open.kattis.com/problems/dingdongditch
"""
import marimo

app = marimo.App(width="medium")

@app.function
def ding_dong_ditch(n, q, angers, expectations) :
    """
    https://open.kattis.com/problems/dingdongditch

    We have N houses and Q persons.
    The ith person wants to ring expectations[i] houses.
    However each person wants to minimize the sum of anger they receive
    from ringing.

    The anger of the ith house can be retrieved with angers[i]

    We want to output the smallest sum of angers each person can receive from
    ringing at expectations[i] doorbells.

    Parameters
    ----------
    N : Integer
        Number of houses
    Q : Integer
        Number of persons
    angers : Array of Integers
        The anger received from ringing a doorbell.
    expectations : Array of Integers
        The amount of doorbells the person i wants to ring.

    Returns
    -------
    Array of Integers
        The smallest sum of anger the person i can receive.

    """
    angers.sort()

    cumulative_anger = []
    s = 0
    for i in range(n) :
        a_i = angers[i]
        s += a_i
        cumulative_anger.append(s)

    return [cumulative_anger[expectations[j] - 1] for j in range(q)]


@app.cell
def _():
    """
    Cell for notebook to test function

    Returns
    -------
    None.

    """
    n, q = 4, 2
    angers = [3, 2, 1, 4]
    expectations = [3, 1]
    print(ding_dong_ditch(n, q, angers, expectations))
