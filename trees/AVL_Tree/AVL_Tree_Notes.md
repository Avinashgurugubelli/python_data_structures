
# 🌳 AVL Tree Complete Notes

## Table of Contents
1. [Introduction](#introduction)
2. [AVL Tree Basics](#avl-tree-basics)
3. [Rotations](#rotations)
4. [Insertion](#insertion)
5. [Deletion](#deletion)
6. [Recursive Dry-Run Visualization](#recursive-dry-run-visualization)
7. [Full Tree Example](#full-tree-example)

---

## Introduction
AVL Tree is a self-balancing Binary Search Tree (BST) where the difference between heights of left and right subtrees cannot be more than one for all nodes.

---

## AVL Tree Basics

- **Height** of a node is the number of edges on the longest path from that node to a leaf.
- **Balance Factor (BF)** = Height of Left Subtree - Height of Right Subtree
- **Balanced Condition**: -1 <= BF <= 1

---

## Rotations

### 1. Left Rotation (RR Case)
```
    x
     \
      y
       \
        z
```
Becomes:
```
    y
   / \
  x   z
```

### 2. Right Rotation (LL Case)
```
      z
     /
    y
   /
  x
```
Becomes:
```
    y
   / \
  x   z
```

### 3. Left-Right Rotation (LR Case)
```
    z
   /
  x
   \
    y
```
Becomes:
```
    y
   / \
  x   z
```

### 4. Right-Left Rotation (RL Case)
```
  x
   \
    z
   /
  y
```
Becomes:
```
    y
   / \
  x   z
```

---

## Insertion

- Insert like in a normal BST.
- Update the height of ancestor nodes.
- Rebalance the tree if the balance factor is violated.

---

## Deletion

1. Perform standard BST delete.
2. Update heights.
3. Rebalance using the same four rotation cases.

---

## Recursive Dry-Run Visualization

### Insert 10 → 20 → 30

#### 1. Insert 10
```
Call insert(root=None, key=10)
→ returns Node(10)
```

#### 2. Insert 20
```
insert(root=10, key=20)
→ root.right = insert(None, 20) → Node(20)
→ height(10) = 1 + max(0, 1) = 2
→ balance = -1 (OK)
```

#### 3. Insert 30
```
insert(root=10, key=30)
→ root.right = insert(20, 30)
→ height updates...
→ balance = -2 → RR → leftRotate(10)
```

Tree becomes:
```
   20
  /  \
10   30
```

---

## Full Tree Example

### Insert sequence:
```
[50, 30, 70, 20, 40, 60, 80, 10, 35, 45, 55, 65]
```

Final Balanced Tree:
```
         30
       /    \
     20      60
    /      /    \
  10     50      70
         /  \    /  \
       40   55  65  80
      /  \
    35   45
```

---

## Python Code

### Node + AVL Tree with Insertion and Deletion

```python
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        # Left Left Case (LL) - Perform right rotation
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # Right Right Case (RR) - Perform left rotation
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # Left Right Case (LR) - Perform left rotation on left child, then right rotation on root
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left Case (RL) - Perform right rotation on right child, then left rotation on root
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)


        return root

    def delete(self, root, key):
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        # Left Left Case (LL) after deletion
        # The balance is > 1, and the left child has balance >= 0, meaning
        # the heavier subtree is still on the left side — single right rotation needed
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        # Right Right Case (RR) after deletion
        # The balance is < -1, and the right child has balance <= 0, meaning
        # the heavier subtree is still on the right side — single left rotation needed
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        # Left Right Case (LR) after deletion
        # The balance is > 1, but the left child has balance < 0, meaning
        # the subtree is left-heavy but unbalanced — perform left rotation on left child
        # then right rotation on root
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left Case (RL) after deletion
        # The balance is < -1, but the right child has balance > 0, meaning
        # the subtree is right-heavy but unbalanced — perform right rotation on right child
        # then left rotation on root
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)


        return root

    def get_min_value_node(self, node):
        while node.left:
            node = node.left
        return node

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y
```

---

## ✅ Summary

- AVL Trees balance themselves using rotations.
- Keep height and balance factor updated.
- Use recursive dry runs to understand insertion/deletion.


## ✅ Time Complexity Summary

| Operation | Time Complexity |
|-----------|-----------------|
| Insert    | O(log n)        |
| Delete    | O(log n)        |
| Search    | O(log n)        |

AVL Tree guarantees `O(log n)` for search, insertion, and deletion due to self-balancing.