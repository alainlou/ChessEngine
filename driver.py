import chess

myboard = chess.Board()

noOption = ["uci", "isready"]

moveCounter = 0

def simpleCommand(operation):
    if operation == "uci":
        print("id name BrothFish")
        print("id author Alain Lou")
        print("uciok")
    elif operation == "isready":
        print("readyok")

def handleCommand(operation, parameters, moveCounter, board):
    # TODO handle when they give FEN notation
    if operation == "position" and "startpos" in parameters: #set the position of the internal board
        parameters = parameters.split()
        print(parameters, moveCounter)
        if parameters[-1] != "startpos":
            board.push_uci(parameters[-1])
        #for move in parameters[(2+moveCounter):]:
        #    board.push_uci(move)
        #    print(move)
        moveCounter += 2
    elif operation == "go":
        moves = []
        for move in board.legal_moves:
            moves.append(move)
        board.push(moves[0])
        print("bestmove", moves[0])

# We can make this I/O loop async eventually
while True:
    line = input()
    if line == "quit":
        break
    elif not " " in line:
        simpleCommand(line)        
    else:
        print(line)
        flag = line.index(" ")
        handleCommand(line[:flag], line[flag+1:], moveCounter, myboard)