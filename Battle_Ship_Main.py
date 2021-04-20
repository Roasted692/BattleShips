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
        input()


    def play_game(self):
        ##TODO; Begin writing play_game function under Game class
        print("Legend: \n O = Empty Space \n X = Occupied by Battle Ship\n")
        print("-----Player Ship Board-----")
        if self.first_turn == "Player":
            self.player_info.player_ship_board.constructed_board()
            print("\n \n....Enter to choose ship location & fire the first shot!")
            input()
            self.player_info.player_ship_board.bare_board()
        else:
            self.player_info.player_ship_board.constructed_board()
            print("\n \n....Enter to choose ship location.")
            input()
            self.player_info.player_ship_board.bare_board()

    def place_player_ships(self):
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
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Using the board below as reference, place your ships via the prompts that appear.\n")
        self.player_info.player_ship_board.constructed_board()
        self.player_info.player_ship_board.place_carrier()

        ##TODO; Create method for placing each of the 5 ships in the board class, run each method so player can have full board.


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
        print(self.board)


    def constructed_board(self):
        print("    A-B-C-D-E-F-G-H-I-J")
        test = [" ".join(self.board[row]) for row in range(len(self.board))]


        ##for row in range(len(self.board)):
            ##print(" ".join(self.board[row]))

        for x in range(1,11):
            if x == 10:
                print(f"{x}- " + test[x-1])
            else:
                print(f"{x}-  " + test[x-1])

    def place_carrier(self):
        starting_spot = input("Provide a starting spot between any of the 10 spots on the board.")
        ending_spot = input(f"Provide an endpoint that is within 5 spaces from the starting point selected {starting_spot}.")


    def check_provided_spots(self):
        pass



    def convert_board_to_dict(self):

        pass


Game = Game()
Game.play_game()





##TODO; Turn current list that represents the board in dictionary so that the player & Bot can interact w/ it, function below





##TODO; Begin writing code to initiate, & play game using the classes above.


