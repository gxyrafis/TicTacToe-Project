import numpy as np
from reversievalfunc import heuristic_eval

def a_b_heuristic_player(game, state):
    """Given a state in a game, calculate the best move by searching
    forward all the way to the terminal  states. [Figure 5.3]"""
    #With Alpha-Beta pruning, depth of 3 and heuristic function

    player = game.to_move(state)
    depth = 0

    def max_value(state, a, b, depth):
        if game.terminal_test(state) or depth == 3:
            return heuristic_eval(game, state)

        depth += 1
        v = -np.inf
        for action in game.actions(state):
            v = max(v, min_value(game.result(state, action), a, b, depth))
            if v >= b:
                return v
            a = max(a, v)
        return v

    def min_value(state, a, b, depth):
        if game.terminal_test(state) or depth == 3:
            return heuristic_eval(game, state)

        depth += 1
        v = np.inf
        for action in game.actions(state):
            v = min(v, max_value(game.result(state, action), a, b, depth))
            if v <= a:
                return v
            b = min(b, v)
        return v

    return max(game.actions(state), key=lambda c: min_value(game.result(state, c), -np.inf, np.inf, depth))