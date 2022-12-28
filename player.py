"""
This is the player class. Stores all player specific information.
Note* storing the index of a player in another class is kind of dodgy,
but it works, questionmark?
"""

class Player :
    
    def __init__(self, symbol, index) :
        self.symbol = symbol  # Symbol to place on the board
        self.index = index  # Index of player in the Game's list
        self.name = ''
        self.wins = 0
        self.moves = [
            False, False, False, False, False, False, False, False, False
        ]

    def get_name(self) :
        self.name = input("Please enter your name: ")

    def get_move(self) :
        move = input(f'{self.name}, what is your move? ')
        while move not in ('1','2','3','4','5','6','7','8','9') :
            move = input('Enter a valid move (1 - 9):  ')
        return int(move)

    def apply_move(self, move) :
        self.moves[move - 1] = True
        return move, self.symbol

    def has_won(self) :
        self.wins += 1
        print(f'{self.name} has won! They have won {self.wins} times.')
