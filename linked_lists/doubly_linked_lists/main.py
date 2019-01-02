from dl_node import DLNode
from doubly_linked_list import DoublyLinkedList

if __name__ == "__main__":
    # Node creation
    node_1, node_2, node_3 = DLNode(), DLNode(), DLNode()
    # Node data assignment
    node_1.data = 5
    node_2.data = 12
    node_3.data = 34
    # assigning nodes to double linked list
    lst_1 = DoublyLinkedList()
    lst_1.head = node_1
    lst_1.head.next = node_2
    node_2.previous = lst_1.head
    node_2.next = node_3
    node_3.previous = node_2
    # lst_1.print_list() # printing double link list
    # Insertion at begining
    lst_1.insertion_at_begining(78)
    lst_1.insertion_at_end(89)
    lst_1.insertion_at_position(-1, 45)
    lst_1.insertion_at_position(2, 105)
    lst_1.insertion_at_position(4, 4)
    # removal
    lst_1.delete_at_postion(-1)
    lst_1.delete_at_postion(1)
    lst_1.delete_at_postion(2)
    lst_1.delete_at_postion(lst_1.get_length())
    # lst_1.print_list()