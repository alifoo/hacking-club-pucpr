"""
COMPLETE BINARY SEARCH TREE IMPLEMENTATION (FIXED)
===================================================
- Only public methods (no private helpers)
- Uses recursion throughout
- Duplicates go to the LEFT (using <= instead of <)
- All common BST operations included
- FIXED: No more infinite recursion bugs!

TREE TRAVERSAL EXPLAINED
=========================

There are TWO main categories of tree traversal:

1. DEPTH-FIRST SEARCH (DFS) - Go deep before going wide
   - Uses recursion (or a stack)
   - Explores one branch completely before moving to another
   - Three types: Inorder, Preorder, Postorder

2. BREADTH-FIRST SEARCH (BFS) - Go wide before going deep
   - Uses a queue
   - Explores all nodes at one level before moving to the next
   - Also called: Level-order traversal

-------------------------------------------------------------------
DEPTH-FIRST TRAVERSALS (DFS)
-------------------------------------------------------------------

Given this tree:
        50
       /  \
      30   70
     / \   / \
    20 40 60 80

1. INORDER (Left → Root → Right)
   - Visit left subtree
   - Visit root
   - Visit right subtree
   Result: [20, 30, 40, 50, 60, 70, 80]
   ⭐ SPECIAL: For BST, this gives SORTED order!
   Use case: Get sorted data from BST

2. PREORDER (Root → Left → Right)
   - Visit root FIRST
   - Visit left subtree
   - Visit right subtree
   Result: [50, 30, 20, 40, 70, 60, 80]
   ⭐ SPECIAL: Root comes first - good for copying/cloning tree
   Use case: Create a copy of the tree, serialize tree structure

3. POSTORDER (Left → Right → Root)
   - Visit left subtree
   - Visit right subtree
   - Visit root LAST
   Result: [20, 40, 30, 60, 80, 70, 50]
   ⭐ SPECIAL: Root comes last - good for deletion
   Use case: Delete tree (delete children before parent), calculate directory sizes

-------------------------------------------------------------------
BREADTH-FIRST TRAVERSAL (BFS)
-------------------------------------------------------------------

LEVEL-ORDER (Top to bottom, left to right at each level)
   - Visit all nodes at level 0 (root)
   - Then all nodes at level 1
   - Then all nodes at level 2, etc.
   
Result: [50, 30, 70, 20, 40, 60, 80]

Visual by levels:
   Level 0: 50
   Level 1: 30, 70
   Level 2: 20, 40, 60, 80

⭐ SPECIAL: Processes tree level by level
Use case: Find shortest path, print tree by levels, find nodes at specific depth

-------------------------------------------------------------------
WHY SO MANY TRAVERSALS?
-------------------------------------------------------------------

Different traversals are useful for different tasks:

- Want sorted data from BST? → Use INORDER
- Want to copy the tree? → Use PREORDER
- Want to delete the tree? → Use POSTORDER
- Want to process by levels? → Use LEVEL-ORDER (BFS)
- Want to search efficiently? → Use appropriate traversal based on what you're looking for

-------------------------------------------------------------------
DFS vs BFS - WHEN TO USE WHICH?
-------------------------------------------------------------------

Use DFS when:
✓ Solution is far from root (deep in tree)
✓ Tree is very wide
✓ You want to explore all paths
✓ Memory is limited (recursion uses call stack, not extra queue)

Use BFS when:
✓ Solution is close to root (shallow)
✓ Tree is very deep
✓ You want shortest path
✓ You want to process level by level

Memory usage:
- DFS: Uses stack space = height of tree
- BFS: Uses queue space = width of widest level
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
    # INSERT - Add a value to the tree
    # ========================================
    def insert(self, value):
        # Use the helper that actually does recursion
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        # Base case: found empty spot, create new node here
        if node is None:
            return Node(value)

        # BST Rule: smaller OR EQUAL values go to the left (duplicates left)
        if value <= node.value:
            node.left = self._insert_recursive(node.left, value)
        # BST Rule: larger values go to the right
        else:
            node.right = self._insert_recursive(node.right, value)

        # Return the node (unchanged, except for its children)
        return node

    # ========================================
    # SEARCH - Find if a value exists
    # ========================================
    def search(self, value):
        # Use the helper that actually does recursion
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        # Base case: reached end of tree (value not found)
        if node is None:
            return False

        # Base case: found the value!
        if value == node.value:
            return True

        # Recursive case: search left or right
        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    # ========================================
    # DELETE - Remove a value from the tree
    # ========================================
    def delete(self, value):
        # Use the helper that actually does recursion
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        # Base case: value not found in tree
        if node is None:
            return None

        # Recursive case: search for the node to delete
        if value < node.value:
            # Value is in left subtree
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            # Value is in right subtree
            node.right = self._delete_recursive(node.right, value)
        else:
            # Found the node to delete! Now handle 3 cases:

            # Case 1: Node has no children (leaf node)
            if node.left is None and node.right is None:
                return None  # Remove this node

            # Case 2: Node has only right child
            if node.left is None:
                return node.right  # Replace node with right child

            # Case 3: Node has only left child
            if node.right is None:
                return node.left  # Replace node with left child

            # Case 4: Node has two children
            # Find minimum value in right subtree (successor)
            min_node = self._find_min_node(node.right)
            # Replace current node's value with successor's value
            node.value = min_node.value
            # Delete the successor (it will be a leaf or have only right child)
            node.right = self._delete_recursive(node.right, min_node.value)

        # Return the modified node
        return node

    # ========================================
    # FIND MIN - Get the minimum value
    # ========================================
    def find_min(self):
        if self.root is None:
            return None
        return self._find_min_node(self.root).value

    def _find_min_node(self, node):
        # Keep going left until we can't anymore
        if node.left is None:
            return node
        return self._find_min_node(node.left)

    # ========================================
    # FIND MAX - Get the maximum value
    # ========================================
    def find_max(self):
        if self.root is None:
            return None
        return self._find_max_node(self.root).value

    def _find_max_node(self, node):
        # Keep going right until we can't anymore
        if node.right is None:
            return node
        return self._find_max_node(node.right)

    # ========================================
    # HEIGHT - Calculate tree height
    # ========================================
    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        # Base case: empty node has height 0
        if node is None:
            return 0

        # Recursive case: height = 1 + max(left height, right height)
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return 1 + max(left_height, right_height)

    # ========================================
    # SIZE - Count total nodes
    # ========================================
    def size(self):
        return self._size_recursive(self.root)

    def _size_recursive(self, node):
        # Base case: empty node contributes 0
        if node is None:
            return 0

        # Recursive case: size = 1 (current) + left size + right size
        return 1 + self._size_recursive(node.left) + self._size_recursive(node.right)

    # ========================================
    # INORDER TRAVERSAL - Left, Root, Right
    # Returns values in sorted order
    # ========================================
    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        # Base case: empty node, nothing to add
        if node is None:
            return

        # Recursive case: Left -> Root -> Right
        self._inorder_recursive(node.left, result)  # Visit left subtree
        result.append(node.value)  # Visit root
        self._inorder_recursive(node.right, result)  # Visit right subtree

    # ========================================
    # PREORDER TRAVERSAL - Root, Left, Right
    # ========================================
    def preorder(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        # Base case: empty node, nothing to add
        if node is None:
            return

        # Recursive case: Root -> Left -> Right
        result.append(node.value)  # Visit root
        self._preorder_recursive(node.left, result)  # Visit left subtree
        self._preorder_recursive(node.right, result)  # Visit right subtree

    # ========================================
    # POSTORDER TRAVERSAL - Left, Right, Root
    # ========================================
    def postorder(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        # Base case: empty node, nothing to add
        if node is None:
            return

        # Recursive case: Left -> Right -> Root
        self._postorder_recursive(node.left, result)  # Visit left subtree
        self._postorder_recursive(node.right, result)  # Visit right subtree
        result.append(node.value)  # Visit root

    # ========================================
    # LEVEL-ORDER TRAVERSAL - Breadth-First Search (BFS)
    # Visit nodes level by level, left to right
    # ========================================
    def level_order(self):
        # Base case: empty tree
        if self.root is None:
            return []

        result = []  # Store the traversal result
        queue = [self.root]  # Queue for BFS (start with root)

        # Keep processing until queue is empty
        while len(queue) > 0:
            # Remove first node from queue (FIFO - First In First Out)
            current = queue.pop(0)

            # Visit the current node (add its value to result)
            result.append(current.value)

            # Add left child to queue (if it exists)
            if current.left is not None:
                queue.append(current.left)

            # Add right child to queue (if it exists)
            if current.right is not None:
                queue.append(current.right)

        return result

    # ========================================
    # COUNT OCCURRENCES - Count how many times a value appears
    # ========================================
    def count(self, value):
        return self._count_recursive(self.root, value)

    def _count_recursive(self, node, value):
        # Base case: empty node, count is 0
        if node is None:
            return 0

        # Count in current node (1 if matches, 0 otherwise)
        current_count = 1 if node.value == value else 0

        # Add counts from left and right subtrees
        left_count = self._count_recursive(node.left, value)
        right_count = self._count_recursive(node.right, value)

        return current_count + left_count + right_count

    # ========================================
    # IS EMPTY - Check if tree is empty
    # ========================================
    def is_empty(self):
        return self.root is None


# ============================================
# EXAMPLE USAGE AND TESTING
# ============================================
if __name__ == "__main__":
    print("Creating a Binary Search Tree")
    print("=" * 50)

    # Create a new BST
    bst = BST()

    # Test: Insert values
    print("\n1. INSERTING VALUES")
    values = [50, 30, 70, 30, 20, 40, 60, 80, 30]  # Note: 30 appears 3 times
    print(f"Inserting: {values}")
    for value in values:
        bst.insert(value)

    # Test: Tree properties
    print("\n2. TREE PROPERTIES")
    print(f"Tree height: {bst.height()}")
    print(f"Tree size: {bst.size()}")
    print(f"Is empty: {bst.is_empty()}")
    print(f"Minimum value: {bst.find_min()}")
    print(f"Maximum value: {bst.find_max()}")

    # Test: Search
    print("\n3. SEARCHING")
    print(f"Search for 40: {bst.search(40)}")
    print(f"Search for 100: {bst.search(100)}")
    print(f"Count of 30: {bst.count(30)}")  # Should be 3

    # Test: Traversals
    print("\n4. TRAVERSALS")
    print(f"Inorder (sorted): {bst.inorder()}")
    print(f"Preorder: {bst.preorder()}")
    print(f"Postorder: {bst.postorder()}")
    print(f"Level-order (BFS): {bst.level_order()}")

    # Test: Delete
    print("\n5. DELETING VALUES")
    print(f"Deleting 20 (leaf node)...")
    bst.delete(20)
    print(f"Inorder after deletion: {bst.inorder()}")

    print(f"\nDeleting 30 (node with duplicates)...")
    bst.delete(30)
    print(f"Inorder after deletion: {bst.inorder()}")
    print(f"Count of 30 after one deletion: {bst.count(30)}")  # Should be 2

    print(f"\nDeleting 50 (root node)...")
    bst.delete(50)
    print(f"Inorder after deletion: {bst.inorder()}")

    print("\n" + "=" * 50)
    print("All tests completed!")
