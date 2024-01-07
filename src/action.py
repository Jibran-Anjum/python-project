from location import ItemLocation

import time

class Action(ItemLocation):

    items_collected = []

    def __init__(self, name):
        self.__name = name
        
    # Setter module to set the name of the player
    def setName(self) -> None:
        name = input("Enter Name: ")
        self.__name = name    

    # Getter module to get the name of the Player
    def getName(self):
        return self.__name

    # collection process along with the outcome of the fight
    def collectItems(self) -> None:

        self.setName()

        print("-------------------------------")
        print(f"Welcome {self.__name}... You've Begin to play the game!\nHere's your challenge move to 'North', 'South', and 'East'to collect the weapon.\nMove to 'West' if you think you have collected the tools to fight the monster.\nIf you want to quit (because you're scare) just type 'quit'")
        print("-------------------------------")


        while True:

            move_to = input("Your Move: ")

            # Try-Except block if in any-case the key is invalid
            try:
                item_at_the_location = self.item_location[move_to.lower()]
            except:
                print("--> Invalid Input")
                continue
            
            # conditions based on the input of the user
            if move_to.lower() == "north":
                if item_at_the_location not in self.items_collected:
                    self.items_collected.append(item_at_the_location)
                    print(f"--> You've collected '{item_at_the_location}' in {move_to.lower()}")
                    
            elif move_to.lower() == "south":
                if item_at_the_location not in self.items_collected:
                    self.items_collected.append(item_at_the_location)
                    print(f"--> You've collected '{item_at_the_location}' in {move_to.lower()}.")
                    
            elif move_to.lower() == "east":
                if item_at_the_location not in self.items_collected:
                    self.items_collected.append(item_at_the_location)
                    print(f"--> You've collected '{item_at_the_location}' in {move_to.lower()}.")
                    
            elif move_to.lower() == "west":
                if "Sword" in self.items_collected and "Bow and Arrow" in self.items_collected and "Dagger" in self.items_collected:
                    print("\n-----------------------------------------------")
                    print("--> You're about to fight with the Monster...")
                    time.sleep(2)
                    print("\n--> You've Won!!!")
                    print("-----------------------------------------------\n")
                    break
                else:
                    print("\n-----------------------------------------------")
                    print("--> You're about to fight with the Monster...")
                    time.sleep(2)
                    print("\n--> You've Lost, since you didn't collected all of the items.")
                    print("-----------------------------------------------\n")
                    break
            elif move_to.lower() == "quit":
                print("--> Bye Bye... Take care")
                break
