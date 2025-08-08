# main.py

from bplus_tree import BPlusTree
from bplus_crud import BPlusTreeWithCRUD
from bplus_range_query import BPlusTreeWithRangeQuery
from bplus_visualization import display_tree, display_leaves

# Initialize B+ Tree
tree = BPlusTreeWithRangeQuery(order=4)

# Example operations
tree.create(10, "Record A")
tree.create(20, "Record B")
tree.create(5, "Record C")
tree.create(15, "Record D")

# Visualize after insertions
print("Tree structure after insertions:")
display_tree(tree)
display_leaves(tree)

# Perform range query and visualize
tree.range_query(5, 20)

# Deletion example
tree.delete(10)
print("\nTree structure after deletion of key 10:")
display_tree(tree)
display_leaves(tree)