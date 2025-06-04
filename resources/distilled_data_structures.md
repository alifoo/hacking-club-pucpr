*This resource is a work in progress.*

## Binary Trees

Basically trees but limited to 2 children for each node (and ordered). It performs O(log n) for deletion and other methods. Any BST Node is also a full BST. (Binary search tree)

Implementation:
```
class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def delete(self, val):
        if self.val is None:
            return None
        if val < self.val:
            if self.left:
                left = self.left.delete(val)
                self.left = left
            return self
        if val > self.val:
            if self.right:
                right = self.right.delete(val)
                self.right = right
            return self
        if val == self.val:
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right
            current = self.right
            while current.left is not None:
                current = current.left
            self.val = current.val
            self.right = self.right.delete(self.val)
            return self


    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val
```

We can preorder traversal a tree to create indexes or postorder too. In the postorder, the difference is that the current node is accessed afetr its children. But the most intuitive wway is still traversing the tree with inorder, so the traversion data looks the same as the tree.

The problem of BSTs is that if we insert like a complete ordered list into it, the tree will be very deep. To calculate a tree height, we need to access it, if the value of the root is none, the height is 0. If no, we then recursively call the height method on each side and at the end we return the max function on the left height, right height + 1 (current node). The sorted data into the tree will be very deep because it's unbalanced. So all the operations that used to be O(log(n)) will then be O(n).

## Red-black Trees (Binary Search Trees but preventing Unbalance by adding a 'fix' step)

In a red-black tree, every node has a color and has to know about their parent (by having a reference to it). We use it to know if the tree is sufficiently balanced. The root is black, and all Nil leaf nodes are black. If a node is red, then both its children are black. All paths from a single node go through the same number of black nodes to reach any of its descendant Nil (black) nodes.

How to perform the rotation:
1. Take the pivots left side node out by pointing the left to the pivots parent.
2. Make the abandoned left child of Pivot to be the right child of the old parent.
3. That's it!

This is by far the most difficult algorithm I saw until now, lol.
Implementation:

```
def fix_insert(self, new_node):
        while new_node != self.root and new_node.parent.red is True:
            parent = new_node.parent
            grandparent = new_node.parent.parent
            uncle = self.nil
            if grandparent.right == parent:
                uncle = grandparent.left
                if uncle.red:
                    uncle.red = False
                    parent.red = False
                    new_node = grandparent
                else:
                    if new_node.parent.left == self:
                        new_node = new_node.parent
                        self.rotate_right(new_node.parent)
                        parent = self.parent
                    parent.red = False
                    grandparent.red = True
                    if grandparent.parent:
                        self.rotate_left(grandparent.parent)
                    else:
                        grandparent.parent = self.nil
                        self.rotate_left(grandparent.parent)
                        
            else:
                uncle = grandparent.right
                if uncle.red:
                    uncle.red = False
                    parent.red = False
                    new_node = grandparent
                else:
                    if new_node.parent.right == new_node:
                        new_node = new_node.parent
                        self.rotate_left(new_node.parent)
                        parent = new_node.parent
                    parent.red = False
                    grandparent.red = True
                    if grandparent.parent:
                        self.rotate_right(grandparent.parent)
                    else:
                        grandparent.parent = self.nil
                        self.rotate_right(grandparent.parent)
                        
        self.root.red = False
```

## Hash maps (key-value pairs)

A python dictionary is a hashmap. As the name implies, we hash a key value and get the index using the modulo operator (hash % len of the underlying structure). In each insertion we need to calculate the need for a resize. To do this, we calculate the load, which is the ratio between populated items in the hashmap and total items. If the load is greater than 5%, we need to resize by creating a temp hashmap with 10x the size of the previous, and then populating it with the previous key value pairs.

Collisions can happen in Hash tables if the algorithm is not that goot. To avoid this, it's possible to use Linear Probing. It works by finding the next avaliable slot after the collision index and placing the new key*value pair there.

Implementation:
```
class HashMap:
    def insert(self, key, value):
        self.resize()
        index = self.key_to_index(key)
        self.hashmap[index] = (key, value)

    def resize(self):
        if len(self.hashmap) == 0:
            self.hashmap.append(None)
            return
        load = self.current_load()
        if load >= 0.05:
            temp = self.hashmap
            self.hashmap = [None for i in range(len(temp) * 10)]
            for b in temp:
                if b is not None:
                    index = self.key_to_index(b[0])
                    self.hashmap[index] = (b[0], b[1])

    def current_load(self):
        if len(self.hashmap) == 0:
            return 1
        filled_buckets = 0
        for b in self.hashmap:
            if b is not None:
                filled_buckets += 1
        return filled_buckets / len(self.hashmap)

    def insert(self, key, value):
        index = self.key_to_index(key)
        original_index = index
        first_iteration = True
        while self.hashmap[index] and self.hashmap[index][0] != key:
            if not first_iteration and index == original_index:
                raise Exception("hashmap is full")
            index = (index + 1) % len(self.hashmap)
            first_iteration = False
        self.hashmap[index] = (key, value)

    def get(self, key):
        index = self.key_to_index(key)
        original_index = index
        first_iteration = True
        while self.hashmap[index]:
            if self.hashmap[index][0] == key:
                return self.hashmap[index][1]
            if not first_iteration and index == original_index:
                raise Exception("sorry, key not found")
            index = (index + 1) % len(self.hashmap) 
            first_iteration = False
        raise Exception("sorry, key not found")

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final
```

## Tries (nested tree of dictionaries)

Each key is a character of a string that maps to the next character in a word. Example:
```
{
	"h": {
		"e": {
			"l": {
				"l": {
					"o": {
						"*": True
					}
				},
				"p": {
					"*": True
				}
			}
		},
		"i": {
			"*": True
		}
	}
}
```
The * character paired with True represents the end of a word. Basic syntax for adding a word:
```
class Trie:
    def add(self, word):
        current_level = self.root
        for char in word:
            if not current_level.get(char, None):
                current_level[char] = {}
            current_level = current_level[char]
        current_level[self.end_symbol] = True

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"
```

Basic syntax for checking if a word exists:
```
class Trie:
    def exists(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                return False
            current = current[letter]
        return self.end_symbol in current
```

Effectively searching the current level with a prefix:
```
class Trie:
    def search_level(self, current_level, current_prefix, words):
        if self.end_symbol in current_level:
            words.append(current_prefix)
        for letter in sorted(current_level.keys()):
            if letter != self.end_symbol:
                self.search_level(current_level[letter], current_prefix + letter, words)
        return words
        
        
    def words_with_prefix(self, prefix):
        matching_words = []
        current_level = self.root
        for letter in prefix:
            if letter not in current_level:
                return []
            current_level = current_level[letter]
        return self.search_level(current_level, prefix, matching_words)
```
Most useful part: Finding matches for substrings (basic)
```
class Trie:
    def find_matches(self, document):
        matches = set()
        for i in range(len(document)):
            current_level = self.root
            for j in range(i, len(document)):
                if document[j] not in current_level:
                    break
                current_level = current_level[document[j]]
                if self.end_symbol in current_level:
                    matches.add(document[i:j + 1])
        return matches
```

Finding matches advanced (including variations dict)
```
class Trie:
    def advanced_find_matches(self, document, variations):
        matches = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                ch = document[j]
                if ch in variations:
                    ch = variations[ch]
                if ch not in level:
                    break
                level = level[ch]
                if self.end_symbol in level:
                    matches.add(document[i : j + 1])
        return matches
```
