import player
import world

class Game():
    def __init__(self):
        self.escaped = False
        name = input("What is your name?\n")
        self.player = player.Player(name)
        print("Hello, %s" %name)
        x_size = int(input("How many blocks wide should the room be?\n"))
        y_size = int(input("How many blocks deep should the room be?\n"))
        self.world = world.World(x_size,y_size)
        
    def play(self):
        while ~self.escaped:
            action = input("What should I do? (move, knock, location, check, use, unlock, quit)\n")
            if action == "move":
                move_x = int(input("How many steps should I take left or right?\n"))
                move_y = int(input("How many steps should I take forward or backward?\n"))
                if self.world.can_move(move_x, move_y):
                    self.player.move(move_x, move_y)
                else:
                    print("You can't move there.")
            elif action == "knock":
                self.player.knock(self.world)
            elif action == "location":
                print(self.player.get_location())
            elif action == "unlock":
                self.escaped = self.player.unlock(self.world)
            elif action == "check":
                self.player.check_for_item(self.world)
            elif action == "use":
                self.player.use_item()
            elif action == "quit":
                break
            else:
                print("I don't understand the command")



