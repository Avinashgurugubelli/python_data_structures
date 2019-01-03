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
                print(str(current_node.data))
                current_node = current_node.next
                if(current_node == self.head):
                    break
    # region insertion
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

     # insert at given position, by default inserts at beginning.
    def add(self, data, position = 0):
        if position > self.get_length or position < 0:
            print('node can not be inserted at the given postion {}, current list length: {}'.format(
                position, self.get_length))
        elif position == 0 or self.head is None:
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
            print('new node with data {} inserted at postion {}, current list length: {}'.format(
                data, position, self.get_length))
            self.print_list()
    # endregion

    # region deletion
    # deletion at beginning
    def __delete_at_beginning(self):
        if self.head is not None:
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            node_data_to_delete = self.head.data # optional for printing purpose
            self.head = self.head.next
            current_node.next = self.head
            print('node with data {} deleted from beginning, current list length: {}'.format(
                node_data_to_delete, self.get_length))
            self.print_list()
        else:
            print('currently list is empty, unable to delete')

    # private method
    def __delete_at_end(self):
        if self.head is not None:
            tail_node = self.get_tail_node
            node_before_tail = self.get_node_at_position(self.get_length-1)
            node_before_tail.next = self.head
            print('node with data {} deleted from end, current list length: {}'.format(
                tail_node.data, self.get_length))
            tail_node = None  # optional
            self.print_list()
        else:
            print('currently list is empty, unable to delete')

    # deletion of node at given position, by default deletes at beginning
    def delete(self, position = 0):
        if self.head is not None:
            if position < 0 or position > self.get_length:
                 print('node can not be deleted at the given postion {}, current list length: {}'.format(
                position, self.get_length))
            elif position == 0:
                self.__delete_at_beginning()
            elif position == self.get_length:
                self.__delete_at_end()
            else:
                postion_before_node = self.get_node_at_position(position-1)
                node_at_position = self.get_node_at_position(position)
                postion_before_node.next = node_at_position.next
                print('node with data {} deleted at postion {}, current list length: {}'.format(
                node_at_position.data, position, self.get_length))
                node_at_position = None # optional
                self.print_list()
    # endregion
