"""
The main logic for the game.
"""

from player    import Player
from board     import Board
from game      import Game


def get_player_move(player) :  # Takes instance of Player()
    """
    Calls the get_move method for the player.
    validates the move against a global list of untaken spaces
    """
    valid = False

    while not valid :
        move = player.get_move()  # Loops until valid move is input
        if move not in taken_moves : # Checking the move against the global variable
            taken_moves.append(move)  # Adds the move to the list of moves
            valid = True
            continue

    return move

def player_turn(player) :  # Takes instance of Player()
    """
    A loop for a player's turn.
    """
    move = get_player_move(player)  # Grabs player_1's potential move and validates it
    move = player.apply_move(move)  # Applies a valid move to the player
    board.update_board(move[0] - 1, move[1])  # Passes the data on to the game board, loc and symbol
    print(board.generate_board())  # Prints the game board

    return  # I like how this looks. Don't @ me

def check_win(player) :  # Takes instance of Player()
    """
    Checks to see if a player has won, then returns if the game should continue
    """
    keep_playing = game.keep_playing(player.index)
    if keep_playing is False :
        player.has_won()

    return keep_playing

def main() :
    """
    Main logic function.
    """
    # game loop that ends once all the moves are taken, or a player wins
    keep_playing = True
    counter = 0  # Oscillates the turn order
    print(board.generate_board())  # initial print
    while len(taken_moves) < 9 and keep_playing :

        if counter == 0 :
            player_turn(player_1)
            keep_playing = check_win(player_1)
            counter += 1
        else :
            player_turn(player_2)
            keep_playing = check_win(player_2)
            counter -= 1


############################################################################
#                             GAME IS HERE                                 #
############################################################################

if __name__ == '__main__' :

    # Instantiates the game and board
    game = Game()
    board = Board()

    # Instantiates the players and adds them to the game
    player_1 = Player('X', 0)
    player_1.get_name()
    game.add_player(player_1)

    player_2 = Player('O', 1)
    player_2.get_name()
    game.add_player(player_2)

    play_again = True
    while play_again :

        # Main game
        taken_moves = []
        main()

        # Asking to play again
        response = input('Would you like to play again? (y/n): ').lower()
        while response not in ('y', 'n') :
            response = input('Please input y or n: ').lower()

        if response == 'y' :
            # Resets the gamestate if players choose to play again.
            board = Board()
            taken_moves = []
            player_1.reset_moves()
            player_2.reset_moves()
            print(board.generate_board())

        if response == 'n' :
            print('Thank you for playing!')
            play_again = False
