
from dl_node import DLNode
from colorama import Fore, Back, Style, init as coloramaInit
coloramaInit()


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.__length = 0
        self.__tail = None

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

    @property
    def get_tail_node(self):
        current_node = self.head
        if self.head is not None:
            while current_node.next != self.head:
                current_node = current_node.next
        return current_node

    def get_node_at_position(self, position):
        current_node = self.head
        if position == self.get_length:
            return self.get_tail_node
        else:
            counter = 0
            while current_node.next != self.head and counter < position-1:
                counter += 1
                current_node = current_node.next
        return current_node

    def print_list(self):
        if self.head is not None:
            current_node = self.head
            while(True):
                print(Fore.MAGENTA + str(current_node.data))
                current_node = current_node.next
                if(current_node == self.head):
                    break

    # region insertion
    # insert_at_beginning
    def push(self, data):
        new_node = DLNode()
        new_node.data = data
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
        else:
            tail_node = self.get_tail_node
            new_node.next = self.head
            self.head = new_node
            tail_node.next = self.head
        print(Fore.GREEN + 'new node with data {} inserted at beginning, current list length: {}'.format(
            data, self.get_length))
        self.print_list()

    # insert at end
    def append(self, data):
        if self.head is None:
            self.push(data)
        else:
            new_node = DLNode()
            new_node.data = data
            tail_node = self.get_tail_node
            tail_node.next = new_node
            new_node.previous = tail_node
            new_node.next = self.head
            print(Fore.GREEN + 'new node with data {} inserted at end, current list length: {}'.format(
                data, self.get_length))
            self.print_list()

    # insert at given position, by default inserts at beginning.
    def add(self, data, position=0):
        if position < 0 or position > self.get_length:
            print(Fore.RED + 'node can not be inserted at the given postion {}, current list length: {}'.format(
                position, self.get_length))
        elif position == 0 or self.head is None:
            self.push(data)
        elif position == self.get_length:
            self.append(data)
        else:
            new_node = DLNode()
            new_node.data = data
            node_before_position = self.get_node_at_position(position-1)
            node_at_position = self.get_node_at_position(position)
            new_node.previous = node_before_position
            new_node.next = node_at_position
            node_before_position.next = new_node
            print(Fore.GREEN + 'new node with data {} inserted at postion {}, current list length: {}'.format(
                data, position, self.get_length))
            self.print_list()

    # endregion

    # region deletion
    def delete_at_beginning(self):
        if self.head is not None:
            tail_node = self.get_tail_node
            node_data_to_delete = self.head.data  # optional for printing purpose
            self.head = self.head.next
            tail_node.next = self.head
            print(Fore.GREEN + 'node with data {} deleted at begining, current list length: {}'.format(
                node_data_to_delete, self.get_length))
            self.print_list()
        else:
            print(
                Fore.RED + 'currently list is empty, deletion operation can\'t be performed')

    def delete_at_end(self):
        if self.head is not None:
            tail_node = self.get_tail_node
            node_before_tail = self.get_node_at_position(self.get_length-1)
            node_before_tail.next = self.head
            print(Fore.GREEN + 'node with data {} deleted at end, current list length: {}'.format(
                tail_node.data, self.get_length))
            self.print_list()
            tail_node = None # optional
        else:
            print(Fore.RED + 'currently list is empty, deletion operation can\'t be performed')


    def delete(self, position = 0):
        if position > self.get_length or position < 0:
            print(Fore.RED +'node can not be deleted at the given postion {}, current list length: {}'.format(position, self.get_length))
        elif position == 0 or self.head is None:
            self.delete_at_beginning()
        elif position == self.get_length:
            self.delete_at_end()
        else:
            node_at_position = self.get_node_at_position(position)
            position_before_node = self.get_node_at_position(position -1)
            position_before_node.next = node_at_position.next
            print(Fore.GREEN+ 'node with data {} deleted at postion {}, current list length: {}'.format(
                node_at_position.data, position, self.get_length))
            node_at_position = None # optional
            self.print_list()
            

    # endregion
