#!/usr/bin/env python3
import ipdb

from classes.player import Player
from classes.game import Game
from classes.result import Result

if __name__ == "__main__":
    print("HELLO! :) let's debug :vibing_potato:")
    game = Game("Skribbl.io")
    game_2 = Game("Scattegories")
    player = Player("Saaammmm")
    result_1 = Result(player, game, 2000)
    result_2 = Result(player, game, 3500)
    result_3 = Result(player, game_2, 19)
    ipdb.set_trace()
