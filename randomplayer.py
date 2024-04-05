from numpy import random

def random_player(game, state):
    #AI player that chooses one of the available actions at random
    #with equal chances of each action being chosen
    player = game.to_move(state)
    actions = game.actions(state)

    while True:
        choice = random.randint(len(actions))
        return actions[choice]