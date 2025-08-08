# Efficient Data Retrieval and Indexing with B+ Trees

Python implementation of a B+ Tree with CRUD operations, range queries, and visualization for efficient data indexing and retrieval.  
This project demonstrates how B+ Trees can be used for fast search, insertion, deletion, and range-based retrieval in large datasets while maintaining a balanced tree structure.

## Features
- Supports Create, Read, Update, and Delete (CRUD) operations
- Efficient range queries using linked leaf nodes
- Balanced tree structure with automatic splitting and merging
- Visualization of the tree after key operations
- Scalable for large datasets with minimal performance degradation

## Project Structure
bplus_crud.py           - Implements CRUD operations  
bplus_range_query.py    - Handles range query functionality  
bplus_tree.py           - Core B+ Tree data structure and algorithms  
bplus_visualization.py  - Visualization of the B+ Tree structure  
main.py                 - Entry point to run the project

## Installation
Clone the repository:
git clone https://github.com/shreya12125/Efficient-Data-Retrieval-and-Indexing-with-B-Trees.git
cd Efficient-Data-Retrieval-and-Indexing-with-B-Trees

Install dependencies (only if visualization is required):
pip install matplotlib

## Usage
Run the program:
python main.py

##Example Output
Creating record with key: 10, value: Record A
Record with key 10 created successfully.
Creating record with key: 20, value: Record B
Record with key 20 created successfully.
Creating record with key: 5, value: Record C
Record with key 5 created successfully.
Creating record with key: 15, value: Record D
Record with key 15 created successfully.

Tree structure after insertions:
Level 0: 10
Level 1: 5 15 | 20
Leaf Nodes: 5 15 | 20

Performing range query from key 5 to 20
Range Query Results: [(5, 'Record C'), (15, 'Record D'), (20, 'Record B')]

Tree structure after deletion of key 10:
Level 0: 10
Level 1: 5 15 | 20
Leaf Nodes: 5 15 | 20


## Performance
Search: O(log N)  
Insert: O(log N)  
Delete: O(log N)  
Range Query: O(k + log N) where k is the number of results in range

## Authors
Shreya Sriram  
Shruti Sivakumar  
Vida Nadheera S  



