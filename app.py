import os

from src.quadtree import QuadTree
from src.file_manager import FileManager
from src.pygame_quadtree import PyGameQuadTree


def main():
    directory_path = "files/"

    # Display available JSON files and get user choice
    file_list = FileManager.display_available_json_files(directory_path)

    if file_list is None:
        return

    choice = FileManager.get_valid_file_choice(file_list)
    chosen_file = os.path.join(directory_path, file_list[choice - 1])

    # Load quadtree
    quadtree = QuadTree.from_file(chosen_file)

    # Create and display the interface
    interface = PyGameQuadTree(quadtree)
    interface.display_all()


if __name__ == "__main__":
    main()
