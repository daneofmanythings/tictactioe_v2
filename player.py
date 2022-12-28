"""
This is the player class. Stores all player specific information.
Note* storing the index of a player in another class is kind of dodgy,
but it works, questionmark?
"""

class Player :
    """
    This is a class holding all the player information
    """
    def __init__(self, symbol: str, index: int) :
        self.symbol = symbol  # Symbol to place on the board, Typically 'X' or 'O'
        self.index = index  # Index of player in the Game's list. First player is 0, ect
        self.name = ''
        self.wins = 0
        self.no_moves = '123456789'  # DO NOT TOUCH!
        self.moves = '123456789'  # Get's updated as play progresses

    def get_name(self) :
        """
        Get's the players name. Makes main.py look better.
        """
        self.name = input("Please enter your name: ")

    def get_move(self) :
        """
        Gets a possible move and checks that it is an int between 1 and 9.
        """
        move = input(f'{self.name}, what is your move? ')
        while move not in self.no_moves:
            move = input('Enter a valid move (1 - 9):  ')
        return move  # Digit string

    def apply_move(self, move: str) :  # move ends up being a digit string until this returns it as int
        """
        Once the move has been validated from get_move, and the function
        in main.py against previous moves, applies the move to the player
        and game. Also returns the players symbol to add to the board.
        """
        self.moves = self.moves.replace(move, 'X')
        return int(move), self.symbol

    def reset_moves(self) :
        """
        Resets the players move tracker.
        """
        self.moves = self.no_moves

    def has_won(self) :
        """
        Call on a player once they have won to increment their win counter.
        """
        self.wins += 1
        print(f'{self.name} has won! They have won {self.wins} times.')
