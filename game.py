"""
A class to keep track of meta data about the game.
"""

class Game :
    def __init__(self) :
        self.players = []
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

    def keep_playing(self, idx) :
        for win_con in self.win_cons :
            if win_con == self.players[idx].moves :
                return False

        return True
