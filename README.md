# PyGameQuadTree - Visualizing Quadtree Structures with Pygame

PyGameQuadTree is a Python class for visualizing quadtree structures using the Pygame library. This tool allows you to create a graphical representation of a quadtree, making it easier to understand and debug your quadtree-based algorithms. This README provides an overview of how to use PyGameQuadTree and its features.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation

1. Clone this repository.
2. Make sure all dependencies are installed. You can install them via pip :

   ```shell
   pip install requirements.txt
   ```

## Usage

### Creating a QuadTree

To use PyGameQuadTree, you first need to create a QuadTree data structure. You can create a QuadTree using the `QuadTree` class provided in the example. A QuadTree is a hierarchical data structure that recursively divides space into four quadrants, representing a two-dimensional space partition.


```python
from pygame_quadtree import PyGameQuadTree
from quadtree import QuadTree

def main():
    filename = "quadtree.json"
    quadtree = QuadTree.from_file(filename)
    
    quadtree_depth = quadtree.depth()
    
    interface = PyGameQuadTree(quadtree, quadtree_depth)
    interface.display_all()

if __name__ == "__main__":
    main()
```

In this example, make sure to replace `"quadtree_data.json"` with the path to your quadtree data file. The `QuadTree` class provided in the example can load quadtree data from a JSON file and create a quadtree structure.