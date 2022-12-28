"""
A class to keep track of meta data about the game.
"""

class Game :
    def __init__(self) :
        self.players = []
        self.board = '.........'
        self.win_cons = (
            [True, True, True, False, False, False, False, False, False],
            [False, False, False, True, True, True, False, False, False],
            [False, False, False, False, False, False, True, True, True],
            [True, False, False, True, False, False, True, False, False],
            [False, True, False, False, True, False, False, True, False],
            [False, False, True, False, False, True, False, False, True],
            [True, False, False, False, True, False, False, False, True],
            [False, False, True, False, True, False, True, False, False],
        )
    def add_player(self, player) :
        self.players.append(player)