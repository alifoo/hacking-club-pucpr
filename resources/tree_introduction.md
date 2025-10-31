- Every tree has a root and nodes.
- We can have data inside the nodes.
- A node have reference to some other nodes, we call it children.

- Root
- Children
- Parent
- Sibling (children of the same parent)
- Node in the tree without child: leaf node
- Ancestors and descendents
- Cousins (have same grandparent)

## Tree defined recursively
- Tree is a recursive data structure.

Root of the tree contains link to root of the subtrees.
- In a tree with N nodes, there will be exactly n-1 links (or edges)
- One link for each parent-child relationship (1 incoming edge, several outgoing edges)

## Depth and height
- Depth of x: length of path from root to x. Or, number of edges in path from root to x
- Height of x: number of edges in longest path from x to a leaf
- Height of leaf nodes will be 0.
- Height of tree: height of root node.

## Binary trees
- Each node has at most 2 children.
