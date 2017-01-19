# Ryan Ge
# January 10, 2017
# pipeline game

import pygame, sys, pipeline_ball, pipeline_wall
from pygame.locals import *

def main():

    pygame.init()
    main_surface = pygame.display.set_mode((400, 600), 0, 32)
    pygame.display.set_caption('Pipeline Game')
    main_surface.fill((255,255,255))

    wall_group = pygame.sprite.Group()

    # First wall
    wall = pipeline_wall.Wall(10, 400)
    wall.rect.x = 140
    wall.rect.y = 100
    main_surface.blit(wall.surface, wall.rect)
    wall_group.add(wall)

    # Second wall
    wall = pipeline_wall.Wall(10, 350)
    wall.rect.x = 180
    wall.rect.y = 110
    main_surface.blit(wall.surface, wall.rect)
    wall_group.add(wall)

    # Third wall
    wall = pipeline_wall.Wall(80, 10)
    wall.rect.x = 150
    wall.rect.y = 490
    main_surface.blit(wall.surface, wall.rect)
    wall_group.add(wall)

    # Fourth wall
    wall = pipeline_wall.Wall(10, 360)
    wall.rect.x = 220
    wall.rect.y = 140
    main_surface.blit(wall.surface, wall.rect)
    wall_group.add(wall)

    # Fifth wall
    wall = pipeline_wall.Wall(110, 10)
    wall.rect.x = 150
    wall.rect.y = 100
    main_surface.blit(wall.surface, wall.rect)
    wall_group.add(wall)

    # Sixth wall
    wall = pipeline_wall.Wall(10, 400)
    wall.rect.x = 260
    wall.rect.y = 100
    main_surface.blit(wall.surface, wall.rect)
    wall_group.add(wall)

    # Exit door
    door_group = pygame.sprite.Group()
    door = pipeline_wall.Wall(30, 10)
    door.rect.x = 230
    door.rect.y = 515
    door_group.add(door)


    # Ball
    ball_group = pygame.sprite.Group()

    ball = pipeline_ball.Ball()
    ball.rect.x = 157
    ball.rect.y = 120
    main_surface.blit(ball.surface, ball.rect)
    ball_group.add(ball)

    game_start = False
    hit_wall = False
    ball_out = False

    while True:

        while not hit_wall and not ball_out:
            # Pregame
            start_font = pygame.font.SysFont("Times New Roman", 20)
            start_label = start_font.render("Click on the ball to start", 1, (0,0,0))
            main_surface.blit(start_label, (100, 550))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    game_start = True

                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            # Main game
            while game_start and not hit_wall and not ball_out:
                # Redraw surface and movement of ball
                main_surface.fill((255,255,255))

                for a_wall in wall_group:
                    main_surface.blit(a_wall.surface, a_wall.rect)

                main_surface.blit(ball.surface, ball.rect)

                # Detect collision between ball and wall
                for a_wall in wall_group:
                    if pygame.sprite.spritecollide(a_wall, ball_group, False):
                        hit_wall = True
                        break

                # Detect if ball exited the maze
                if pygame.sprite.spritecollide(ball, door_group, False):
                    ball_out = True
                    break

                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == MOUSEMOTION:
                        ball.move()

                pygame.display.update()

        # Result screen
        main_surface.fill((255,255,255))

        # Display results after the ball hit the wall
        if hit_wall:
            fail_font = pygame.font.SysFont("Times New Roman", 20)
            fail_label = fail_font.render("You Lost!", 1, (0,0,0))
            main_surface.blit(fail_label, (150, 100))

        # Display results after the ball came out
        if ball_out:
            win_font = pygame.font.SysFont("Times New Roman", 20)
            win_label = win_font.render("You Won!", 1, (0, 0, 0))
            main_surface.blit(win_label, (150, 100))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

main()







