import random
class World():
    def __init__(self,x=5,y=5):
        self.size_x = x
        self.size_y = y
        location_item = (random.randint(1,self.size_x), random.randint(1,self.size_y))
        self.door = (random.randint(1,self.size_x), random.randint(1,self.size_y))
        self.item = (location_item, ("potion", random.randint(0,1)))
        location_key = (random.randint(1,self.size_x), random.randint(1,self.size_y))
        self.key = (location_key, "key")
        print("location of key is %d, %d location of door is %d, %d location of item is %d, %d" %(location_key[0],location_key[1], self.door[0], self.door[1], location_item[0],location_item[1]))

    def can_move(self,x,y):
        return x <= self.size_x and y <= self.size_y

    def knock(self, location):
        if(location == self.door):
            print("Here is the door!")
        else:
            print("No door here")

    def unlock(self, location):
        if(location == self.door):
            return True
        else:
            print("There is no door to unlock.")
            return False


    def check_for_item(self, location):
        if self.item[0] == location :
            print("You have acquired a potion!")
            return self.item[1]
        elif self.key[0] == location:
            print("You have acquired a key!")
            return self.key
        else:
            print("Nothing here")
            return False
