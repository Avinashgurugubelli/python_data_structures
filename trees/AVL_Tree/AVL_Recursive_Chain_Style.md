
# 🔁 AVL Tree Recursive Dry Run (Chain Style)

## 🧩 Step-by-Step Recursive Calls for Insert Sequence:
```
[50, 30, 70, 20, 40, 60, 80, 10, 35, 45, 55, 65]
```

---

### Insert 50
```
insert(root=None, key=50)
→ root is None → create Node(50)
```

### Insert 30
```
insert(50, 30)
→ key < 50 → insert(30 in left subtree)
    insert(None, 30) → create Node(30)
← back to 50: update height = 2, balance = 1 → OK
```

### Insert 70
```
insert(50, 70)
→ key > 50 → insert(70 in right subtree)
    insert(None, 70) → create Node(70)
← back to 50: update height = 2, balance = 0 → OK
```

### Insert 20
```
insert(50, 20)
→ left
    insert(30, 20)
    → left
        insert(None, 20) → Node(20)
    ← 30: height = 2, balance = 1
← 50: height = 3, balance = 1 → OK
```

### Insert 40
```
insert(50, 40)
→ left
    insert(30, 40)
    → right
        insert(None, 40) → Node(40)
    ← 30: height = 2, balance = 0
← 50: height = 3, balance = 1 → OK
```

### Insert 60
```
insert(50, 60)
→ right
    insert(70, 60)
    → left
        insert(None, 60) → Node(60)
    ← 70: height = 2, balance = 1
← 50: height = 3, balance = 0 → OK
```

### Insert 80
```
insert(50, 80)
→ right
    insert(70, 80)
    → right
        insert(None, 80) → Node(80)
    ← 70: height = 2, balance = 0
← 50: height = 3, balance = 0 → OK
```

### Insert 10 (Triggers Left-Left imbalance)
```
insert(50, 10)
→ left
    insert(30, 10)
    → left
        insert(20, 10)
        → left
            insert(None, 10) → Node(10)
        ← 20: height = 2, balance = 1
    ← 30: height = 3, balance = 1
← 50: height = 4, balance = 2 → 🚨 unbalanced

➡ Left-Left case → rightRotate(50)
New subtree root = 30
```

### Insert 35
```
insert(30, 35)
→ right
    insert(50, 35)
    → left
        insert(40, 35)
        → left
            insert(None, 35) → Node(35)
        ← 40: height = 2, balance = 1
    ← 50: height = 3, balance = 1
← 30: height = 4, balance = 0 → OK
```

### Insert 45 (Triggers Left-Right imbalance)
```
insert(30, 45)
→ right
    insert(50, 45)
    → left
        insert(40, 45)
        → right
            insert(None, 45) → Node(45)
        ← 40: height = 2, balance = 0
    ← 50: height = 3, balance = 2 → 🚨 unbalanced

➡ Left-Right case → leftRotate(40) → rightRotate(50)
New subtree root = 45
```

### Insert 55
```
insert(30, 55)
→ right
    insert(45, 55)
    → right
        insert(50, 55)
        → right
            insert(None, 55) → Node(55)
        ← 50: height = 2, balance = -1
    ← 45: height = 3, balance = -1
← 30: height = 4, balance = -1 → OK
```

### Insert 65 (Triggers Right-Left imbalance)
```
insert(30, 65)
→ right
    insert(45, 65)
    → right
        insert(50, 65)
        → right
            insert(70, 65)
            → left
                insert(60, 65)
                → right
                    insert(None, 65) → Node(65)
                ← 60: height = 2, balance = -1
            ← 70: height = 3, balance = 1
        ← 50: height = 4, balance = -2 → 🚨 unbalanced

➡ Right-Left case → rightRotate(70), leftRotate(50)
New subtree root = 60
```

---

## ✅ Final Balanced AVL Tree

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


## AVL Tree Deletion — Recursive Chain Dry-Run

- Insertion sequence: [50, 30, 70, 20, 40, 60, 80, 10, 35, 45, 55, 65]

- Deletion Sequence: [10, 20, 40, 60]


### ❌ Delete 10 — No Rebalance

```
delete(50, 10)
→ left
  delete(30, 10)
  → left
    delete(20, 10)
    → left
      delete(10, 10)
      → match found → no children → return None
    ← back to 20: height = 1, balance = 0 → OK
  ← back to 30: height = 3, balance = 1 → OK
← back to 50: height = 4, balance = 1 → OK

```

✅ No rebalancing needed.


### ❌ Delete 20 — Rebalance Required (Right Rotation)

```
delete(50, 20)
→ left
  delete(30, 20)
  → left
    delete(20, 20)
    → match found → no children → return None
  ← back to 30: height = 2, balance = 0
← back to 50: height = 4, balance = 2 → 🚨 Unbalanced

→ Balance(50) = 2 (left-heavy)
→ Balance(30) = 0 → 🔁 Left-Left Case

➡ Perform rightRotate(50)
→ New root = 30

```
✅ Right rotation fixes imbalance


### ❌ Delete 40 — No Rebalance

```
delete(30, 40)
→ right
  delete(50, 40)
  → left
    delete(40, 40)
    → match found → one child (45) → return 45
  ← back to 50: height = 2, balance = 0 → OK
← back to 30: height = 3, balance = 0 → OK

```
✅ Simple replace. No rebalancing needed.


### ❌ Delete 60 — Rebalance Required (Right-Left Case)

```
delete(30, 60)
→ right
  delete(50, 60)
  → right
    delete(70, 60)
    → left
      delete(60, 60)
      → match found → no children → return None
    ← 70: height = 2 → balance = -1
  ← 50: height = 3 → balance = -2 → 🚨 Unbalanced

→ Balance(50) = -2
→ Balance(70) = -1 → 🔁 Right-Left Case

➡ Perform rightRotate(70)
➡ Perform leftRotate(50)

```

✅ Double rotation restores balance.


### ✅ Final Tree (After All Deletions)

```
        30
      /    \
    None    65
           /  \
         50    70
        /  \     \
      45   55     80

```

### 📝 Summary Table

| Deleted | Rebalance? | Case       | Action                 |
| ------- | ---------- | ---------- | ---------------------- |
| 10      | ❌ No       | Leaf       | None                   |
| 20      | ✅ Yes      | Left-Left  | rightRotate(50)        |
| 40      | ❌ No       | One Child  | None                   |
| 60      | ✅ Yes      | Right-Left | rightRotate+leftRotate |

