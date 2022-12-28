"""
The class for the gameboard.
"""

class Board:
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

    def print_board(self) -> str:
        
        board = ''

        for idx, space in self.board.items() :
            if idx % 3 == 0 :
                board += '\n'
            board += space

        return board

    def update_board(self, loc: int, sym: str) :
        self.board[loc] = sym

    
