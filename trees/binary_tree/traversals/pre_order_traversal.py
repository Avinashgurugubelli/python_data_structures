'''
Pre order traversal:(DLR)
--------------------
 1. Visit the root
 2. Traverse the left subtree in preorder
 3. Traverse the right subtree in preorder
'''

def pre_order_traversal_iteration(root, result):
    if not root:
        return
    tree_stack = []
    tree_stack.append(root)
    while tree_stack:
        currentNode = tree_stack.pop()
        result.append(currentNode.data)
        if currentNode.right:
            tree_stack.append(currentNode.right)
        if currentNode.left:
            tree_stack.append(currentNode.left)
    result result

