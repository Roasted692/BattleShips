import os
import random

class Initiate_Game:
    def __init__(self):
        self.player = Create_Player()
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Setting up new Board...\n")
        print("Legend: \n O = Empty Space \n X = Occupied by Battle Ship \n ")
        self.board = Board()
        print(self.board, "\n \n....Enter to continue.")
        input()





class Board(list):

    def __str__(self):
        return "\n".join(" ".join(row) for row in self)


def decide_first_turn():
    return random.randrange(1,3)


class Create_Player:
    def __init__(self):
        self.player_name = input("Welcome to Terminal Battle-Ship, please provide a Player Name:")
        os.system('cls' if os.name == 'nt' else 'clear')
        self.first_turn = "Player" if decide_first_turn() == 1 else "Bot"
        print(self.first_turn)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Player name set to {self.player_name} & '{self.first_turn}' gets to go first!")
        input("\n Press Enter")


Initiate_Game()










