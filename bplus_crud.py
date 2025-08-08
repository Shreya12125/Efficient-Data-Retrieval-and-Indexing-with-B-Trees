# bplus_crud.py

from bplus_tree import BPlusTree

class BPlusTreeWithCRUD(BPlusTree):
    def create(self, key, value):
        print(f"Creating record with key: {key}, value: {value}")
        self.insert(key, value)
        print(f"Record with key {key} created successfully.")

    def read(self, key):
        print(f"Reading record with key: {key}")
        value = self.search(self.root, key)
        if value is not None:
            print(f"Record found - Key: {key}, Value: {value}")
        else:
            print(f"Record with key {key} not found.")
        return value

    def update(self, key, new_value):
        print(f"Updating record with key: {key}")
        node = self.root
        while node:
            if key in node.keys:
                index = node.keys.index(key)
                node.children[index] = new_value
                print(f"Record with key {key} updated to new value: {new_value}")
                return True
            elif node.leaf:
                print(f"Record with key {key} not found.")
                return False
            else:
                node = node.children[node.keys.index(key)] if key < node.keys[-1] else node.children[-1]

    def delete_key(self, key):
        print(f"Deleting record with key: {key}")
        super().delete(key)
        print(f"Record with key {key} deleted successfully.")