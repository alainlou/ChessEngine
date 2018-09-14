import chess
import sys
import threading
import time

name = "Brothfish"
author = "Alain Lou"

def wait():
    while True:
        time.sleep(2)
        print("going")

def exit():
    print("stopped")

thread1 = threading.Thread(target=wait)
thread1.daemon = True
thread1.start()

board = chess.Board()

while True:
    if input() == "stop":
        exit()
        sys.exit()
        break
    else:
        print("continuing")
