def heuristic_eval(game, state):
    player = game.to_move(state)

    def piece_score():
        countX = 0
        countO = 0
        for tile in state.board.values():    #Count X and Y tiles
            if tile == "X":
                countX += 1
            elif tile == "O":
                countO +=1
        if countX > countO:
            return (100*countX)/(countX + countO)
        elif countO > countX:
            return (100*countO)/(countX + countO)
        else:
            return 0

    def corner_score():
        countX = 0
        countO = 0
        for y in range(0, 8, 7):
            for x in range(0, 8, 7):
                if not ((x,y) in state.board):
                    continue
                if state.board[(x,y)] == "X":
                    countX += 1
                elif state.board[(x,y)] == "O":
                    countO += 1
        return 25*(countX - countO)

    def near_corner_score():
        countX = 0
        countO = 0

        for y in range(0, 8, 7):            #Check each corner
            for x in range(0, 8, 7):
                if (x,y) in state.board and state.board[(x,y)] != "X" and state.board[(x,y)] != "O":
                    for w in range(y-1, y+2):       #check each valid block near corner
                        for z in range(x-1, x+2):
                            if w == y and z == x:
                                continue
                            elif (z,w) in state.board and state.board[(z,w)] == "X":
                                countX += 1
                            elif (z,w) in state.board and state.board[(z,w)] == "O":
                                countO += 1
        return -12.5*(countX - countO)

    def mobility_score():
        countX = len(game.getValidMoves(state.board, "X"))
        countO = len(game.getValidMoves(state.board, "O"))
        if countX > countO:
            return (100*countX)/(countX + countO)
        elif countX < countO:
            return (100*countO)/(countX + countO)
        else:
            return 0

    def position_score():
        weights = [[20,-3,11,8,8,11,-3,20],
                   [-3,-7,-4,1,1,-4,-7,-3],
                   [11,-4,2,2,2,2,-4,11],
                   [8,1,2,-3,-3,2,1,8],
                   [8,1,2,-3,-3,2,1,8],
                   [11,-4,2,2,2,2,-4,11],
                   [-3,-7,-4,1,1,-4,-7,-3],
                   [20,-3,11,8,8,11,-3,20]]

        countX = 0
        countO = 0

        for y in range(0,8):
            for x in range(0,8):
                if not ((x,y) in state.board):
                    continue
                if state.board[(x,y)] == "X":
                    countX += weights[x][y]
                elif state.board[(x,y)] == "O":
                    countO += weights[x][y]
        return countX - countO

    score = 10 * piece_score() + 801724 * corner_score() + 382026 * near_corner_score() + 78922 * mobility_score() + 10 * position_score()
    if player == "X":
        return score
    else:
        return -score