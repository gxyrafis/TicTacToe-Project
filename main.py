# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Press the green button in the gutter to run the script.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from tictactoeclass import TicTacToe
from manualplayer import manual_player
from minmaxplayer import minmax_player
from randomplayer import random_player
from a_b_player import a_b_player

while True:
    game = TicTacToe()
    gametype = input("Press \"1\" to play against the MinMax Algorithm.\nPress \"2\" to have the random player play against it.\n"
                     "Press \"3\" to play against the A-B Algorithm.\nPress \"4\" to have the random player play against it.\n"
                     "Press \"q\" to exit\n>$")
    if gametype == "1":
        while True:
            order = input("Who goes first? Press \"I\" for yourself or \"M\" for the MinMax Algorithm\n>$")
            if order.upper() == "I":
                utility = game.play_game(manual_player, minmax_player)
                break
            elif order.upper() == "M":
                utility = game.play_game(minmax_player, manual_player)
                break
            else:
                print("Invalid input!\n")
    elif gametype == "2":
        while True:
            order = input("Who goes first? Press \"R\" for the random player or \"M\" for the MinMax Algorithm\n>$")
            if order.upper() == "R":
                utility = game.play_game(random_player, minmax_player)
                break
            elif order.upper() == "M":
                utility = game.play_game(minmax_player, random_player)
                break
            else:
                print("Invalid input!\n")
    elif gametype == "3":
        while True:
            order = input("Who goes first? Press \"I\" for yourself or \"AB\" for the A-B Algorithm\n>$")
            if order.upper() == "I":
                utility = game.play_game(manual_player, a_b_player)
                break
            elif order.upper() == "AB":
                utility = game.play_game(a_b_player, manual_player)
                break
            else:
                print("Invalid input!\n")
    elif gametype == "4":
        while True:
            order = input("Who goes first? Press \"R\" for the random player or \"AB\" for the MinMax Algorithm\n>$")
            if order.upper() == "R":
                utility = game.play_game(random_player, a_b_player)
                break
            elif order.upper() == "AB":
                utility = game.play_game(a_b_player, random_player)
                break
            else:
                print("Invalid input!\n")
    elif gametype.lower() == "q":
        exit(0)
    else:
        print("Invalid input!\n")
        continue #Without this, the utility checks below crash the programme
    if utility == 1:
        print("'X' won!")
    elif utility == -1:
        print("'O' won!")
    else:
        print('Tie!')