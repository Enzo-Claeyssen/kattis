

def ding_dong_ditch(N, Q, angers, expectations) :
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
    for Ai in angers :
        s += Ai
        cumulative_anger.append(s)
    
    return [cumulative_anger[Bj - 1] for Bj in expectations]
