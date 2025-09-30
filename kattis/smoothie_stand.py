"""
Python solution for the following kattis problem :
    https://open.kattis.com/problems/smoothiestand
"""
import math
import marimo

app = marimo.App(width="medium")

@app.function
def smoothie_stand(k, ingredients, recipes) :
    """
    https://open.kattis.com/problems/smoothiestand
    We have k ingredients and r recipes.
    For each ingredients, we have a stock, the stock of ingredient i
    can be retrieved with ingredients[i]
    
    Each recipes uses a certain amount of stock of each ingredients each
    time the recipe is done.
    The first recipe uses recipes[0][i] stock of the ith ingredient.
    Each time the ith recipe is done, we gain a score of recipes[i][k]
    
    The goal is to select a single recipe and make the maximum score.
    
    Output the maximum score achievable.

    Parameters
    ----------
    k : Integer
        The number of ingredients
    r : Integer
        The number of recipes
    ingredients : Array of Integers
        The stock of all ingredients
    recipes : Array of Array of Integers
        Contrains all recipes.
        Each array describing a recipe contrains the necessary stock of
        each ingredient to make it once and the score obtained from
        doing this recipe once.

    Returns
    -------
    best_score : Integer
        The maximum score achievable by choosing only a single recipe.

    """
    best_score = -1
    for recipe in recipes :
        bottleneck = math.inf
        for i in range(k) :
            if recipe[i] > 0 :
                s = ingredients[i] // recipe[i]
                bottleneck = min(bottleneck, s)
        score = bottleneck * recipe[k]

        best_score = max(best_score, score)

    return best_score


@app.cell
def _():
    """
    Cell for notebook to test function

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
    print(smoothie_stand(k, ingredients, recipes))
