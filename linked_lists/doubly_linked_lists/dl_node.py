# Node of a doubly linked list
class DLNode:
    # constructor
    def __init__(self):
        self.__data = None
        self.__next = None
        self.__previous = None
    # method for getting data field of the node
    @property
    def data(self):
        return self.__data
    # method for getting next files of the node
    @property
    def next(self):
        return self.__next
    # method for getting previous files of the node
    @property
    def previous(self):
        return self.__previous
    # method for setting data field of the node
    @data.setter
    def data(self, data):
        self.__data = data
    # method for setting next field of the node
    @next.setter
    def next(self, next):
        self.__next = next
    # method for setting next field of the node
    @previous.setter
    def previous(self, previous):
        self.__previous = previous
    # returns true if node points to the another node and vise versa
    @property
    def has_next(self):
        return self.__next != None
     # returns true if node points to the another node and vise versa
    def has_previous(self):
        return self.__next != None
