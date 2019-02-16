import chess

board: chess.Board = chess.Board()

noOption: [str] = ["uci", "isready"]
# Using Fischer's suggested values
PIECE_VALUES: dict = {chess.PAWN: 100, chess.KNIGHT: 300, chess.BISHOP: 325, chess.ROOK: 500, chess.QUEEN: 900, chess.KING: 0}

# Evaluates a board based on total centipawn value of white pieces - total centipawn value of black pieces
def eval(board: chess.Board) -> int:
    value = 0

    for key in PIECE_VALUES.keys():
        value += len(board.pieces(key, chess.WHITE)) * PIECE_VALUES[key]
        value -= len(board.pieces(key, chess.BLACK)) * PIECE_VALUES[key]

    return -value

def findMove(board: chess.Board, moves: [chess.Move]) -> chess.Move:
    bestEval: int = -999999999
    bestMove: chess.Move = moves[0]

    for move in moves:
        board.push(move)
        currEval = eval(board)
        if(currEval > bestEval):
            bestEval = currEval
            bestMove = move
        board.pop()
    
    return bestMove



def simpleCommand(operation: str):
    if operation == "uci":
        print("id name BrothFish")
        print("id author Alain Lou")
        print("uciok")
    elif operation == "isready":
        print("readyok")

def handleCommand(operation: str, parameters: [str]):
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
        toMove: chess.Move = findMove(board, moves)
        board.push(toMove)
        print("bestmove", toMove)

# We can make this I/O loop async eventually
while True:
    line: str = input()
    if line == "quit":
        break
    elif not " " in line:
        simpleCommand(line)        
    else:
        flag = line.index(" ")
        handleCommand(line[:flag], line[flag+1:])