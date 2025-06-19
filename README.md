# Global Cargo Management System (GCMS)

A robust cargo management system developed for efficiently storing and managing objects in bins based on size and color classification.

## Project Overview

This project implements a Global Cargo Management System using advanced data structures. The system allows users to:
- Add bins with unique IDs and specified capacities
- Add objects with specific sizes and colors
- Automatically find the best bin for each object based on color-specific allocation strategies
- Retrieve information about bins and their contents
- Remove objects from bins

## Data Structures Used

The primary data structure used in this project is an **AVL Tree** (self-balancing binary search tree) which ensures O(log n) time complexity for most operations. Key implementations include:

- **AVL Tree**: Used for storing and efficiently retrieving bins and objects
- **Multiple Tree Instances**:
  - `avl_bin`: Stores bin objects indexed by their ID
  - `avl_object`: Stores all cargo objects 
  - `avl_search`: Special AVL tree for bin selection algorithms
  - `avl_inside_bin`: Each bin contains its own AVL tree to track contained objects

## Object Allocation Strategy

Objects are allocated to bins based on their color:

- **BLUE**: Placed in the bin with sufficient capacity that has the smallest ID
- **YELLOW**: Placed in the bin with sufficient capacity that has the largest ID
- **RED**: Placed in the bin with the largest capacity among those with the smallest IDs
- **GREEN**: Placed in the bin with the largest capacity among those with the largest IDs

## Project Structure

- `main.py`: Entry point of the application with example usage
- `gcms.py`: Core GCMS class implementing the management system functionality
- `avl.py`: Implementation of the AVL tree data structure with custom comparators
- `bin.py`: Bin class representing storage containers
- `object.py`: Object class and Color enum for cargo items
- `node.py`: Node implementation for the AVL tree
- `exceptions.py`: Custom exceptions for error handling

## How to Run

### Prerequisites
- Python 3.6 or higher

### Running the Program

1. Clone the repository
```bash
git clone https://github.com/your-username/Cargo-management-system-COL106.git
cd Cargo-management-system-COL106
```

2. Run the main script
```bash
python main.py
```

### Creating Your Own Implementation

To use the GCMS in your own code:

```python
from gcms import GCMS
from object import Color

# Initialize the GCMS
gcms = GCMS()

# Add bins with ID and capacity
gcms.add_bin(1001, 100)
gcms.add_bin(1002, 150)

# Add objects with ID, size, and color
try:
    gcms.add_object(5001, 50, Color.BLUE)
    gcms.add_object(5002, 30, Color.RED)
    gcms.add_object(5003, 40, Color.YELLOW)
except Exception as e:
    print(f"Error: {e}")

# Get bin information
print(gcms.bin_info(1001))
```

## Design Decisions

1. **AVL Trees**: Chosen for their self-balancing property, ensuring O(log n) performance even in worst-case scenarios
2. **Custom Comparators**: The system uses different comparison strategies to handle various bin selection algorithms
3. **Color-Based Allocation**: Objects are allocated to bins using different strategies based on their color, allowing for flexible management policies
4. **Exception Handling**: Robust error handling for cases like insufficient bin capacity

## Algorithms

1. **compact_least**: Finds the bin with sufficient capacity and smallest ID
2. **compact_greatest**: Finds the bin with sufficient capacity and largest ID
3. **largest_least**: Finds the bin with largest capacity among those with smallest IDs
4. **largest_greatest**: Finds the bin with largest capacity among those with largest IDs

## Performance Analysis

- **Adding Bins**: O(log n) where n is the number of bins
- **Adding Objects**: O(log n) for finding the appropriate bin
- **Bin Information Retrieval**: O(log n)
- **Object Removal**: O(log n)

The AVL tree implementation ensures that operations remain efficient even as the system scales to handle many bins and objects.

## License

This project was developed as part of the COL106 course assignment at IIT Delhi.