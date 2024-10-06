from room import Room
from character import Character, Enemy, Friend
from item import Item
kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining hall")

key = Item("key", "A secret key that opens many doors.")
kitchen.set_item(key) 
locked_door = Room("an ancient locked door which requires a special key to unlock.")
locked_door.set_description("A old battered door with cobwebs.")

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Hi this is dave and I am evil")
dave.set_weakness("Banana")
dining_hall.set_character(dave)

goodie = Character("goodie", "A kind alien.")
goodie.set_conversation("Hi I am gooddie, a friend!?")
kitchen.set_character(goodie)


kitchen.set_description("A dank and dirty room with flies")
ballroom.set_description("Vast room ,shiny floor")
dining_hall.set_description("A nice lunch room")


kitchen.link_room(dining_hall,"south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

have_key = False

current_room = kitchen


while True:
    print("\n")
    current_room.get_details()
    inhabitant =  current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    command = input(">").lower()
    if command in ["north", "south", "east", "west"]:
        new_room = current_room.move(command)
        if new_room == locked_door and not have_key:
            print("Door locked, access denied, you need a key")
        else:
            current_room = new_room

    elif command == "take key":
        if Item is not None and Item.get_name() == "Key":
            have_key = True  
            current_room.set_item(None)  
            print("picked up the key")
        else:
            print("there's no key here")

    
    elif command == "use key":
        if have_key:
            print("You unlock the door")
            current_room = locked_door 
            print("You've entred")
            have_key = False
        else:
            print("You don't have a key to use")


        
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
        else:
            print("There's no one to talk to.")
    
    elif command == "hug":
        if isinstance(inhabitant, Friend):
            inhabitant.hug()
        else:
            print("hes a mortal enemy, you cannot hug him.")
    elif command == "gift":
        if isinstance(inhabitant, Friend):
            gift = input("What gift do you want to offer? ")
            inhabitant.offer_gift(gift)


    elif command == "fight":
        if inhabitant is not None:
            print("What item do you want use?")
            fight_with = input("Enter item: ")
            if inhabitant.fight(fight_with):  
                print(f"You have successfully beaten {inhabitant.get_name()}.")  
            else:
                print(f"You were beaten by {inhabitant.get_name()}.")  
                print("The end") 
                break 
        else:
            print("There's no one to fihgt")

