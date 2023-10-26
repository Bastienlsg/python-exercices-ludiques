from src.pygame_quadtree import PyGameQuadTree
from src.quadtree import QuadTree


def main():
    filename = "files/quadtree_smile.json"
    quadtree = QuadTree.from_file(filename)
    quadtree_depth = quadtree.depth()
    interface = PyGameQuadTree(quadtree, quadtree_depth)
    interface.display_all()


if __name__ == "__main__":
    main()
