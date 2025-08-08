# bplus_tree.py

class BPlusTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []
        self.next_leaf = None  # Pointer to the next leaf for range queries

class BPlusTree:
    def __init__(self, order=4):
        self.root = BPlusTreeNode(leaf=True)
        self.order = order

    def search(self, node, key):
        if node.leaf:
            for i, item in enumerate(node.keys):
                if key == item:
                    return node.children[i]  # Return associated value
            return None
        else:
            for i, item in enumerate(node.keys):
                if key < item:
                    return self.search(node.children[i], key)
            return self.search(node.children[-1], key)

    def split_node(self, parent, node, index):
        new_node = BPlusTreeNode(leaf=node.leaf)
        mid_index = len(node.keys) // 2
        mid_key = node.keys[mid_index]

        new_node.keys = node.keys[mid_index + 1:]
        new_node.children = node.children[mid_index + 1:]
        node.keys = node.keys[:mid_index]
        node.children = node.children[:mid_index + 1]

        if node.leaf:
            new_node.next_leaf = node.next_leaf
            node.next_leaf = new_node

        parent.keys.insert(index, mid_key)
        parent.children.insert(index + 1, new_node)

    def insert(self, key, value):
        root = self.root
        if len(root.keys) == self.order - 1:
            new_root = BPlusTreeNode()
            new_root.children.append(self.root)
            self.split_node(new_root, self.root, 0)
            self.root = new_root
        self._insert_non_full(self.root, key, value)

    def _insert_non_full(self, node, key, value):
        if node.leaf:
            if key not in node.keys:
                for i, item in enumerate(node.keys):
                    if key < item:
                        node.keys.insert(i, key)
                        node.children.insert(i, value)
                        return
                node.keys.append(key)
                node.children.append(value)
        else:
            for i, item in enumerate(node.keys):
                if key < item:
                    self._insert_non_full(node.children[i], key, value)
                    return
            self._insert_non_full(node.children[-1], key, value)

    def delete(self, key):
        self._delete(self.root, key)

        if len(self.root.keys) == 0 and not self.root.leaf:
            self.root = self.root.children[0]

    def _delete(self, node, key):
        if node.leaf:
            if key in node.keys:
                index = node.keys.index(key)
                del node.keys[index]
                del node.children[index]
        else:
            for i, item in enumerate(node.keys):
                if key < item:
                    self._delete(node.children[i], key)
                    self._rebalance(node, i)
                    return
            self._delete(node.children[-1], key)
            self._rebalance(node, len(node.keys))

    def _rebalance(self, parent, index):
        node = parent.children[index]
        min_keys = (self.order - 1) // 2
        if len(node.keys) >= min_keys:
            return

        if index > 0:
            left_sibling = parent.children[index - 1]
            if len(left_sibling.keys) > min_keys:
                node.keys.insert(0, parent.keys[index - 1])
                parent.keys[index - 1] = left_sibling.keys.pop(-1)
                if not node.leaf:
                    node.children.insert(0, left_sibling.children.pop(-1))
                return

        if index < len(parent.children) - 1:
            right_sibling = parent.children[index + 1]
            if len(right_sibling.keys) > min_keys:
                node.keys.append(parent.keys[index])
                parent.keys[index] = right_sibling.keys.pop(0)
                if not node.leaf:
                    node.children.append(right_sibling.children.pop(0))
                return

        if index > 0:
            left_sibling = parent.children[index - 1]
            left_sibling.keys.extend([parent.keys.pop(index - 1)] + node.keys)
            left_sibling.children.extend(node.children)
            parent.children.pop(index)
        else:
            right_sibling = parent.children[index + 1]
            node.keys.extend([parent.keys.pop(index)] + right_sibling.keys)
            node.children.extend(right_sibling.children)
            parent.children.pop(index + 1)