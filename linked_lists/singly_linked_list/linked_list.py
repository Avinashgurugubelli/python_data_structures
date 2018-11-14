from node import Node

# Linked List class contains a Node object
class LinkedList:
    def __init__(self):
        self.head = Node

    '''
      this function takes linked list as an input and counts the number of nodes in the list
      Algorithm:-
      let us assume that the head points to the first node of the list. to traverse the list we do the following
      1. Follow the pointer
      2. count the node as they are traversed
      3. stop when next pointer points to null
      '''
    def get_list_length(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count

    # This function prints contents of linked list starting from head
    def print_list(self):
        print('list elements:')
        current = self.head
        while current:
            print(current.data)
            current = current.next

    # Insert node at beginning
    def insert_at_beginning(self, data):
        new_node = Node()
        new_node.data = data
        if self.head.next == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        print('new node with data {} inserted at beginning'.format(data))
        self.print_list()

    # Insert node at end
    def insert_at_end(self, data):
        current_node = self.head
        new_node = Node()
        new_node.data = data
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node
        print('new node with data {} inserted at end'.format(data))
        self.print_list()

        