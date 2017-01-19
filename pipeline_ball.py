# Ryan Ge
# January 10, 2017
# pipeline_ball

import pygame

class Ball(pygame.sprite.Sprite):

    def __init__(self):
        super(). __init__()

        self.RADIUS = 20

        self.surface = pygame.Surface((self.RADIUS, self.RADIUS))
        self.surface.fill((0,0,255))
        self.rect = self.surface.get_rect()

    def move(self):
        x_pos, _ = pygame.mouse.get_pos()
        # Make the mouse at the center of the paddle
        x_pos -= self.RADIUS / 2

        _, y_pos = pygame.mouse.get_pos()
        y_pos -= self.RADIUS / 2

        self.rect.x = x_pos
        self.rect.y = y_pos