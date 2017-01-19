# Ryan Ge
# January 10, 2017
# pipeline_wall

import pygame

class Wall(pygame.sprite.Sprite):

    def __init__(self, width, height):
        super(). __init__()

        self.WALL_HEIGHT = height
        self.WALL_WIDTH = width

        self.surface = pygame.Surface((self.WALL_WIDTH, self.WALL_HEIGHT))
        self.surface.fill((255,0,0))
        self.rect = self.surface.get_rect()