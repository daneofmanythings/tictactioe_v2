"""
A class to keep track of meta data about the game.
"""

import re

class Game :
    """
    Holds meta information about the game. Might see more use with more features.
    """
    def __init__(self) :
        self.players = []
        self.win_cons_raw = (
            'XXX......',
            '...XXX...',
            '......XXX',
            'X..X..X..',
            '.X..X..X.',
            '..X..X..X',
            'X...X...X',
            '..X.X.X..'
        )
        self.win_cons = [re.compile(x) for x in self.win_cons_raw]

    def add_player(self, player) :
        """
        Adds the player to the game's list.
        """
        self.players.append(player)

    def keep_playing(self, idx) :
        """
        Checks the games win conditions against a players moves
        to determine if a win has happened.
        """
        for win_con in self.win_cons :
            if win_con.match(self.players[idx].moves) :
                return False

        return True
