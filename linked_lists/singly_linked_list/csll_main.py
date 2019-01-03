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
    linked_list_1.add(45,2)
    linked_list_1.add(45647,3)
    # endregion
    #region deletion
    linked_list_1.delete(0)
    linked_list_1.delete(linked_list_1.get_length)
    linked_list_1.delete(linked_list_1.get_length -1)
    #endregion
