# bplus_range_query.py

from bplus_crud import BPlusTreeWithCRUD

class BPlusTreeWithRangeQuery(BPlusTreeWithCRUD):
    def range_query(self, start_key, end_key):
        print(f"Performing range query from key {start_key} to {end_key}")
        node = self.root
        
        # Step 1: Traverse to find the starting node in the range
        while not node.leaf:
            for i, key in enumerate(node.keys):
                if start_key < key:
                    node = node.children[i]
                    break
            else:
                node = node.children[-1]
        
        # Step 2: Collect records within the range by following `next_leaf` pointers
        results = []
        while node:
            for i, key in enumerate(node.keys):
                if start_key <= key <= end_key:
                    results.append((key, node.children[i]))
                elif key > end_key:
                    break
            node = node.next_leaf
            if node and node.keys[0] > end_key:
                break
        
        # Display or return the collected results
        if results:
            print("Range Query Results:", results)
        else:
            print("No records found within the specified range.")
        return results