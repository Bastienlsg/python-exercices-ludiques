import pygame
import pytest
from src.quadtree import QuadTree
from src.pygame_quadtree import PyGameQuadTree


@pytest.fixture
def setup_pygame():
    pygame.init()
    yield
    pygame.quit()


def test_display_quadtree(setup_pygame):
    # Test searching colors in different pixels
    quadtree = QuadTree(True, False, True, QuadTree(True, True, False, False))
    screen_size = (750, 750)

    interface = PyGameQuadTree(quadtree)

    interface.display_quadtree(quadtree, 0, 0, *screen_size)

    screen_content = pygame.surfarray.array3d(interface._PyGameQuadTree__screen)

    pixel_color_black = screen_content[200, 200]
    pixel_color_white = screen_content[600, 100]

    expected_color_black = (14, 17, 17)
    expected_color_white = (251, 250, 245)

    assert (pixel_color_black == expected_color_black).any()
    assert (pixel_color_white == expected_color_white).any()
