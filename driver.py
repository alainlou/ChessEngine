import chess

board = chess.Board()

def handleCommand(operation, parameters):
    if operation == "uci":
        print("id name BrothFish")
        print("id author Alain Lou")
        print("uciok")
    elif operation == "isready":
        print("readyok")
    elif operation == "position": #set the position of the internal board
        if parameters[:8] != "startpos":
            fenString = parameters[:parameters.index("moves")]
            board.set_board_fen(fenString)
        moves = parameters[parameters.index("moves")+5:].split()
        for move in moves:
            foo = chess.Move.from_uci(move)
            board.push(foo)
    elif operation == "go":
        print("bestmove h7h5")

# We can make this I/O loop async eventually
while True:
    line = input()
    if line == "quit":
        break
    else:
        flag = line.index(" ")
        handleCommand(line[:flag], line[flag+1:])