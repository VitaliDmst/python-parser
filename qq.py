def cakes(recipe, available):
    # TODO: insert code

    for i in range(len(recipe)):
        print(available.values(recipe[i]))


recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}

print(cakes(recipe, available))