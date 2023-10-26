from src.quadtree import QuadTree


def test_sample():
    # Test function for a sample quadtree JSON file
    filename = "../files/quadtree.json"

    # Create a QuadTree instance from the JSON file
    q = QuadTree.from_file(filename)

    # Check if the depth of the quadtree matches the expected depth (4)
    assert q.depth() == 4


def test_single():
    # Test function for a simple quadtree JSON file
    filename = "../files/quadtree_easy.json"

    # Create a QuadTree instance from the JSON file
    q = QuadTree.from_file(filename)

    # Check if the depth of the quadtree matches the expected depth (1)
    assert q.depth() == 1
