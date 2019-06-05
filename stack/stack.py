'''
A stack is a simple data structure used for storing data similar to linked list
Defnition: A stack is an ordered list in which insertion and deletion are done at one end (called top).
i.e. the last element inserted is the first element to be deleted (i.e LIFO -> last in first out)
'''
from utils.logger import Logger as log

class Stack:
    def __init__(self, limit):
        self.__stack = []
        self.__limit = limit

    # Stack is empty when stack size is 0
    @property
    def is_empty(self):
        return len(self.__stack) <= 0

    # return the size of the stack
    @property
    def size(self):
        return len(self.__stack)

    # getter for stack elements
    @property
    def get(self):
        return self.__stack

    # Function to add an item to stack. It increases size by 1
    def push(self, item):
        if self.size >= self.__limit:
            log.error('Stack overflow')
        else:
            self.__stack.append(item)
            log.success('item {}, pushed to stack, current length {}'.format(item, self.size))

    # Function to remove an item from stack. It decreases size by 1
    def pop(self):
        if self.is_empty:
            log.error('Stack underflow')
            return None
        else:
           return self.__stack.pop()
