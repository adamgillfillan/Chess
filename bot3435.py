__author__ = 'Adam'

from player import Player
import sys
import time


class Bot3435(Player):
    def move(self):
        time.sleep(1)
        print("Bot's turn.")
        for letter in "Bot is calculating his move ...":
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.3)
        print("\nBot has moved. Your turn!")

        # print("\n\nYou successfully moved your {0} from {1}{2} to {3}{4}!".format(
        #     piece.type, old_posn.x, old_posn.y, piece.posn.x, piece.posn.y))