import random
class Die:
    def __init__(self, faces = 6):
        self.faces = faces
        self.currVal = 0
    def roll(self):
        roll = randint(1, self.faces)
        self.currVal = roll
        return roll
    def __repr__(self):
        return (self.currVal)
    
class PigGamePlayer:
    def __init__(self, name):
        self.name = name
        self.score = 0
    def turn(self):
        self.score += Die.currVal()
        if self.score > 100:
            print(self.name, "has won! The game has ended with score:", score)
    

class PigGame:
    def __init__(self, name1, name2):
        self.p1 = name1
        self.p2 = name2
    def play(self):
        print("Player 1 goes first")
        action = "0"
        player = self.p1
        if player == self.p1:
            total = 0
            print(self.p1, "'s turn:")
            while action != "1":
                action = input("You can roll or hold (0 or 1) ")
                if action == "0":
                    val = Die.roll
                    print("You rolled a", val)
                    total += val
                    print("Your total for this turn is:", total)
                    if val == 1:
                        print("You rolled a 1.")
                        player == self.p2
                        action = "1"
                    else:
                        PigGamePlayer.turn
        if player == self.p2:
            total = 0
            print(self.p2, "'s turn:")
            while action != "1":
                action = input("You can roll or hold (0 or 1) ")
                if action == "0":
                    val = Die.roll()
                    print("You rolled a", val)
                    total += val
                    print("Your total for this turn is:", total)
                    if val == 1:
                        print("You rolled a 1.")
                        player == self.p1
                        action = "1"
                    else:
                        PigGamePlayer.turn


def main():
    name1 = input("Player #1, enter your name: ")
    name2 = input("Player #2, enter your name: ")
    game1 = PigGame(name1, name2)
    game1.play()
main()
