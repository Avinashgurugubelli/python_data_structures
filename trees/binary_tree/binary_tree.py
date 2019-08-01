import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))


from .utils.binary_tree_traversal_types import BinaryTreeTraversalType, BinaryTreeTraversalMethodType
from .traversals.pre_order_traversal import pre_order_traversal_iteration

class BinaryTree:

    def traverse(self, traversalType, traversalMethod, root):
        result = []
        if traversalType == BinaryTreeTraversalType.PRE_ORDER:
            if traversalMethod == BinaryTreeTraversalMethodType.ITERATIVE:
                pre_order_traversal_iteration(root, result)
                print(result)
    
