

def encryption(s, d, common) :
    """
    https://open.kattis.com/problems/encryption
    
    We have a word s and d.
    We say that a is a subsquence of b if we can have a from removing letters
    of b.
    
    We are provided common which is the longest string which is both a 
    subsequence of s and a subsequence of d.
    
    We want the shortest string for which s and d are both a subsequence.

    Parameters
    ----------
    s : String
        The first word
    d : String
        The second word
    common : String
        The longest common subsequence of s and d

    Returns
    -------
    res : String
        The shortest word for which s and d are subsequences.

    """
    
    res = ""
    
    s_iterator = iter(s)
    d_iterator = iter(d)
    for element in common :
        candidate = next(s_iterator)
        while candidate != element :
            res += candidate
            candidate = next(s_iterator)
        
        candidate = next(d_iterator)
        while candidate != element :
            res += candidate
            candidate = next(d_iterator)
        
        res += element
    
    for element in s_iterator :
        res += element
    for element in d_iterator :
        res += element
    
    return res
