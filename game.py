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
        self.win_cons_raw = (  # Tuple of regex expressions outlining win conditions
            'XXX......',
            '...XXX...',
            '......XXX',
            'X..X..X..',
            '.X..X..X.',
            '..X..X..X',
            'X...X...X',
            '..X.X.X..'
        )
        self.win_cons = [re.compile(x) for x in self.win_cons_raw]  # Making regex into re.Patterns

    def add_player(self, player) :  # player is an instance of Player()
        """
        Adds the player to the game's list.
        """
        self.players.append(player)

    def keep_playing(self, idx: int) -> bool:  # idx is player.index for the player being checked
        """
        Checks the games win conditions against a players moves
        to determine if a win has happened.
        """
        for win_con in self.win_cons :
            if win_con.match(self.players[idx].moves) :  # If it matches, someone has won
                return False

        return True
