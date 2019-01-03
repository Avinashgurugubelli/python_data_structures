'''
module cdll_main

main file for executing the Circular Doubly Linked List operations
'''
from circular_doubly_linked_list import CircularDoublyLinkedList
if __name__ == "__main__":
    list1 = CircularDoublyLinkedList()
    list1.push(1)
    list1.push(2)
    list1.push(3)
    list1.push(4)
    list1.append(5)
    list1.append(6)
    list1.add(45)
    list1.add(123, 0)
    list1.add(34, list1.get_length)
    list1.delete_at_end()
    list1.delete()
    list1.delete(4)
    list1.delete(list1.get_length+34)
