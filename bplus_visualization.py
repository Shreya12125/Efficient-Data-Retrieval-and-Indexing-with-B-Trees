# bplus_visualization.py

from bplus_tree import BPlusTree, BPlusTreeNode

def display_tree(tree: BPlusTree):
    """
    Display the structure of the B+ Tree in a text-based format.
    Shows each level of the tree and keys at each node.
    """
    if not tree.root.keys:
        print("The tree is empty.")
        return

    # Use a queue to perform level-order traversal
    queue = [(tree.root, 0)]  # (node, level)
    current_level = 0
    level_str = ""

    while queue:
        node, level = queue.pop(0)
        
        # When we move to a new level, print the accumulated level_str
        if level != current_level:
            print(f"Level {current_level}: {level_str}")
            level_str = ""
            current_level = level

        # Append node keys to the current level's string
        level_str += " | ".join(map(str, node.keys)) + "   "

        # If it's not a leaf, add its children to the queue for the next level
        if not node.leaf:
            for child in node.children:
                queue.append((child, level + 1))

    # Print the last level's nodes
    print(f"Level {current_level}: {level_str}")

def display_leaves(tree: BPlusTree):
    """
    Display all leaf nodes in a sequence to show the linked leaf node structure.
    """
    # Start from the leftmost leaf node
    node = tree.root
    while node and not node.leaf:
        node = node.children[0]  # Go to the first child of the root

    # Traverse through the linked list of leaf nodes
    level_str = "Leaf Nodes: "
    while node:
        level_str += " | ".join(map(str, node.keys)) + "   "
        node = node.next_leaf

    print(level_str)