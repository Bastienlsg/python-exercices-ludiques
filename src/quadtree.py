from __future__ import annotations

import json


class QuadTree:
    NB_NODES: int = 4

    def __init__(self, hg: bool | QuadTree, hd: bool | QuadTree, bd: bool | QuadTree, bg: bool | QuadTree):
        self.__hg = hg
        self.__hd = hd
        self.__bd = bd
        self.__bg = bg

    @property
    def depth(self) -> int:
        return 1

    @staticmethod
    def from_file(filename: str) -> QuadTree:
        with open(filename, 'r') as file:
            data = json.load(file)
            return QuadTree.from_list(data)

    @staticmethod
    def from_list(data: list) -> QuadTree:
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
