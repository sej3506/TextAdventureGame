import world

class Player():
    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.hp = 100
        self.item = False;
        self.key = False;
        
    def move(self,x=0,y=0):
        self.x += x
        self.y += y
            
    def get_location(self):
            return (self.x, self.y)

    def knock(self, world):
        world.knock(self.get_location())

    def unlock(self, world):
        if(self.key):
            print("You have unlocked the door and escaped!")
            return world.unlock(self.get_location())
        else:
            print("You do not have a key!")

    def check_for_item(self, world):
        item = world.check_for_item(self.get_location())
        if(item):
            if(item[0] == "potion"):
                self.item = item
            else:
                self.key = item

    def use_item(self):
        if(self.item):
            if(self.item[1]):
                self.hp += 5
                print("HP increased by 5")
            else:
                self.hp -= 5
                print("HP decreased by 5")
        else:
            print("You have nothing to use.")

