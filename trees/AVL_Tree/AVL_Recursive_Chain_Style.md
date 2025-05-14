
# AVL Tree Insertions

Sequence: [1,2,3,4,5,6,7,15,14,13,12,11,10,9,8,25,35]

## Step 1: Insert 1
Tree after insertion:

```
1
```
Insert 1 as the root node of the tree.

## Step 2: Insert 2
Tree after insertion:

```
    1
     \
      2
```
Insert 2 as the right child of 1.

The tree remains balanced.

## Step 3: Insert 3
Tree after insertion:

```
    1
     \
      2
       \
        3
```
Insert 3 as the right child of 2.

The tree is unbalanced with a balance factor of +2 at node 1, so we need to perform a left rotation at node 1.

After left rotation at node 1:

```
    2
   / \
  1   3
```
The tree is balanced after the left rotation, with 2 as the root.

## Step 4: Insert 4
Tree after insertion:

```
    2
   / \
  1   3
       \
        4
```
Insert 4 as the right child of 3.

The tree remains balanced.

## Step 5: Insert 5
Tree after insertion:

```
    2
   / \
  1   3
       \
        4
         \
          5
```
Insert 5 as the right child of 4.

The tree becomes unbalanced at node 3 with a balance factor of +2, so we perform a left rotation at node 3.

After left rotation at node 3:

```
    2
   / \
  1   4
     / \
    3   5
```
The tree is balanced again after the left rotation.

## Step 6: Insert 6

Tree after insertion: (Insert to the right of 5)

```
    2
   / \
  1   4
     / \
    3   5
         \
          6
```
Balance at 5 = -1, at 4 = -2 → RR case at node 2.

🔁 Rotate Left at 2:
```
    4
   / \
  2   5
 / \    \
1   3    6

```

The tree now balanced.

## Step 7: Insert 7
- Insert to the right of 6.
Tree after insertion:

```
    4
   / \
  2   5
 / \    \
1   3    6
            \
             7

```
Balance at 6 = -1, at 5 = -2 → RR case at node 5.

🔁 Rotate Left at 5:

```
    4
   / \
  2   6
 / \  / \
1  3 5  7

```
The tree is balanced again after the RR rotation.

## Step 8: Insert 15
- Goes to right of 7.

```
    4
   / \
  2   6
 / \  / \
1  3 5  7
         \
          15

```
Balance at 7 = -1, all other balances okay → no rotation.

## Step 9: Insert 14
- Goes to left of 15 → RL case at node 7.

```
    4
   / \
  2   6
 / \  / \
1  3 5  7
         \
          15
        /
       14

```
Balance at 7 = -2, and right child (15) has a left child → Right-Left (RL)

🔁 Rotate Right at 15, then Rotate Left at 7:

```
    4
   / \
  2   6
 / \  / \
1  3 5  14
        / \
       7   15

```

## Step 10: Insert 13
Inserted as left of 14 → triggers RL case at node 6.

```
    4
   / \
  2   6
 / \  / \
1  3 5  14
         / \
       13  15
      /
     7

```
- Balance at 6 = -2 → RL case at node 6.

🔁 Rotate Right at 14, then Rotate Left at 6:

```
    4
   / \
  2   7
 / \  / \
1  3 6  14
     /  / \
    5 13  15

```

## Step 11: Insert 12
- inserts to the left of 13

```
    4
   / \
  2   7
 / \  / \
1  3 6  14
     /  / \
    5 13  15
      /
      12
```
- BF of 13   = 1  -> OK
- BF of 14   = 1  -> OK
- BF of 7    = -1 -> OK
- BF of 4    = -2 -> Un-balanced (RR rotation)

```
         7
       /   \
      4     14
     / \    / \
    2   6 13   15
   / \  /  /
  1  3 5  12

```

## Step 12: Insert 11

- inserts to the left of 12
```
         7
       /   \
      4     14
     / \    / \
    2   6 13   15
   / \  /  /
  1  3 5  12
          /
        11

```
- BF of 12   = 1  -> OK
- BF of 13   = 2  -> Un-balanced (LL Rotation)

```
         7
       /   \
      4     14
     / \    / \
    2   6 12   15
   / \  /  / \
  1  3 5 11  13

```

## Step 13: Insert 10

- inserts to the left of 11

```
         7
       /   \
      4     14
     / \    / \
    2   6 12   15
   / \  /  / \
  1  3 5 11  13
        /
       10 
```
- BF of 11   = 1  -> OK
- BF of 12   = 1  -> OK
- BF of 14   = 2  -> Un-balanced (LL Rotation)

```
            7
         /      \
        4        12
       / \       / \
      2   6     11   14
     / \  /     /    / \
    1  3 5     10   13  15
           
```

## Step 14: Insert 9

- inserts to the left of 10
```
            7
         /      \
        4        12
       / \       / \
      2   6     11   14
     / \  /     /    / \
    1  3 5     10   13  15
              /
             9 
           
```

- BF of 10   = 1  -> OK
- BF of 11   = 2  -> Un-balanced (LL Rotation)

```
              7 
         /         \
        4           12
       / \       /      \
      2   6     10      14
     / \  /     / \     / \
    1  3 5     9   11   13  15
              
```

## Step 15: Insert 8

- inserts to the left of 9

```
              7 
         /         \
        4           12
       / \       /      \
      2   6     10      14
     / \  /     / \     / \
    1  3 5     9   11   13  15
              /
            8
              
```
- Tree is balance no need of rotations.

## Step 16: Insert 25

- inserts to the right of 15

```
              7 
         /         \
        4           12
       / \       /      \
      2   6     10      14
     / \  /     / \     / \
    1  3 5     9   11   13  15
              /               \
             8                  25
              
```
- Tree is balance no need of rotations.

## Step 17: Insert 35

- inserts to the right of 25

```
              7 
         /         \
        4           12
       / \       /      \
      2   6     10      14
     / \  /     / \     / \
    1  3 5     9   11   13  15
              /               \
             8                  25
                                  \
                                   35
              
```
- BF of 25   = -1  -> OK
- BF of 15   = -2  -> Un-balanced (RR Rotation)

```
              7 
         /         \
        4           12
       / \       /      \
      2   6     10      14
     / \  /     / \     / \
    1  3 5     9   11   13  25
              /             / \
             8             15    25
              
```