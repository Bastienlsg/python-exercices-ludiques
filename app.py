from src.quadtree import QuadTree


def main():
    filename = "files/quadtree.txt"

    quadtree = QuadTree.fromFile(filename)
    print(quadtree)


if __name__ == "__main__":
    main()
