def handleCommand(operation, parameters):
    if operation == "uci":
        print("id name BrothFish")
        print("id author Alain Lou")
        print("uciok")
    elif operation == "isready":
        print("readyok")
    elif operation == "go":
        print("bestmove h7h5")
while True:
    line = input()
    if line == "quit":
        break
    else:
        args = line.split()
        handleCommand(args[0], args[1:])