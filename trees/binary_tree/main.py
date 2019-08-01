# Below os and sys imports required to match the custom imports
import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from binary_tree_node import BinaryTreeNode
from binary_tree import BinaryTree
from .utils.binary_tree_traversal_types import BinaryTreeTraversalMethodType, BinaryTreeTraversalType

if __name__ == "__main__":
    node1 = BinaryTreeNode(1)
    node1.left = BinaryTreeNode(2)
    node1.right = BinaryTreeNode(3)
    binaryTree = BinaryTree()
    binaryTree.traverse(BinaryTreeTraversalType.PRE_ORDER, BinaryTreeTraversalMethodType.ITERATIVE, node1)