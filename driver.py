import chess

board: chess.Board = chess.Board()

noOption: [str] = ["uci", "isready"]

# Using Fischer's suggested values
PIECE_VALUES: dict = {chess.PAWN: 100, chess.KNIGHT: 300, chess.BISHOP: 325, chess.ROOK: 500, chess.QUEEN: 900, chess.KING: 0}

# Piece-square tables
PAWN_SQUARE_EVAL = [
0,0,0,0,0,0,0,0,
50,50,50,50,50,50,50,50,
10,10,20,30,30,20,10,10,
5,5,10,25,25,10,5,5,
0,0,0,20,20,0,0,0,
5,-5,-10,0,0,-10,-5,5,
5,10,10,-20,-20,10,10,5,
0,0,0,0,0,0,0,0
]

KNIGHT_SQUARE_EVAL = [
-50,-40,-30,-30,-30,-30,-40,-50,
-40,-20,0,0,0,0,-20,-40,
-30,0,10,15,15,10,0,-30,
-30,5,15,20,20,15,5,-30,
-30,5,15,20,20,15,5,-30,
-30,0,10,15,15,10,0,-30,
-40,-20,0,0,0,0,-20,-40,
-50,-40,-30,-30,-30,-30,-40,-50,
]

BISHOP_SQUARE_EVAL = [
-20,-10,-10,-10,-10,-10,-10,-20,
-10,0,0,0,0,0,0,-10,
-10,0,5,10,10,5,0,-10,
-10,5,5,10,10,5,5,-10,
-10,0,10,10,10,10,0,-10,
-10,10,10,10,10,10,10,-10,
-10,5,0,0,0,0,5,-10,
-20,-10,-10,-10,-10,-10,-10,-20
]

ROOK_SQUARE_EVAL = [
0,0,0,0,0,0,0,0,
5,10,10,10,10,10,10,5,
-5,0,0,0,0,0,0,-5,
-5,0,0,0,0,0,0,-5,
-5,0,0,0,0,0,0,-5,
-5,0,0,0,0,0,0,-5,
-5,0,0,0,0,0,0,-5,
0,0,0,5,5,0,0,0,
]

QUEEN_SQUARE_EVAL = [
-20,-10,-10,-5,-5,-10,-10,-20,
-10,0,0,0,0,0,0,-10,
-10,0,5,5,5,5,0,-10,
-5,0,5,5,5,5,0,-5,
0,0,5,5,5,5,0,-5,
-10,5,5,5,5,5,0,-10,
-10,0,5,0,0,0,0,-10,
-20,-10,-10,-5,-5,-10,-10,-20
]

KING_SQUARE_EVAL = [
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-20,-30,-30,-40,-40,-30,-30,-20,
-10,-20,-20,-20,-20,-20,-20,-10,
20,20,0,0,0,0,20,20,
20,30,10,0,0,10,30,20
]

# Evaluates a board based on total centipawn value of white pieces - total centipawn value of black pieces
def eval(board: chess.Board) -> int:
    value = 0

    # piece value evaluations
    for key in PIECE_VALUES.keys():
        value += len(board.pieces(key, chess.WHITE)) * PIECE_VALUES[key]
        value -= len(board.pieces(key, chess.BLACK)) * PIECE_VALUES[key]

    # positional evaluations (it needs to take into account if anything is being attacked)
    # 63 - index for black
    pieces = board.piece_map()
    for key in pieces.keys():
        if pieces[key] == 'P':
            value += PAWN_SQUARE_EVAL[key]
        elif pieces[key] == 'p':
            value -= PAWN_SQUARE_EVAL[63-key]
        elif pieces[key] == 'K':
            value += KNIGHT_SQUARE_EVAL[key]
        elif pieces[key] == 'k':
            value -= KNIGHT_SQUARE_EVAL[63-key]
        elif pieces[key] == 'B':
            value += BISHOP_SQUARE_EVAL[key]
        elif pieces[key] == 'b':
            value -= BISHOP_SQUARE_EVAL[63-key]
        elif pieces[key] == 'R':
            value += ROOK_SQUARE_EVAL[key]
        elif pieces[key] == 'r':
            value -= ROOK_SQUARE_EVAL[63-key]
        elif pieces[key] == 'Q':
            value += QUEEN_SQUARE_EVAL[key]
        elif pieces[key] == 'q':
            value -= QUEEN_SQUARE_EVAL[63-key]
        elif pieces[key] == 'K':
            value += KING_SQUARE_EVAL[key]
        else:
            value -= KING_SQUARE_EVAL[63-key]

    # evaluation of tempo distributed between the evaluation and search functions

    return value

def findMove(board: chess.Board) -> chess.Move:
    bestEval: int = -999999999

    bestMove: chess.Move = None

    for move in board.legal_moves:
        board.push(move)
        currEval = negamax(board, 4)
        print(currEval, end=" ")       

        if(currEval > bestEval):
            bestEval = currEval
            bestMove = move

        board.pop()

    print()
    return bestMove

# find the value of a position through negamax search at a given depth
def negamax(board: chess.Board, depth: int):
    bestEval = -999999999
    if depth == 0:
        return eval(board) if board.turn else -eval(board)
    for move in board.legal_moves:
        board.push(move)
        currEval = -negamax(board, depth - 1) if board.turn else negamax(board, depth - 1)
        if currEval > bestEval:
            bestEval = currEval
        board.pop()
    return bestEval

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
        toMove: chess.Move = findMove(board)
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