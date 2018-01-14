def groupingDishes(dishes):
    ingredients = {}
    for recipe in dishes:
        dish = recipe[0]
        for ingredient in recipe[1:]:
            if ingredient not in ingredients:
                ingredients[ingredient] = []
            ingredients[ingredient].append(dish)

    output = []
    for ingredient in sorted(ingredients):
        if len(ingredients[ingredient]) < 2:
            continue
        output.append([ingredient] + sorted(ingredients[ingredient]))
    
    return output