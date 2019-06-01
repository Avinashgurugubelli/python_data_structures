'''
A stack is a simple data structure used for storing data similar to linked list
Defnition: A stack is an ordered list in which insertion and deletion are done at one end (called top).
i.e. the last element inserted is the first element to be deleted (i.e LIFO -> last in first out)
'''

class Stack:
    def __init__(self, size):
        self.__stack = []
        self.__size = size

    @property
    def is_empty(self):
        return len(self.__stack) <= 0

    @property
    def size(self):
        return len(self.__stack)

    @property
    def get(self):
        return self.__stack

    def push(self, item):
        if self.size >= self.__size:
            print('Stack overflow')
        else:
            self.__stack.append(item)
            print('item {}, pushed into stack, current length {}'.format(item, self.size))

    def pop(self):
        if self.size <= 0:
            print('Stack underflow')
            return None
        else:
           return self.__stack.pop()