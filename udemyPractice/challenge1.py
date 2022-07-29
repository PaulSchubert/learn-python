
selection = 5

while selection != 0:

    while 0 > selection or selection > 4:
        print("1. Bread \n 2. Cheese \n 3. Salami \n 4. Python \n 0. Exit")
        selection = int(input())

    if selection == 0:
        break

    print("You selected {}".format(selection))
    selection = 5
