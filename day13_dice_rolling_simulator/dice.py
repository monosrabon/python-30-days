# Handles dice rolling logic using random module

import random

def roll_dice(sides=6, count=1):
    """
    Rolls 'count' number of dice with 'sides' sides each.
    Returns a list of results.
    """
    results = [random.randint(1, sides) for _ in range(count)]
    return results
