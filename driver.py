import chess

board = chess.Board()

noOption = ["uci", "isready"]

def simpleCommand(operation):
    if operation == "uci":
        print("id name BrothFish")
        print("id author Alain Lou")
        print("uciok")
    elif operation == "isready":
        print("readyok")

def handleCommand(operation, parameters):
    # TODO handle when they give FEN notation
    global board

    if operation == "position" and "startpos" in parameters: #set the position of the internal board
        parameters = parameters.split()
        if parameters[-1] != "startpos":
            board.push_uci(parameters[-1])

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
        handleCommand(line[:flag], line[flag+1:])