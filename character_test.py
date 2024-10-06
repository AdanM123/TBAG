from character import Enemy, Character
from item import Item
from room import Room
#tests

def test_dave():
    dave = Enemy("Dave", "a smelly zombie")
    dave.describe()
    dave.set_conversation("Hi this is dave and I am evil")
    dave.talk()
    dave.set_weakness("Banana")
    print ("What u fighting with?")
    fight_with = input("Enter item")
    dave.fight(fight_with)
    print(f"Daves weakness is {dave.get_weakness()}")
    result = dave.fight("Banana")
    print(f"Fight result: {'Victory' if result else 'Defeat'}")#
    
    if __name__ == "__main__":
        test_dave()


#def test_character():
    print("Testing")
    goodie = Character("Goodie", "A friendly alien.")
    goodie.describe()
    goodie.set_conversation("Hi I am gooddie, a friend!?")
    goodie.talk()
    if __name__ == "__main__":
        test_character()

#def test_key():
    kitchen = Room("Kitchen")
    kitchen.set_description("Kitchen contains key.")
    
    key = Item("Key", "A secret key that opens many doors")
    kitchen.set_item(key)
    have_key = False  
    if kitchen.get_item():  
        have_key = True  
        kitchen.set_item(None)  
        print("You picked up the key")
    else:
        print("No key found")

    if have_key:
        print("You now have the key!")
    else:
        print("You don't have the key.")

    if __name__ == "__main__":
        test_key()

    



