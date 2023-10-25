from src.quadtree import QuadTree


def test_sample():
    filename = "../files/quadtree.txt"
    q = QuadTree.from_file(filename)
    assert q.depth() == 4


def test_single():
    filename = "../files/quadtree_easy.txt"
    q = QuadTree.from_file(filename)
    assert q.depth() == 1
