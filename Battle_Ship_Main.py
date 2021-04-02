import os
import random

class Player_Info:
    def __init__(self):
        self.player_ship_board = Board(10, 10, "O")
        self.bot_ship_board = Board(10, 10, "O")
        self.bot_attack_board = Board(10, 10, "O")
        self.player_attack_board = Board(10, 10, "O")
        os.system('cls' if os.name == 'nt' else 'clear')
        self.player_name = input("Welcome to Terminal Battle-Ship, please provide a Player Name:")
        os.system('cls' if os.name == 'nt' else 'clear')


    def decide_first_turn(self):
        return random.randrange(1, 3)

    def choose_ship_location(self):
        '''
        Function that prompts the player for where they would like to place their 5 ships & returns a player board
        with the ships placed & ready to play.


        Carrier(5 spaces)
        Battleship(4 spaces)
        Cruiser(3 spaces)
        Submarine(3 spaces)
        Destroyer(2 spaces)
        :return:
        '''
        ##TODO; Begin/finish writing choose_ship_location
        pass

class Game:
    def __init__(self):
        self.player_info = Player_Info()
        self.first_turn = "Player" if self.player_info.decide_first_turn() == 1 else "Bot"
        print(self.first_turn)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Player name set to {self.player_info.player_name} & '{self.first_turn}' gets to go first!")
        input("\n Press Enter")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Setting up new Board...\n")
        print("Legend: \n O = Empty Space \n X = Occupied by Battle Ship \n ")
        print("-----Player Ship Board-----")
        if self.first_turn == "Player":
            print(self.player_info.player_ship_board.constructed_board(), f"\n \n....Enter to choose ship location & fire the first shot!")
            input()
            print(self.player_info.player_ship_board.bare_board())
        else:
            print(self.player_info.player_ship_board.constructed_board(), f"\n \n....Enter to choose ship location.")
            input()




    def play_game(self):
        ##TODO; Begin writing play_game function under Game class
        pass


    def restart_game(self):
        ##TODO; Begin working on restart_game function under Game class
        pass


class Board(list):

    def __init__(self, x: int = 0, y: int = 0, character: str = "O"):
        self.board = [[character] * x for _ in range(y)]


    def generate_board(x: int = 0, y: int = 0, character: str = "O"):
        '''

        :param x: takes in the number of items you'd like on the X axis of the board.
        :param y: takes in the number of items you'd like on the Y axis of the board.
        :param character: takes in the character you'd like to populate the board with.
        :return:
        '''
        return [[character] * x for _ in range(y)]

    def bare_board(self):
        return self.board

    def constructed_board(self):
        return "\n".join(" ".join(row) for row in self.board)

Game()

##TODO; Begin writing code to initiate, & play game using the classes above.


