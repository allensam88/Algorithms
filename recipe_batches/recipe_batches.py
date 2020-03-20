#!/usr/bin/python
# STEP 1: UNDERSTAND
# Look at readme

# STEP 2: PLAN
# *****PSEUDO CODE*****
# loop thru each recipe dictionary key (i)
# then loop thru each ingredients dictionary key (j) to find matching redipe key (i)
# compare key values
# if recipe value is less than available ingredients value
# send back minimum batch value


import math


def recipe_batches(recipe, ingredients):
    batch_count = []

    if len(recipe) != len(ingredients):
        return 0

    for i in recipe:
        for j in ingredients:
            if i == j:
                batch_count.append(ingredients[j]/recipe[i])
            elif not i or not j:
                batch_count.append(0)

    if min(batch_count) >= 1:
        return int(min(batch_count))
    else:
        return 0


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 2, 'butter': 40, 'flour': 20}
    ingredients = {'milk': 5, 'butter': 120, 'flour': 500}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
