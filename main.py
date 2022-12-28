"""
The main logic for the game.
"""

from player    import Player
from board     import Board
from game      import Game

def get_player_move(player) :
    """
    Calls the get_move method for the player.
    validates the move against a global list of untaken spaces
    """
    
    valid = False
    
    while not valid :
        move = player.get_move()
        if move in valid_moves :
            valid_moves.remove(move)
            valid = True
            continue

    return move


# Instantiates the game and board
game = Game()
board = Board()

# Instantiates the players and adds them to the game
player_1 = Player('X')
player_1.get_name()
game.add_player(player_1)

player_2 = Player('O')
player_2.get_name()
game.add_player(player_2)

# Lists all the untaken moves thus far.
valid_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# game loop that ends once all the moves are taken.
keep_playing = True
while len(valid_moves) > 0 :
    
    print(board.print_board())  # Prints the game board

    p1_move = get_player_move(player_1)  # Grabs player_1's potential move and validates it
    p1_move = player_1.apply_move(p1_move)  # Applies a valid move to the player
    board.update_board(p1_move[0] - 1, p1_move[1])  # Passes the data on to the game board
    keep_playing = game.keep_playing(0)  # Checks to see if player has won against the games win conditions
    if keep_playing == False :
        player_1.has_won()
        break    

    print(board.print_board())

    p2_move = get_player_move(player_2)  # Does all the same for player_2
    p2_move = player_2.apply_move(p2_move)
    board.update_board(p2_move[0] - 1, p2_move[1])
    keep_playing = game.keep_playing(1)
    if keep_playing == False :
        player_2.has_won()
        break
