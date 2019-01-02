from node import Node


class CircularSinglyLinkedList:

    def __init__(self):
        self.head = None
        self.__length = 0

    @property
    def get_length(self):
        self.__length = 0
        current_node = self.head
        if self.head is not None:
            while (True):
                self.__length += 1
                current_node = current_node.next
                if current_node == self.head:
                    break
        return self.__length

    def print_list(self):
        if self.head is not None:
            current_node = self.head
            while(True):
                print(str(current_node.data))
                current_node = current_node.next
                if(current_node == self.head):
                    break

    # insert_at_beginning
    def push(self, data):
        new_node = Node()
        new_node.data = data
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            new_node.next = self.head
            self.head = new_node
            current_node.next = self.head
        print('new node with data {} inserted at beginning, current list length: {}'.format(
            data, self.get_length))
        self.print_list()

    # insert_at_end
    def append(self, data):
        new_node = Node()
        new_node.data = data
        if self.head is not None:
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            new_node.next = self.head
            current_node.next = new_node
            print('new node with data {} inserted at end, current list length: {}'.format(
                data, self.get_length))
            self.print_list()
        else:
            self.push(data)

    def insert_at_position(self, data, position):
        if position > self.get_length or position < 0:
            print('node can not be inserted at the given postion {}, current list length: {}'.format(
                position, self.get_length))
        elif position == 0:
            self.push(data)
        elif position == self.get_length:
            self.append(data)
        else:
            new_node = Node()
            new_node.data = data
            counter = 1
            current_node = self.head
            while current_node.next != self.head and counter < position - 1:
                counter += 1
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
            print('new node with data {} inserted at postion {}, current list length: {}'.format(data, position, self.get_length))
            self.print_list() 
