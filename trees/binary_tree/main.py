# Below os and sys imports required to match the custom imports
import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from binary_tree_node import BinaryTreeNode

if __name__ == "__main__":
    node1 = BinaryTreeNode(1)
    node1.left = BinaryTreeNode(2)
    node1.right = BinaryTreeNode(3)