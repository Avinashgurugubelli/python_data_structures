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
        
