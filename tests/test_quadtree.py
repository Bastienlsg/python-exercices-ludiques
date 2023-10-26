import unittest
from src.quadtree import QuadTree


class TestQuadTree(unittest.TestCase):

    def test_depth_single_level(self):
        # Test the depth when the QuadTree has one level of nodes
        quadtree = QuadTree(True, False, True, False)
        self.assertEqual(quadtree.depth(), 1)

    def test_depth_three_level(self):
        # Test the depth when the QuadTree has three level of nodes
        quadtree = QuadTree(False,
                            QuadTree(False,
                                     QuadTree(True, True, False, True),
                                     True, True),
                            False, True)
        self.assertEqual(quadtree.depth(), 3)

    def test_from_file(self):
        # Test creating a QuadTree from a JSON file
        quadtree = QuadTree.from_file('../files/quadtree.json')
        self.assertEqual(quadtree.depth(), 4)

    def test_from_list(self):
        # Test creating a QuadTree from a list of data
        data = [
                   [0,0,0,[0,1,0,0]],
                   [0,0,[1,0,0,0],0],
                   [0,0,0,[[0,0,1,1],[0,1,0,1],0,0]],
                   [0,0,[[1,0,1,0],[0,0,1,1],0,0],0]
                ]
        quadtree = QuadTree.from_list(data)
        self.assertEqual(quadtree.depth(), 4)

    def test_invalid_list_length(self):
        # Test creating a QuadTree from an invalid list length
        data = [0, 1, 0]
        with self.assertRaises(ValueError):
            QuadTree.from_list(data)


if __name__ == '__main__':
    unittest.main()
