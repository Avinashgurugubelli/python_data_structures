# Node of a singly linked list
class Node:
    # constructor
    def __init__(self):
        self.__data = None
        self.__next = None
    # method for getting data field of the node
    @property
    def data(self):
        return self.__data
    # method for getting next files of the node
    @property
    def next(self):
        return self.__next
    # method for setting data field of the node
    @data.setter
    def data(self, data):
        self.__data = data
    # method for setting next field of the node
    @next.setter
    def next(self, next):
        self.__next = next
    # returns true if node points to the another node and vise versa
    def has_node(self):
        return self.__next != None
