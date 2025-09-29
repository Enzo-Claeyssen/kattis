"""
Python solution for the following kattis problem :
    https://open.kattis.com/problems/talnalas
"""
import math

def get_distance(s1, s2) :
    """
    Computes the number of steps needed to go from s1 to s2.

    Parameters
    ----------
    s1 : String
        The first code.
    s2 : String
        The second code.

    Returns
    -------
    s : Integer
        The number of steps required to select s2 if s1 is initially selected.

    """
    n = len(s1)
    s = 0
    for i in range(n) :
        diff = abs(int(s1[i]) - int(s2[i]))
        if diff == 9 :
            s += 1
        else :
            s += diff
    return s




def search(initial, end, get_neighbor, already_seen) :
    """
    Finds the shortest path from intial to end on the unoriented and 
    non-weighted graph get_neighbor.

    Parameters
    ----------
    initial : String
        The starting point of the path
    end : String
        The end of the path
    get_neighbor : Dict
        The graph where a key is a node and values are connected nodes.
    already_seen : Array of Strings
        Nodes that have already been explored.

    Returns
    -------
    Boolean
        True if there exists a path from intial to end.
    Integer
        The length of the smallest path from initial to end.
    Array of Strings
        The smallest path from initial to end.

    """
    if initial == end :
        return True, 0, [initial]
    found = False
    best_size = math.inf
    best_path = []
    for neighbor in get_neighbor[initial] :
        if neighbor not in already_seen :

            current_found, current_size, current_path = search(
                neighbor,
                end,
                get_neighbor,
                already_seen + [neighbor]
                )

            if current_found :
                if current_size < best_size :
                    found = True
                    best_size = current_size + 1
                    best_path = [initial] + current_path
    return found, best_size, best_path




def talnalas(initial, objective, lucky) :
    """
    https://open.kattis.com/problems/talnalas
    
    We have a lock which needs a passcode to be unlocked.
    The passcode contains n digits from 0 to 9.
    For each digit, the lock is provided a circular system to select the 
    digit.
    
    At each step, we can only move one circle in one direction thus modifying
    only a single digit either by adding 1 to it or removing 1.
    Because the selection system is circular, if we add 1 to 9 we select 0,
    and if we substract 1 to 0 we select 9.
    
    We are also provided the initial state of the lock (current selected code)
    and the objective, the passcode we have to select to unlock.
    
    m is the number of lucky words other than the initial and objective codes.
    initial and objective codes are lucky codes.
    
    At each step, we must have selected a lucky code.
    For example if the current selected is 1, 2, 3
    Then we can add 1 to the digit 3 only if 1, 2, 4 is a lucky code.
    
    Output wether there is a solution and if there's at least one,
    then output the minimal number of steps required to obtain the objective
    from the initial selected code and output all selected codes we have to go
    through to unlock the lock.

    Parameters
    ----------
    initial : String
        The initially selected code
    objective : String
        The code we have to reach
    lucky : Array of Strings
        Contains all lucky codes (including initial and objectives)

    Returns
    -------
    bool
        True iff there is a solution (we can reach the objective by passing
        through only lucky codes), False otherwise.
    Integer
        The minimal number of step to reach to objective.
    Array of Strings
        All codes we'll have to go through (including initial and objective)
        in the right order.

    """
    graph = {}
    for s1 in lucky :
        graph[s1] = []
        for s2 in lucky :
            if get_distance(s1, s2) == 1 :
                graph[s1].append(s2)
    found, size, path = search(initial, objective, graph, [])
    if not found :
        return False, 0, []
    return True, size, path
