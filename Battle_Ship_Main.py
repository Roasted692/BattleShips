import os
import random


class Player_Info:
    def __init__(self):
        self.player = welcome_create_player()
        self.player_ship_board = Board(Board.generate_board(10, 10, "O"))
        self.bot_ship_board = Board(Board.generate_board(10, 10, "O"))
        self.player_attack_board = Board(Board.generate_board(10, 10, "O"))

class Game:
    def __init__(self):
        self.player_info = Player_Info()
        self.player = self.player_info.player

        os.system('cls' if os.name == 'nt' else 'clear')
        print("Setting up new Board...\n")
        print("Legend: \n O = Empty Space \n X = Occupied by Battle Ship \n ")
        print("-----Player Ship Board-----")
        print(self.player_info.player_ship_board, "\n \n....Enter to continue.")
        input()


class Board(list):

    def generate_board(x: int = 0, y: int = 0, character: str = "O"):
        '''

        :param x: takes in the number of items you'd like on the X axis of the board.
        :param y: takes in the number of items you'd like on the Y axis of the board.
        :param character: takes in the character you'd like to populate the board with.
        :return:
        '''
        return [[character] * x for _ in range(y)]

    def __str__(self):
        return "\n".join(" ".join(row) for row in self)


def decide_first_turn():
    return random.randrange(1, 3)

class welcome_create_player:
    def __init__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.player_name = input("Welcome to Terminal Battle-Ship, please provide a Player Name:")
        os.system('cls' if os.name == 'nt' else 'clear')
        self.first_turn = "Player" if decide_first_turn() == 1 else "Bot"
        print(self.first_turn)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Player name set to {self.player_name} & '{self.first_turn}' gets to go first!")
        input("\n Press Enter")



Game()