"""
The main logic for the game.
"""

from player    import Player
from board     import Board
from game      import Game

game = Game()
board = Board()

player_1 = Player('X')
player_1.get_name()
game.add_player(player_1)

player_2 = Player('O')
player_2.get_name()
game.add_player(player_2)

while True :
    
    p1_move = player_1.get_move()
    board.update_board(p1_move[0], p1_move[1])
    print(board.print_board())

    p2_move = player_2.get_move()
    board.update_board(p2_move[0], p2_move[1])
    print(board.print_board())

    break