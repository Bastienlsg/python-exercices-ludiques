from __future__ import annotations

import json


class QuadTree:
    """
    QuadTree is a class that represents a quadtree data structure.

    Attributes:
        NB_NODES (int): The number of nodes in a quadtree (always 4).

    Methods:
    - __init__(hg: bool | QuadTree, hd: bool | QuadTree, bd: bool | QuadTree, bg: bool | QuadTree):
    Initializes a QuadTree instance.
    - depth() -> int: Calculates and returns the depth of the quadtree.
    - from_file(filename: str) -> QuadTree: Creates a QuadTree instance from a JSON file.
    - from_list(data: list) -> QuadTree: Creates a QuadTree instance from a list of data.
    """

    NB_NODES: int = 4

    def __init__(self, hg: bool | QuadTree, hd: bool | QuadTree, bd: bool | QuadTree, bg: bool | QuadTree):
        """
        Initializes a QuadTree instance.

        Args:
            hg (bool | QuadTree): The top-left node (or a subtree) of the quadtree.
            hd (bool | QuadTree): The top-right node (or a subtree) of the quadtree.
            bd (bool | QuadTree): The bottom-right node (or a subtree) of the quadtree.
            bg (bool | QuadTree): The bottom-left node (or a subtree) of the quadtree.
        """
        self.__hg = hg
        self.__hd = hd
        self.__bd = bd
        self.__bg = bg

    def depth(self) -> int:
        """
        Calculates and returns the depth of the quadtree.

        Returns:
            int: The depth of the quadtree.
        """
        if not isinstance(self.hg, QuadTree) and not isinstance(self.hd, QuadTree) \
               and not isinstance(self.bd, QuadTree) and not isinstance(self.bg, QuadTree):
            return 1
        else:
            depths = []
            for child in [self.hg, self.hd, self.bd, self.bg]:
                if isinstance(child, QuadTree):
                    depths.append(child.depth())

            return max(depths) + 1

    @staticmethod
    def from_file(filename: str) -> QuadTree:
        """
        Creates a QuadTree instance from a JSON file.

        Args:
            filename (str): The name of the JSON file containing quadtree data.

        Returns:
            QuadTree: A QuadTree instance constructed from the JSON data.
        """
        with open(filename, 'r') as file:
            data = json.load(file)
            return QuadTree.from_list(data)

    @staticmethod
    def from_list(data: list) -> QuadTree:
        """
        Creates a QuadTree instance from a list of data.

        Args:
            data (list): A list containing quadtree data.

        Returns:
            QuadTree: A QuadTree instance constructed from the list.
        """
        if len(data) != 4:
            raise ValueError("La liste de données doit contenir exactement 4 éléments.")

        hg, hd, bd, bg = data

        match hg:
            case list():
                hg = QuadTree.from_list(hg)
            case 0:
                hg = False
            case 1:
                hg = True

        match hd:
            case list():
                hd = QuadTree.from_list(hd)
            case 0:
                hd = False
            case 1:
                hd = True

        match bd:
            case list():
                bd = QuadTree.from_list(bd)
            case 0:
                bd = False
            case 1:
                bd = True

        match bg:
            case list():
                bg = QuadTree.from_list(bg)
            case 0:
                bg = False
            case 1:
                bg = True

        return QuadTree(hg, hd, bd, bg)


    @property
    def hg(self):
        return self.__hg

    @property
    def hd(self):
        return self.__hd

    @property
    def bd(self):
        return self.__bd

    @property
    def bg(self):
        return self.__bg
