shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

itemToFind = "albatross"
foundAt = None

#for index in range(6)
#for index in range(len(shopping_list)):
#    if shopping_list[index] == itemToFind:
#        foundAt = index
#        break #go out of the main loop

if itemToFind in shopping_list:
    foundAt = shopping_list.index(itemToFind)

if foundAt is not None:
    print("Item found at position {}".format(foundAt))
else:
    print("{} not found".format(itemToFind))

