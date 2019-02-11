import chess

board = chess.Board()

noOption = ["uci", "isready"]

moveCounter = 0

def simpleCommand(operation):
    if operation == "uci":
        print("id name BrothFish")
        print("id author Alain Lou")
        print("uciok")
    elif operation == "isready":
        print("readyok")

def handleCommand(operation, parameters, moveCounter):
    if operation == "position": #set the position of the internal board
        parameters = parameters.split()
        board.push_uci(parameters[-1])
        moveCounter += 1
    elif operation == "go":
        moves = []
        for move in board.legal_moves:
            moves.append(move)
        board.push(moves[0])
        moveCounter += 1
        print("bestmove", moves[0])

# We can make this I/O loop async eventually
while True:
    line = input()
    if line == "quit":
        break
    elif not (" " in line):
        simpleCommand(line)        
    else:
        flag = line.index(" ")
        handleCommand(line[:flag], line[flag+1:], moveCounter)