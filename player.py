"""
This is the player class. Stores all player specific information.
"""

class Player :
    
    def __init__(self, symbol) :
        self.symbol = symbol
        self.name = ''
        self.wins = 0
        self.moves = [
            False, False, False, False, False, False, False, False, False
        ]

    def get_name(self) :
        self.name = input("Please enter your name: ")

    def get_move(self) :
        move = int(input(f'{self.name}, what is your move? '))
        self.moves[move - 1] = True
        return move, self.symbol
