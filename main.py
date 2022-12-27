"""
The main logic for the game.
"""

from player    import *
from gameboard import *
from game      import *

player_one = Player()
player_one.get_info()
print(player_one.name, player_one.symbol)