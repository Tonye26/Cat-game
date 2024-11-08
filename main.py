import pygame
DISPLAYSURF = pygame.display.set_mode((300,300))
cat_attributes = {
    "intelligence": 10,
    "energy": 50,
    "weight": 10,
    # change the inital values above
}

print("Welcome to my cat game!")

# Take the user inputs for name and colour:
name = input("Enter name:")
colour=input("What colour would you like your cat to be? ")
# ...

# start the while loop
while True:
    # Finish the string below
    option = input("What would you like to do? 1. Play with your cat 2. Train your cat 3.Feed your Cat 4.Put it to sleep 5.show stats ")

    if option == '1':
        # change the cat's attributes here
        energy=cat_attributes.get("energy")
        if energy<5:
            print("Your cat is low on energy and must sleep you cannot play with it")
        else:
            energy1=energy-10
            cat_attributes["energy"]=energy1
        pass
    elif option == '2':
        intelligence=cat_attributes.get("intelligence")
        intelligence1=intelligence+10
        cat_attributes["intelligence"]=intelligence1
        energy=cat_attributes.get("energy")
        energy1=energy-10
        cat_attributes["energy"]=energy1
        weight=cat_attributes.get("weight")
        weight1=weight-5
        cat_attributes["weight"]=weight1
        pass
    elif option=="3":
        weight=cat_attributes.get("weight")
        if weight>20:
            print("Your cat cannot eat anymore")
        else:
            weight2=weight+5
            cat_attributes["weight"]=weight2
    elif option=="4":
        energy=cat_attributes.get("energy")
        energy2=energy+20
        cat_attributes["energy"]=energy2
    # elif ...
    elif option=="5":
        print(name)
        print(colour)
        print(cat_attributes)
        pass

    # finish off the if statements below
    if cat_attributes["energy"] < 0:
        print("Your cat is tired and needs to sleep")
        pass
    # elif ...
    elif cat_attributes["weight"]>20:
        print("Your cat is too fat and must train")
