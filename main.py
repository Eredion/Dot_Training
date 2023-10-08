# Example file showing a circle moving on screen

import pygame
from dot import Dot
from population import Population

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

goal = pygame.Vector2(400, 20)
dots = Population(screen, goal, 1000)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    pygame.draw.circle(screen, "green", goal, 10)

    if dots.all_dots_dead():
        dots.calculate_fitness()
        dots.natural_selection()
        dots.mutate()
        print(dots.generation)
    else:
        dots.show()
        dots.update()

    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
