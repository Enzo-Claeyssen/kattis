"""
Python solution for the following kattis problem :
    https://open.kattis.com/problems/theplank
"""
import marimo

app = marimo.App(width="medium")

@app.function
def theplank(length) :
    """
    https://open.kattis.com/problems/theplank
    
    We are provided an infinite amount of planks of length 1, 2 and 3.
    We're able to glew planks together to form a longer plank.
    How many combinations of glued planks can we make to create a plank
    of a certain length ?
    
    Example :
        To have a plank of length 3, we can have :
            1 - 1 - 1
            1 - 2
            2 - 1
            3
        There 4 ways to glue planks of length <= 3 st they form a plank of 
        length 3.
    

    Parameters
    ----------
    length : Integer
        The length of the plank we want to have.

    Returns
    -------
    Integer
        The number of glued planks combinations we can make to get the plank
        of length "length".

    """
    if length <= 2 :
        return length
    if length == 3 :
        return 4
    return theplank(length-1) + theplank(length-2) + theplank(length-3)


@app.cell
def _():
    """
    Cell for notebook to test function

    Returns
    -------
    None.

    """
    length = 4
    print(theplank(length))
