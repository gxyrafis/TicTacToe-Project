# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Press the green button in the gutter to run the script.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from tictactoeclass import TicTacToe
from manualplayer import manual_player
from minmaxplayer import minmax_player

game = TicTacToe()
utility = game.play_game(manual_player, minmax_player)
if utility == 1:
    print("'X' won!")
elif utility == -1:
    print("'O' won!")
else:
    print('Tie!')