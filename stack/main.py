
# Below os and sys imports required to match the custom imports
import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from stack import Stack;

if __name__ == "__main__":
    s1 = Stack(15)
    s1.pop() # expect underflow error
    for item in range(10):
        s1.push(str(item))
    print("size of the stack is {}".format(s1.size))
    print("list of elements in stack {}".format(s1.get))
    for item in range(13):
        print("pop out element: {}".format(s1.pop()))
        
