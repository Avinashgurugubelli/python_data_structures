
# 🌲 Iterative Tree Traversals with Full Stack Visualization

This document provides **iterative traversal algorithms** for binary trees along with **step-by-step stack visualizations** to deepen understanding.

---

## 🌳 Example Tree Structure

```
       A
     /   \
    B     C
   / \   / \
  D   E F   G
```

Each node is labeled with a capital letter. We'll use this tree for all examples.

---

## 🔁 Preorder Traversal (Node → Left → Right)

### 🧠 Algorithm

1. Initialize stack with root.
2. Pop node, visit it.
3. Push **right**, then **left** (so left is processed first).

### 🧪 Python Code

```python
def preorder_iterative(root):
    if root is None:
        return
    
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.val, end=' ')
        
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
```

### 📦 Stack Visualization

| Step | Action            | Stack          | Output |
|------|-------------------|----------------|--------|
| 1    | Push A            | [A]            |        |
| 2    | Pop A, visit      | []             | A      |
| 3    | Push C, B         | [C, B]         | A      |
| 4    | Pop B, visit      | [C]            | A B    |
| 5    | Push E, D         | [C, E, D]      | A B    |
| 6    | Pop D, visit      | [C, E]         | A B D  |
| 7    | Pop E, visit      | [C]            | A B D E|
| 8    | Pop C, visit      | []             | A B D E C|
| 9    | Push G, F         | [G, F]         | A B D E C|
| 10   | Pop F, visit      | [G]            | A B D E C F|
| 11   | Pop G, visit      | []             | A B D E C F G|

### ✅ Output
```
A B D E C F G
```

---

## 🔁 Inorder Traversal (Left → Node → Right)

### 🧠 Algorithm

1. Go left, push nodes on stack.
2. When null, pop, visit.
3. Move to right.

### 🧪 Python Code

```python
def inorder_iterative(root):
    stack = []
    current = root
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        print(current.val, end=' ')
        current = current.right
```

### 📦 Stack Visualization

| Step | Action                | Stack           | Output |
|------|-----------------------|------------------|--------|
| 1    | Go left A → B → D     | [A, B, D]        |        |
| 2    | Pop D, visit          | [A, B]           | D      |
| 3    | Pop B, visit          | [A]              | D B    |
| 4    | Move to E, push       | [A, E]           | D B    |
| 5    | Pop E, visit          | [A]              | D B E  |
| 6    | Pop A, visit          | []               | D B E A|
| 7    | Move to C → F         | [C, F]           | D B E A|
| 8    | Pop F, visit          | [C]              | D B E A F|
| 9    | Pop C, visit          | []               | D B E A F C|
| 10   | Move to G, push       | [G]              | D B E A F C|
| 11   | Pop G, visit          | []               | D B E A F C G|

### ✅ Output
```
D B E A F C G
```

---

## 🔁 Postorder Traversal (Left → Right → Node)

### 🧠 Algorithm (Two Stack)

1. Push root to `stack1`.
2. Pop from `stack1`, push to `stack2`.
3. Push left and right to `stack1`.
4. Pop all from `stack2` to visit in postorder.

### 🧪 Python Code

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
        print(stack2.pop().val, end=' ')
```

### 📦 Stack Visualization

| Step | Action                    | stack1        | stack2         |
|------|---------------------------|---------------|----------------|
| 1    | Push A                    | [A]           | []             |
| 2    | Pop A → stack2, push B C  | [C, B]        | [A]            |
| 3    | Pop B → stack2, push D E  | [C, E, D]     | [A, B]         |
| 4    | Pop D → stack2            | [C, E]        | [A, B, D]      |
| 5    | Pop E → stack2            | [C]           | [A, B, D, E]   |
| 6    | Pop C → stack2, push F G  | [G, F]        | [A, B, D, E, C]|
| 7    | Pop F → stack2            | [G]           | [A, B, D, E, C, F]|
| 8    | Pop G → stack2            | []            | [A, B, D, E, C, F, G]|

Now pop from `stack2` for output:
```
D E B F G C A
```

---

## ✅ Final Outputs

| Traversal  | Output         |
|------------|----------------|
| Preorder   | A B D E C F G  |
| Inorder    | D B E A F C G  |
| Postorder  | D E B F G C A  |

---

