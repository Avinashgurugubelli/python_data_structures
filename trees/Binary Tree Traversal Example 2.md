# Binary Tree Traversal: Recursive and Iterative Methods with Stack Visualizations

## Tree Structure Used

```
              1
           /     \
         2         3
       /   \     /   \
     4      5   6     7
    / \    /        / \
   8   9 10       14  15
          \
          11
```

## Python Code to Build Tree

```python
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Constructing the tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right.left = Node(10)
root.left.right.left.right = Node(11)
root.right.right.left = Node(14)
root.right.right.right = Node(15)
```

---

## Inorder Traversal (Left → Root → Right)

### Recursive

```python
def inorder_recursive(node):
    if node:
        inorder_recursive(node.left)
        print(node.key, end=" ")
        inorder_recursive(node.right)
```

**Recursion Visualization:**

```
inorder(1)
├── inorder(2)
│   ├── inorder(4)
│   │   ├── inorder(8)
│   │   └── inorder(9)
│   └── inorder(5)
│       └── inorder(10)
│           └── inorder(11)
├── print(1)
└── inorder(3)
    ├── inorder(6)
    └── inorder(7)
        ├── inorder(14)
        └── inorder(15)
```

### Iterative

```python
def inorder_iterative(root):
    stack = []
    current = root
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        print(current.key, end=" ")
        current = current.right
```

**Stack Visualization:**

```
Stack push: 1 → 2 → 4 → 8
Pop 8 → print → move to right
Pop 4 → print → push 9
Pop 9 → print → move to parent
...
```

---

## Preorder Traversal (Root → Left → Right)

### Recursive

```python
def preorder_recursive(node):
    if node:
        print(node.key, end=" ")
        preorder_recursive(node.left)
        preorder_recursive(node.right)
```

**Recursion Visualization:**

```
preorder(1)
├── print(1)
├── preorder(2)
│   ├── print(2)
│   ├── preorder(4)
│   │   ├── print(4)
│   │   ├── preorder(8)
│   │   └── preorder(9)
│   └── preorder(5)
│       ├── print(5)
│       └── preorder(10)
│           ├── print(10)
│           └── preorder(11)
├── preorder(3)
    ├── print(3)
    ├── preorder(6)
    └── preorder(7)
        ├── preorder(14)
        └── preorder(15)
```

### Iterative

```python
def preorder_iterative(root):
    if not root:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.key, end=" ")
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
```

**Stack Visualization:**

```
Start: [1]
Pop 1 → print → push 3, 2
Pop 2 → print → push 5, 4
Pop 4 → print → push 9, 8
Pop 8 → print
Pop 9 → print
...
```

---

## Postorder Traversal (Left → Right → Root)

### Recursive

```python
def postorder_recursive(node):
    if node:
        postorder_recursive(node.left)
        postorder_recursive(node.right)
        print(node.key, end=" ")
```

**Recursion Visualization:**

```
postorder(1)
├── postorder(2)
│   ├── postorder(4)
│   │   ├── postorder(8)
│   │   └── postorder(9)
│   └── postorder(5)
│       └── postorder(10)
│           └── postorder(11)
├── postorder(3)
│   ├── postorder(6)
│   └── postorder(7)
│       ├── postorder(14)
│       └── postorder(15)
└── print(1)
```

### Iterative (Two Stacks)

```python
def postorder_iterative(root):
    if not root:
        return
    stack1 = [root]
    stack2 = []
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    while stack2:
        print(stack2.pop().key, end=" ")
```

**Stack Visualization:**

```
stack1: [1]
Pop 1 → push to stack2 → push 2, 3 to stack1
Pop 3 → push to stack2 → push 6, 7
Pop 7 → push to stack2 → push 14, 15
...
After stack1 is empty → pop from stack2 and print
```

---

## Final Output for Verification

| Traversal Type | Expected Output                 |
| -------------- | ------------------------------- |
| Inorder        | `8 4 9 2 10 11 5 1 6 3 14 7 15` |
| Preorder       | `1 2 4 8 9 5 10 11 3 6 7 14 15` |
| Postorder      | `8 9 4 11 10 5 2 6 14 15 7 3 1` |
