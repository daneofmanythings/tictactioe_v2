"""
This is the player class. Stores all player specific information.
"""

class Player :
    def ___init___(self, symbol) :
        self.symbol = symbol
        self.name = ''
        self.moves = []
        self.wins = 0

    def get_name(self) :
        self.name = input("Please enter your name: ")

