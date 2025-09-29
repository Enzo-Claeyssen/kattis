"""
Python solution for the following kattis problem :
    https://open.kattis.com/problems/candy
"""

import math


def get_distance(f, selected) :
    """
    Gives the minimal number of steps to switch the F selected boxes
    to the first f positions.
    
    selected is the array of indeces of selected boxes it has to be sorted
    and len(selected) = f
    """
    d = 0
    for i in range(f) :
        current = selected[i]
        d += current - i
    return d


def get_combinations(n, f, start_index) :
    """
    Returns the f-uplet of integers from 0 to n-1
    Which are sorted, with only unique elements and which starts at start_index
    """
    if f == 1 :
        res = []
        for i in range(start_index, n) :
            res.append([i])
        return res
    res = []
    for i in range(start_index, start_index + n - (f-1)) :
        for comb in get_combinations(n, f-1, i+1) :
            res.append([i] + comb)
    return res


def candy(n, f, t, stock) :
    """
    https://open.kattis.com/problems/candy
    
    There are n boxes in a room.
    The ith box has stock[i] candies remaining.
    Boxes are ordered, the box 0 is the nearest box from the entrance
    And the box n-1 is the one that is the most far away from the entrance.
    
    Each step we can only permute two adjacent boxes.
    
    We want the first f nearest box from the entrance to have a sum
    of candies of at least t.
    
    Output a boolean telling whetther it is possible to fullfill 
    the condition, and if it is, 
    output the smallest number of steps needed to fullfill it.

    Parameters
    ----------
    n : Integer
        Number of boxes
    f : Integer
        The number of boxes considered close enough of the entrance to be
        considered.
    t : Integer
        The smallest sum of the first F boxes we have to reach.
    stock : Array of Integers
        The amount of candies in each box and their posittion from the entrace

    Returns
    -------
    Boolean
        True iff there exists a solution, False otherwise.
    Integer
        The smallest number of steps to reach the solution.

    """
    combinations = get_combinations(n, f, 0)

    mini = math.inf
    best_comb = None
    for comb in combinations :
        s = 0
        for i in comb :
            s += stock[i]
        if s >= t :
            if get_distance(f, comb) < mini :
                mini = get_distance(f, comb)
                best_comb = comb
    if best_comb is None :
        return False, -1
    return True, mini
