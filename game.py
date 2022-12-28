"""
A class to keep track of meta data about the game.
"""

class Game :
    """
    Holds meta information about the game. Might see more use with more features.
    """
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
            if win_con == self.players[idx].moves :
                return False

        return True
