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
    quadtree = QuadTree(True, False, True, QuadTree(True, True, False, False))
    quadtree_depth = 2
    screen_size = (750, 750)

    interface = PyGameQuadTree(quadtree, quadtree_depth)

    screen_content_before = pygame.surfarray.array3d(interface._PyGameQuadTree__screen)

    interface.display_quadtree(quadtree, 0, 0, *screen_size)

    pygame.time.delay(100)

    screen_content_after = pygame.surfarray.array3d(interface._PyGameQuadTree__screen)

    assert (screen_content_before == screen_content_after).all()