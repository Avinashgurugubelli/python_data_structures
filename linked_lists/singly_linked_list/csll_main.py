'''
module csll_main

main file for executing the Circular Singly Linked List operations
'''

from node import Node
from circular_singly_linked_list import CircularSinglyLinkedList

if __name__ == "__main__":
     # Start with the empty list
    linked_list_1 = CircularSinglyLinkedList()
    # region nodes creation
    # endregion
    # region assigning nodes to circular singly linked list
    linked_list_1.push(1)
    linked_list_1.push(2)
    linked_list_1.push(3)
    linked_list_1.push(4)
    linked_list_1.append(6)
    linked_list_1.insert_at_position(45,2)
    linked_list_1.insert_at_position(45647,3)
    # linked_list_1.push(36)
    # endregion