"""Imports the Cat class from cat.py, create three cats that the user can interact
with by feeding, hitting, choosing the night or quit option."""

import cat

# creates list of 3 cats
cats = []
names = ["Felix","Mittens","Toast"]
for elem in range(3): # number of cats is 3
    cats.append(cat.Cat(names[elem]))

while True:
    # prints the status of each cat
    for elem in range(3):
        print(f"{elem+1}. {cats[elem]}")
    # give the user a menu of options
    print("\n1. Feed | 2. Hit | 3. Night | 4. Quit")
    choice = input("Choice: ")
    # feeding
    if choice == "1":
        cat_choice = input("Which cat? ")
        # exception handling
        if cat_choice.isnumeric():
            if int(cat_choice) >= 1 and int(cat_choice) <= 4:
                cats[int(cat_choice)-1].feed()
            else:
                print("Choice must be between 1-4.")
        else:
            print("Choice must be a positive integer.")
    # hitting
    elif choice == "2":
        cat_choice = input("Which cat? ")
        # exception handling
        if cat_choice.isnumeric():
            if int(cat_choice) >= 1 and int(cat_choice) <= 4:
                cats[int(cat_choice)-1].hit()
            else:
                print("Choice must be between 1-4.")
        else:
            print("Choice must be a positive integer.")
    # night
    elif choice == "3":
        # elem represents a cat
        for elem in cats:
            elem.night()
            if elem.gift:
                print(f"{elem.name} has left you a gift!")
    elif choice == "4":
        break
    # exception handling
    elif not choice.isnumeric():
        print("Choice must be a positive integer.")
    elif int(choice) < 1 or int(choice) > 4:
        print("Choice must be between 1-4.")