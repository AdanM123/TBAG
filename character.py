class Character():
    def __init__(self, char_name,char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        print(f"{self.name} is in this room")
        print (self.description)

    def set_conversation(self,conversation):
        self.conversation = conversation

    def talk(self):
        if self.conversation is not None:
            print(f"{self.name} says: {self.conversation}")
        else:
            print(f"{self.name} says they dont want to talk with you")

    def fight(self):
        print(f"{self.name} doesn't want to fight you")
        return False


class Enemy(Character):
    def __init__(self, char_name, char_description):
        
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    
    def get_weakness(self):
        return self.weakness
    
    def fight(self,combat_item):
        if combat_item == self.weakness:
            print(f"you fend {self.name} off with {combat_item}")
            return True
        else:
            print(f"{self.name} crushes you, adventurer")
            return False
        
    def sleep(self):
        self.sleeping = True
        print(f"You try to put {self.name} to sleep.")

    def bribe(self, amount):
        
        if amount > 1000:  
            print(f"{self.name} is corrupt and accepted your bribe of {amount}")
            return True
        else:
            print(f"{self.name} refuses the bribe, you havae been exposed")
            return False
        
    def steal(self):
        if self.sleeping == True:
            print(f"You stole something from {self.name}")
        else:
            print(f"{self.name} caught you stealing")


class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)

    def hug(self):
        print(f"You hugged {self.name}")

    def offer_gift(self, gift):
        print(f"You offer {self.name} a {gift}.")


      
 
        

       

    







    

        
        


