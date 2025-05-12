
# Understanding Tree Traversal Recursion Trees

This article walks through the recursion tree visualizations for **preorder**, **inorder**, and **postorder** traversals using a common binary tree example.

---

## 📌 Example Binary Tree

```
       A
     /   \  
    B     C
   / \   / \
  D   E F   G
```

---

## 🔁 Preorder Traversal

### 🔍 Logic:
```python
def preorder(node):
    if node:
        print(node.val)
        preorder(node.left)
        preorder(node.right)
```

### 🌳 Recursion Tree:
```
preorder(A)
├── preorder(B)
│   ├── preorder(D)
│   │   ├── preorder(None)
│   │   └── preorder(None)
│   └── preorder(E)
│       ├── preorder(None)
│       └── preorder(None)
└── preorder(C)
    ├── preorder(F)
    │   ├── preorder(None)
    │   └── preorder(None)
    └── preorder(G)
        ├── preorder(None)
        └── preorder(None)
```

### ✅ Output:
```
A B D E C F G
```

---

## 🔁 Inorder Traversal

### 🔍 Logic:
```python
def inorder(node):
    if node:
        inorder(node.left)
        print(node.val)
        inorder(node.right)
```

### 🌳 Recursion Tree:
```
inorder(A)
├── inorder(B)
│   ├── inorder(D)
│   │   ├── inorder(None)
│   │   └── print(D)
│   │   └── inorder(None)
│   └── print(B)
│   └── inorder(E)
│       ├── inorder(None)
│       └── print(E)
│       └── inorder(None)
└── print(A)
└── inorder(C)
    ├── inorder(F)
    │   ├── inorder(None)
    │   └── print(F)
    │   └── inorder(None)
    └── print(C)
    └── inorder(G)
        ├── inorder(None)
        └── print(G)
        └── inorder(None)
```

### ✅ Output:
```
D B E A F C G
```

---

## 🔁 Postorder Traversal

### 🔍 Logic:
```python
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.val)
```

### 🌳 Recursion Tree:
```
postorder(A)
├── postorder(B)
│   ├── postorder(D)
│   │   ├── postorder(None)
│   │   ├── postorder(None)
│   │   └── print(D)
│   ├── postorder(E)
│   │   ├── postorder(None)
│   │   ├── postorder(None)
│   │   └── print(E)
│   └── print(B)
├── postorder(C)
│   ├── postorder(F)
│   │   ├── postorder(None)
│   │   ├── postorder(None)
│   │   └── print(F)
│   ├── postorder(G)
│   │   ├── postorder(None)
│   │   ├── postorder(None)
│   │   └── print(G)
│   └── print(C)
└── print(A)
```

### ✅ Output:
```
D E B F G C A
```

---

## 📝 Summary

| Traversal  | Order                          | Output           |
|------------|--------------------------------|------------------|
| Preorder   | Node → Left → Right            | A B D E C F G    |
| Inorder    | Left → Node → Right            | D B E A F C G    |
| Postorder  | Left → Right → Node            | D E B F G C A    |

