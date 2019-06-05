import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from queue import Queue

if __name__ == "__main__":
    q = Queue(7)
    for i in range(6):
        q.enqueue(i)
    print("Q elements {}".format(q.get))
    for i in range(9):
        q.dequeue()
    print("Q elements {}".format(q.get))