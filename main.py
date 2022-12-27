"""
The main logic for the game.
"""

from player    import Player
from board     import Board
from game      import Game

game = Game()

player_one = Player('X')
player_one.get_name()
game.add_player(player_one)

player_two = Player('O')
player_two.get_name()
game.add_player(player_two)


