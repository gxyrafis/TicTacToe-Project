# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Press the green button in the gutter to run the script.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import sys

from a_b_heuristicplayer import a_b_heuristic_player
from reversiclass import Reversi
from tictactoeclass import TicTacToe
from manualplayer import manual_player
from minmaxplayer import minmax_player
from randomplayer import random_player
from a_b_player import a_b_player

while True:
    while True:
        gamechoice = input("Press 1 for TicTacToe, press 2 for Reversi or press q to quit:\n>$")
        if gamechoice == "1" or gamechoice == "2" or gamechoice == "q":
            break
        else:
            print("Error: Invalid input!")
    if gamechoice == "1":
        game = TicTacToe()
    elif gamechoice == "2":
        game = Reversi()
    elif gamechoice == "q":
        sys.exit()
    gametype = input("Press \"1\" to play against the MinMax Algorithm.\nPress \"2\" to have the random player play against it.\n"
                     "Press \"3\" to play against the A-B Algorithm.\nPress \"4\" to have the random player play against it.\n"
                     "Press \"5\" to run MinMax vs Random 100 times.\nPress \"6\" to run A-B vs random 100 times.\n"
                     "Press \"7\" to run 100 games between 2 random players. \n"
                     "Press \"8\" to run to run A-B with a depth of 3 vs random 100 times. \n"
                     "Press \"q\" to exit\n>$")
    skip = False

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
            order = input("Who goes first? Press \"R\" for the random player or \"AB\" for the A-B Algorithm\n>$")
            if order.upper() == "R":
                utility = game.play_game(random_player, a_b_player)
                break
            elif order.upper() == "AB":
                utility = game.play_game(a_b_player, random_player)
                break
            else:
                print("Invalid input!\n")
    elif gametype == "5":
        skip = True
        while True:
            order = input("Who goes first? Press \"R\" for the random player or \"M\" for the Minmax Algorithm\n>$")
            wincounterX = 0
            wincounterO = 0
            if order.upper() == "R":
                for i in range(100):
                    utility = game.play_game(random_player, minmax_player)
                    if utility == -1:
                        wincounterO += 1
                    elif utility == 1:
                        wincounterX += 1
                break
            elif order.upper() == "M":
                for i in range(100):
                    utility = game.play_game(minmax_player, random_player)
                    if utility == 1:
                        wincounterX += 1
                    elif utility == -1:
                        wincounterO += 1
                break
            else:
                print("Invalid input!\n")
    elif gametype == "6":
        skip = True
        while True:
            order = input("Who goes first? Press \"R\" for the random player or \"AB\" for the A-B Algorithm\n>$")
            wincounterX = 0
            wincounteO = 0
            if order.upper() == "R":
                for i in range(100):
                    utility = game.play_game(random_player, a_b_player)
                    if utility == -1:
                        wincounterO += 1
                    elif utility == 1:
                        wincounterX += 1
                break
            elif order.upper() == "AB":
                for i in range(100):
                    utility = game.play_game(a_b_player, random_player)
                    if utility == 1:
                        wincounterX += 1
                    elif utility == -1:
                        wincounterO += 1
                break
            else:
                print("Invalid input!\n")
    elif gametype == "7":
        skip = True
        wincounterX = 0
        wincounterO = 0
        for i in range(1):
            utility = game.play_game(random_player, random_player)
            if utility == -1:
                wincounterO += 1
            elif utility == 1:
                wincounterX += 1
    elif gametype == "8":
        skip = True
        while True:
            order = input("Who goes first? Press \"R\" for the random player or \"AB\" for the A-B Algorithm\n>$")
            wincounterX = 0
            wincounterO = 0
            if order.upper() == "R":
                for i in range(100):
                    utility = game.play_game(random_player, a_b_heuristic_player)
                    if utility == -1:
                        wincounterO += 1
                    elif utility == 1:
                        wincounterX += 1
                break
            elif order.upper() == "AB":
                for i in range(100):
                    utility = game.play_game(a_b_heuristic_player, random_player)
                    if utility == 1:
                        wincounterX += 1
                    elif utility == -1:
                        wincounterO += 1
                break
            else:
                print("Invalid input!\n")

    elif gametype.lower() == "q":
        exit(0)
    else:
        print("Invalid input!\n")
        continue #Without this, the utility checks below crash the programme
    if utility == 1 and skip != True:
        print("'X' won!")
    elif utility == -1 and skip != True:
        print("'O' won!")
    elif utility == 0 and skip != True:
        print('Tie!')
    elif skip == True:
        print("X won " + str(wincounterX) + " times.\nO won " + str(wincounterO) + " times.\nThere were " + str((100 - (wincounterO + wincounterX))) + " draws.\n")