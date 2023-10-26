import pygame


class PyGameQuadTree:
    """
    PyGameQuadTree is a class for visualizing a quadtree structure using Pygame.

    Args:
        quadtree: The root node of the quadtree to be displayed.
        quadtree_depth: The depth of the quadtree.
        screen_size: The size of the Pygame display window (default is 400x400).

    Methods:
        - display_all(): Initializes and displays the quadtree and its depth.
        - display_quadtree(node, x, y, width, height): Recursively displays the quadtree nodes.
        - display_depth(): Displays the depth of the quadtree.
    """

    def __init__(self, quadtree, quadtree_depth, screen_size=(750, 750)):
        """
        Initialize the PyGameQuadTree.

        Args:
            quadtree: The quadtree to be displayed.
            quadtree_depth: The depth of the quadtree.
            screen_size: The size of the Pygame display window (default is 400x400).
        """
        self.__quadtree = quadtree
        self.__quadtree_depth = quadtree_depth
        self.__screen_size = screen_size
        self.__screen = pygame.display.set_mode(screen_size)
        self.__node_size = (screen_size[0] / 2, screen_size[1] / 2)
        pygame.display.set_caption("Quadtree")

    def display_all(self):
        """
        Initializes Pygame and displays the quadtree.
        """
        pygame.init()
        self.display_quadtree(self.__quadtree, 0, 0, *self.__screen_size)
        self.display_depth()
        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()

    def display_quadtree(self, node, x, y, width, height):
        """
        Recursively displays the quadtree nodes and leaves.

        Args:
            node: The quadtree.
            x: The x-coordinate of the node's position.
            y: The y-coordinate of the node's position.
            width: The width of the node's bounding box.
            height: The height of the node's bounding box.
        """
        if isinstance(node, bool):
            color = (14, 17, 17) if node else (251, 250, 245)
            pygame.draw.rect(self.__screen, color, (x, y, width, height))
            pygame.draw.rect(self.__screen, (169, 169, 169), (x, y, width, height), 1)
        else:
            w, h = width / 2, height / 2
            self.display_quadtree(node.hg, x, y, w, h)
            self.display_quadtree(node.hd, x + w, y, w, h)
            self.display_quadtree(node.bd, x + w, y + h, w, h)
            self.display_quadtree(node.bg, x, y + h, w, h)

    def display_depth(self):
        """
        Displays the depth of the quadtree on the Pygame page.
        """
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(f"profondeur: {self.__quadtree_depth}", True, "red")

        text_rect = text.get_rect()
        text_rect.center = (self.__screen_size[0] / 2, 20)
        self.__screen.blit(text, text_rect)