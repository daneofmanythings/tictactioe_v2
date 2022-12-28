"""
The class for the gameboard.
"""

class Board:
    """
    This class mostly is here to draw the gameboard in the terminal
    """
    def __init__(self) :
        self.board = {  # each key represents a space on a 3x3 grid
            0:'_',
            1:'_',
            2:'_',
            3:'_',
            4:'_',
            5:'_',
            6:'_',
            7:'_',
            8:'_',
        }

    def generate_board(self) -> str:  # Returns a board string to print in the terminal
        """
        Generates the gameboard for terminal print.
        """
        board = ''

        for idx, space in self.board.items() :
            if idx % 3 == 0 :
                board += '\n'
            board += space

        return board

    def update_board(self, loc: int, sym: str) :  # loc is 1-9, and sym is the players symbol
        """
        Adds the player's symbol to the gameboard.
        """
        self.board[loc] = sym
