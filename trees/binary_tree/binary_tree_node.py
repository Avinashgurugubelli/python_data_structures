class BinaryTreeNode:
    def __init__(self, data):
        self.__data = data
        self.__left = None
        self.__right = None
    
    # getter for data
    @property
    def data(self):
        return self.__data
    
    @property
    def left(self):
        return self.__left
    
    @property
    def right(self):
        return self.__right
    
    @data.setter
    def data(self, data):
        self.__data = data
    
    @left.setter
    def left(self, left):
        self.__left = left
    
    def right(self, right):
        self.__right = right