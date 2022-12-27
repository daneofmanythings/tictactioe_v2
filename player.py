"""
This is the player class. It is a subclass of the Game class.
"""

class Player :
    def ___init___(self, symbol) :
        self.name = ''
        self.symbol = symbol
        self.moves = []
        self.wins = 0

    def get_name(self) :
        self.name = input("Please enter your name: ")

