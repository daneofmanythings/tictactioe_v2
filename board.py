"""
The class for the gameboard.
"""

class Board:
    def __init__(self) :
        self.board = {  # each number represents a space on a 3x3 grid
            1:'',
            2:'',
            3:'',
            4:'',
            5:'',
            6:'',
            7:'',
            8:'',
            9:'',
        }

    def place_symbol(self,symbol: str, location: int) :
        self.board[location] = symbol

    
