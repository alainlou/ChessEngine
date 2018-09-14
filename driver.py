import chess
import sys
import threading
import time

name = "Brothfish"
author = "Alain Lou"

def processMessages():
    message = input().split()
    print("haha")
    if message[0] == "stop":
        return False
        sys.exit()
    elif message[0] == "uci":
        return True
    else:
        return False

thread1 = threading.Thread(target=processMessages)
thread1.daemon = True
thread1.start()

board = chess.Board()

while True:
    if not processMessages:#right now this only executes once
        print("ok")
        break
