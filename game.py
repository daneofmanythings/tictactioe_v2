"""
A class to keep track of meta data about the game.
"""

class Game :
    def __init__(self) :
        self.players = []
        self.board = []

    def add_player(self, player) :
        self.players.append(player)