


def nafnatalning(n, P, number_names) :
    """
    https://open.kattis.com/problems/nafnatalning
    
    We have n different origins of words.
    We can look up to P pairs of words per day.

    There are number_names[i] different words of origin i.
    
    We want to know how many days it will take to look at all pairs of words
    that are from different origins.

    Parameters
    ----------
    n : Integer
        Number of origins
    P : Integer
        Number of pairs of words we can look each days.
    number_names : Array of Integers
        Number of different words for each origins.

    Returns
    -------
    Integer
        Number of day needed to look at all pairs of words that are not of 
        the same origin.

    """
    number_of_pairs = 0
    for i in range(n) :
        for j in range(i+1, n) :
            number_of_pairs += number_names[i] * number_names[j]
    
    if number_of_pairs%P == 0 :
        return number_of_pairs // P
    else :
        return number_of_pairs // P +1
