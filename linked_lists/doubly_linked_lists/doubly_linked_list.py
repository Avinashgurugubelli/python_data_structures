from dl_node import DLNode


class DoublyLinkedList:
    def __init__(self):
        self.head = DLNode
    # print list

    def print_list(self):
        current_node = self.head
        while current_node != None:
            print(str(current_node.data))
            current_node = current_node.next

    def get_length(self):
        counter = 0
        current_node = self.head
        while current_node != None:
            counter += 1
            current_node = current_node.next
        return counter

    # region insertion
    def insertion_at_begining(self, node_data):
        new_node = DLNode()
        new_node.data = node_data
        if self.head.next == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        self.print_list()

    def insertion_at_end(self, data):
        new_node = DLNode()
        new_node.data = data
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node
        new_node.previous = current_node
        print('node with data {} inserted at end'.format(data))
        self.print_list()

    def insertion_at_position(self, position, data):
        current_node = self.head
        new_node = DLNode()
        new_node.data = data
        if position < 0 or position > self.get_length():
            print('invalid position')
            return
        elif position == 0:
            self.insertion_at_begining(data)
        elif position == self.get_length():
            self.insertion_at_end(data)
        else:
            counter = 1
            while current_node != None and counter < position - 1:
                current_node = current_node.next
                counter += 1
            new_node.next = current_node.next
            new_node.previous = current_node
            current_node.next = new_node
            print('node with data {} at position {} inserted, current list length: {}'.format(
                data, position, self.get_length()))
            self.print_list()
        # endregion insertion

    # region deletion
    def delete_at_begining(self):
        if self.head == None:
            raise ValueError('currently list is empty')
        else:
            current_node = self.head
            self.head = current_node.next
            print('node with data {} deleted at begining, current list length: {}'.format(
                current_node.data, self.get_length()))
            self.print_list()

    def delete_at_end(self):
        if self.head == None:
            raise ValueError('currently list is empty')
        else:
            counter = 1
            list_length = self.get_length()
            current_node = self.head
            while current_node != None and counter < list_length:
                if counter == list_length-1:
                    deleted_node = current_node.next
                    current_node.next = None
                    print('node with data {} deleted at end, current list length: {}'.format(
                        deleted_node.data, self.get_length()))
                    self.print_list()
                    return
                else:
                    counter += 1
                    current_node = current_node.next

    def delete_at_postion(self, position):
        if position <= 0 or position > self.get_length():
            print('invalid postion {}, position should be positive number and less than the list length to delete'.format(position))
        elif position == 1:
            self.delete_at_begining()
        elif position == self.get_length():
            self.delete_at_end()
        else:
            current_node = self.head
            previous_node = current_node
            counter = 1
            while current_node != None and counter <= position:
                if counter == position:
                    previous_node.next = current_node.next
                    print('node with data {} deleted at position {}, current list length: {}'.format(
                        current_node.data, position, self.get_length()))
                    self.print_list()
                    return
                else:
                    counter += 1
                    previous_node = current_node
                    current_node = current_node.next

            # endregion deletion
