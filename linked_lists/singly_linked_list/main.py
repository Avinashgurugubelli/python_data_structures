from linked_list import LinkedList
from node import Node

# Code execution starts here
if __name__ == '__main__':
    # Start with the empty list
    linked_list_1 = LinkedList()
    # region nodes creation
    first_node, second_node, third_node = Node(), Node(), Node()
    first_node.data = 5
    second_node.data = 10
    third_node.data = 36
    # endregion

    # region assigning nodes to linked list
    linked_list_1.head = first_node
    '''
        Three nodes have been created.
        We have references to these three blocks as first,
        second and third

        linked_list_1.head   second_node   third_node
             |                |                  |
             |                |                  |
        +----+------+     +----+------+     +----+------+
        | 5  | None |     | 10  | None |     |  36 | None |
        +----+------+     +----+------+     +----+------+
        '''
    linked_list_1.head.next = second_node # Link first node with second
    '''
        Now next of first Node refers to second.  So they
        both are linked.

        linked_list_1.head        second_node              third_node
             |                |                  |
             |                |                  |
        +----+------+     +----+------+     +----+------+
        | 5  |  o-------->| 10  | null |     |  36 | null |
        +----+------+     +----+------+     +----+------+
    '''
    second_node.next = third_node  # Link second node with the third node
    '''
    Now next of second Node refers to third.  So all three
    nodes are linked.

    linked_list_1.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 5  |  o-------->| 10  |  o-------->|  36 | null |
    +----+------+     +----+------+     +----+------+
    '''
    lst_Length = linked_list_1.get_list_length
    print('length of linked List: '+ str(lst_Length))
    linked_list_1.print_list()
    # endregion

    # region Node insertion
    linked_list_1.insert_node_at_position(0, 112) # Insertion at beginning
    linked_list_1.insert_node_at_position(linked_list_1.get_list_length, 236) # Insertion at end
    linked_list_1.insert_node_at_position(3, 99)
    # endregion
    # region node deletion
    linked_list_1.delete_node_at_beginning()
    linked_list_1.delete_node_at_end()
    # end region