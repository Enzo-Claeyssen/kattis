



def get_distance(F, selected) :
    """
    Gives the minimal number of steps to switch the F selected boxes
    to the first F positions.
    
    selected is the array of indeces of selected boxes it has to be sorted
    and len(selected) = F
    """
    d = 0
    for i in range(F) :
        current = selected[i]
        d += current - i
    return d


def get_combinations(N, F, start_index) :
    """
    Returns the F-uplet of integers from 0 to N-1
    Which are sorted, with only unique elements and which starts at start_index
    """
    if F == 1 :
        res = []
        for i in range(start_index, N) :
            res.append([i])
        return res
    else :
        res = []
        for i in range(start_index, start_index + N - (F-1)) :
            for comb in get_combinations(N, F-1, i+1) :
                res.append([i] + comb)
        return res
    
    

def candy(N, F, T, stock) :
    """
    https://open.kattis.com/problems/candy
    
    There are N boxes in a room.
    The ith box has stock[i] candies remaining.
    Boxes are ordered, the box 0 is the nearest box from the entrance
    And the box N-1 is the one that is the most far away from the entrance.
    
    Each step we can only permute two adjacent boxes.
    
    We want the first F nearest box from the entrance to have a sum
    of candies of at least T.
    
    Output a boolean telling whetther it is possible to fullfill 
    the condition, and if it is, 
    output the smallest number of steps needed to fullfill it.

    Parameters
    ----------
    N : Integer
        Number of boxes
    F : Integer
        The number of boxes considered close enough of the entrance to be
        considered.
    T : Integer
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
    import math
    
    combinations = get_combinations(N, F, 0)
    
    mini = math.inf
    best_comb = None
    for comb in combinations :
        s = sum([stock[i] for i in comb])
        if s >= T :
            if get_distance(F, comb) < mini :
                mini = get_distance(F, comb)
                best_comb = comb
    if best_comb == None :
        return False, -1
    else :
        return True, mini