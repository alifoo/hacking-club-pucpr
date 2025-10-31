"""
BINARY SEARCH TREE - DETAILED EXPLANATIONS
===========================================

Q1: Is self.root a pointer to a root node?
-------------------------------------------
Yes! In Python, we don't use explicit pointers like in C/C++, but variables 
that hold objects ARE references (pointers).

Example:
    node1 = Node(5)     # node1 references a Node object in memory
    self.root = node1   # self.root now references the SAME object
    
When we do: self.root = Node(5)
We're storing a REFERENCE to the Node object, not a copy of it.

In Python, you don't need to worry about pointers explicitly - Python handles
this automatically. But yes, conceptually self.root "points to" the root node.


Q2: How come each node is a tree itself?
-----------------------------------------
This is the KEY insight of recursive tree structures!

Every node IS a tree because:
- A node has a value (the root of its subtree)
- A node has left and right children (which are also trees!)
- Even a single node with no children is a valid tree (a tree of size 1)
- Even None (empty) is considered a tree (an empty tree)

Visual example:
        5          <-- This whole thing is a tree
       / \
      3   7        <-- The node with value 3 is ALSO a tree (with its subtrees)
     /     \       <-- The node with value 7 is ALSO a tree (with its subtrees)
    1       9
    
When we call insert(4, node_3):
- We treat node_3 as the ROOT of its own tree
- We apply the same BST rules to that smaller tree
- This is why recursion works so beautifully with trees!


Q3: Why use < instead of <= for comparing with node.value?
-----------------------------------------------------------
Great observation! We use < (not <=) to handle duplicate values consistently.

The logic is:
    if value < node.value:      # Strictly less than → go LEFT
        go left
    else:                        # Greater than OR equal → go RIGHT
        go right

This means:
- Values LESS than current node → go left
- Values EQUAL to current node → go right
- Values GREATER than current node → go right

Why this matters:
- If we allow duplicates, they always go to the RIGHT
- This keeps our BST consistent
- Some BSTs don't allow duplicates at all (they just don't insert if equal)

Alternative approaches:
1. Use < for left, > for right, and ignore equals (no duplicates allowed)
2. Use <= for left, > for right (duplicates go left)
3. Use < for left, >= for right (duplicates go right) ← This is what we do

In our implementation, if you insert 5 twice, the second 5 goes to the right
of the first 5, treating it as "greater than or equal to."
"""


# Define a Node class - this represents each node in our tree
class Node:
    # Constructor to create a new node
    def __init__(self, value):
        self.value = value  # Store the data value
        self.left = None  # Pointer to left child (initially no child)
        self.right = None  # Pointer to right child (initially no child)


# Define the Binary Search Tree class
class BST:
    # Constructor to create an empty tree
    def __init__(self):
        self.root = None  # Tree starts empty (no root node)

    # ========================================
    # PUBLIC METHOD: Insert a value into the tree
    # ========================================
    def insert(self, value):
        # Call the private helper method to do the actual recursion
        self.root = self._insert_recursive(self.root, value)

    # PRIVATE HELPER: Does the actual recursive insertion
    def _insert_recursive(self, node, value):
        # Base case: found an empty spot, create new node here
        if node is None:
            return Node(value)

        # BST Rule: smaller values go to the left
        if value < node.value:
            # Recursively insert in left subtree
            node.left = self._insert_recursive(node.left, value)
        # BST Rule: larger or equal values go to the right
        else:
            # Recursively insert in right subtree
            node.right = self._insert_recursive(node.right, value)

        # Return the node (unchanged except for its children)
        return node

    # ========================================
    # PUBLIC METHOD: Search for a value in the tree
    # ========================================
    def search(self, value):
        # Call the private helper method to do the actual recursion
        return self._search_recursive(self.root, value)

    # PRIVATE HELPER: Does the actual recursive search
    def _search_recursive(self, node, value):
        # Base case: reached end of tree (value not found)
        if node is None:
            return False

        # Base case: found the value!
        if value == node.value:
            return True

        # Recursive case: if value is smaller, search in left subtree
        if value < node.value:
            return self._search_recursive(node.left, value)
        # Recursive case: if value is larger, search in right subtree
        else:
            return self._search_recursive(node.right, value)


# ============================================
# EXAMPLE USAGE - How to use the BST
# ============================================

# Create a new empty binary search tree
bst = BST()

# Insert values one by one
# The tree will organize them automatically:
#       5
#      / \
#     3   7
#    /     \
#   1       9
bst.insert(5)  # Insert 5 as root
bst.insert(3)  # 3 < 5, goes to left of 5
bst.insert(7)  # 7 > 5, goes to right of 5
bst.insert(1)  # 1 < 5, go left; 1 < 3, goes to left of 3
bst.insert(9)  # 9 > 5, go right; 9 > 7, goes to right of 7

# Search for values in the tree
print(bst.search(7))  # True - 7 is in the tree
print(bst.search(4))  # False - 4 is not in the tree
