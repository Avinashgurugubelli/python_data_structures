from node import Node

# Linked List class contains a Node object
class LinkedList:
    def __init__(self):
        self.head = Node

    @property
    def get_list_length(self):
        '''
        Algorithm:-
        let us assume that the head points to the first node of the list. to traverse the list we do the following
        1. follow the pointer
        2. count the node as they are traversed
        3. stop when next pointer points to null
        '''
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count

    # this function prints contents of linked list starting from head
    def print_list(self):
        print('list elements:')
        current = self.head
        while current:
            print(current.data)
            current = current.next

    # region node insertion
    # insert node at beginning
    def insert_at_beginning(self, data):
        '''
        Algorithm:
        1. update the next pointer of new node, to point to the current node/head.
        2. update head pointer to point the new node.
        '''
        new_node = Node()
        new_node.data = data
        if self.head.next == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        print('new node with data {} inserted at beginning, current list length: {}'.format(data, self.get_list_length))
        self.print_list()

    # insert node at end
    def insert_at_end(self, data):
        '''
        Algorithm:
        1. new node next pointer points to Null.
        2. last node next pointer points to new node.
        '''
        current_node = self.head
        new_node = Node()
        new_node.data = data
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node
        print('new node with data {} inserted at end, current list length: {}'.format(data, self.get_list_length))
        self.print_list()
    
    # insert node at given position
    def insert_node_at_position(self, position, data):
        '''
        Algorithm:
        1. should not insert the node if position < 0 or postion > current linked list.
        2. if position = 0 insert at beginning.
        3. if position == linked list length insert at end
        4. else, if we want to add an element at positing 3 then we stop at position 2. i.e traverse 2 nodes and insert new node
            - for simplicity assume second node as postion node.
            1. new node next pointer points to the new node of position node (i.e. position node next pointer)
            2. position node next pointer points to new node
        '''
        if position > self.get_list_length or position < 0:
            print('node can not be inserted at the given postion {}, current list length: {}'.format(position, self.get_list_length))
        elif position == 0:
            self.insert_at_beginning(data)
        elif position == self.get_list_length:
            self.insert_at_end(data)
        else:
            new_node = Node()
            new_node.data = data
            current_node = self.head
            counter = 0;
            while counter < position - 1:
                counter += 1
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
            print('new node with data {} inserted at postion {}, current list length: {}'.format(data, position, self.get_list_length))
            self.print_list()
    # endregion node insertion

    #region node deletion
    # delete node at beginning
    def delete_node_at_beginning(self):
        if self.head == None:
            raise ValueError('currently list is empty')
        else:
            node_data_to_delete = self.head.data # for printing purpose
            self.head = self.head.next
            print('node with data {} at beginning deleted, current list length: {}'.format(node_data_to_delete,self.get_list_length))
            self.print_list()
    
    # delete node at end
    def delete_node_at_end(self):
        current_node = self.head
        previous_node = self.head
        node_data_to_delete = self.head.data # for printing purpose
        while current_node.next != None:
            previous_node = current_node
            current_node = current_node.next
        node_data_to_delete = current_node.data
        previous_node.next = None
        print('node with data {} at end deleted, current list length: {}'.format(node_data_to_delete,self.get_list_length))
        self.print_list()
    
    # delete node at postion
    def delete_node_at_position(self, position):
        if position < 0 or position > self.get_list_length:
            raise ValueError('empty list')
        elif position == 0:
            self.delete_node_at_beginning()
        elif position == self.get_list_length:
            self.delete_node_at_end()
        else:
            count = 0
            current_node = self.head
            previous_node = self.head
            while current_node.next != None and count < position:
                count += 1
                previous_node = current_node
                current_node = current_node.next
            previous_node.next = current_node.next
            print('node with data {} at position {} deleted, current list length: {}'.format(current_node.data, position, self.get_list_length))
            self.print_list()
    #endregion node deletion
        