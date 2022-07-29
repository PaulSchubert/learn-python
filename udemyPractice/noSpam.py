menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

# one way of getting rid of spam and then printing out
#for meal in menu:
#    while "spam" in meal:
#        meal.remove("spam")
#    print(meal)


# another way of removing spam and the printing otu meals
for meal in menu:
    for index in range(len(meal) - 1, -1, -1):
        if meal[index] == "spam":
            del meal[index]
    print(", ".join(meal))


# another way of printing items as long as its not spam
#for meal in menu:
#    for ing in meal:
#        if ing == "spam":
#            continue
#        else:
#            print(ing, end=" ")
#    print()


# OR
#for meal in menu:
#    items = ", ".join((item for item in meal if item != "spam"))
#    print(items)