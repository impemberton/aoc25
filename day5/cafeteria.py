input = open("input.txt").read()
ranges, ingredients = input.split("\n\n")
ingredients = [int(i) for i in ingredients.split("\n") if i != ""]
ranges = [r.split("-") for r in ranges.split("\n")]
ranges = [(int(lower), int(upper)) for lower, upper in ranges]

fresh = 0
for ingredient in ingredients:
    is_fresh = False
    for lower, upper in ranges:
        if ingredient >= lower and ingredient <= upper:
            is_fresh = True
            break
    if is_fresh:
        fresh += 1

print(fresh)
