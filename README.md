# =========================================================
# README.md
# ZipRide Dispatch System
# =========================================================

# PROJECT TITLE
ZipRide Dispatch System

# AUTHOR
Richa Prajapati

# DESCRIPTION
The ZipRide Dispatch System is a Python-based ride dispatch simulation project developed using custom data structures and algorithms.

The system demonstrates:

1. Graph Route Planning
2. Hash Table Lookup
3. Heap Pickup Scheduling
4. Sorting Pickup Records

The project avoids built-in Python data structures such as dictionaries, lists, tuples, deque, and priority queues. NumPy arrays and custom classes are used instead.

------------------------------------------------------------
FILES INCLUDED
------------------------------------------------------------

1. main.py
2. graph.py
3. hash_table.py
4. heap.py
5. sorting.py
6. README.md

------------------------------------------------------------
MODULE DETAILS
------------------------------------------------------------

============================================================
1. main.py
============================================================

Purpose:
Controls the entire ZipRide system using a menu-driven interface.

Features:
- Displays main menu
- Calls all modules
- Runs full system demo
- Handles user interaction

Menu Options:

1. Graph Route Planning
2. Hash Table Lookup
3. Heap Pickup Scheduling
4. Sorting Pickup Records
5. Run Full System Demo
6. Exit

============================================================
2. graph.py
============================================================

Purpose:
Implements graph algorithms for route planning.

Data Structures Used:
- Custom Graph
- Vertex Class
- Edge Class
- Queue Class
- NumPy Arrays

Algorithms:
- BFS Traversal
- DFS Cycle Detection
- Dijkstra Shortest Path

Features:
- Adjacency list representation
- Route connections
- Shortest pickup path calculation
- Cycle detection

Example Routes:
- CBD → Airport
- Airport → IndustrialPark
- University → ShoppingMall

============================================================
3. hash_table.py
============================================================

Purpose:
Stores passenger and driver records.

Data Structures Used:
- Custom Hash Table
- Linked List Chaining
- NumPy Arrays

Classes:
- Passenger
- Driver
- PassengerHashTable
- DriverHashTable

Features:
- Insert records
- Search records
- Delete records
- Collision handling
- Load factor calculation
- Input validation

Validation Rules:
Passenger:
- Tier must be between 1–5
- Name cannot be empty

Driver:
- Status must be:
  Available
  Busy
  Offline

============================================================
4. heap.py
============================================================

Purpose:
Implements a Max Heap for pickup scheduling.

Data Structures Used:
- Custom Max Heap
- NumPy Arrays

Classes:
- PickupRequest
- MaxHeap

Features:
- Insert pickup requests
- Extract highest priority request
- Heapify Up
- Heapify Down
- Peek highest priority request

Priority Formula:
Priority =
(6 - MembershipTier) + (1000 / PickupTime)

Higher priority requests are served first.

============================================================
5. sorting.py
============================================================

Purpose:
Sorts pickup records by estimated pickup time.

Algorithms:
- Merge Sort
- Quick Sort

Features:
- Benchmarking
- Timing analysis
- Random dataset testing
- Nearly sorted dataset testing
- Reverse sorted dataset testing

Complexity:
Merge Sort:
- Best: O(n log n)
- Average: O(n log n)
- Worst: O(n log n)

Quick Sort:
- Best: O(n log n)
- Average: O(n log n)
- Worst: O(n²)

------------------------------------------------------------
SYSTEM REQUIREMENTS
------------------------------------------------------------

Python Version:
- Python 3.10 or above

Required Library:
- NumPy

Install NumPy using:

pip install numpy

------------------------------------------------------------
HOW TO RUN
------------------------------------------------------------

Step 1:
Open terminal in project folder

Step 2:
Run the program

Command:

python main.py

------------------------------------------------------------
EXPECTED OUTPUT
------------------------------------------------------------

===== ZIPRIDE MENU =====

1. Graph Route Planning

2. Hash Table Lookup

3. Heap Pickup Scheduling

4. Sorting Pickup Records

5. Run Full System Demo

6. Exit

Enter Option :

------------------------------------------------------------
PROJECT FEATURES
------------------------------------------------------------

✔ Custom Graph Implementation
✔ BFS Traversal
✔ DFS Cycle Detection
✔ Dijkstra Algorithm
✔ Custom Hash Tables
✔ Collision Handling
✔ Load Factor Analysis
✔ Max Heap Scheduling
✔ Merge Sort
✔ Quick Sort
✔ Benchmark Testing
✔ Menu Driven Program
✔ NumPy Array Usage
✔ Object-Oriented Programming

------------------------------------------------------------
LIMITATIONS
------------------------------------------------------------

- Console-based application
- Static route dataset
- No real-time GPS integration
- No database connectivity

------------------------------------------------------------
FUTURE IMPROVEMENTS
------------------------------------------------------------

- GUI Integration using Tkinter
- Real-time Driver Tracking
- Database Storage
- API Integration
- Dynamic Traffic Prediction
- Mobile Application Support

------------------------------------------------------------
ACADEMIC CONCEPTS USED
------------------------------------------------------------

Data Structures:
- Graph
- Hash Table
- Heap
- Queue
- Linked List

Algorithms:
- BFS
- DFS
- Dijkstra
- Merge Sort
- Quick Sort

Programming Concepts:
- OOP
- Searching
- Sorting
- Collision Resolution
- Complexity Analysis

------------------------------------------------------------
END OF README
------------------------------------------------------------