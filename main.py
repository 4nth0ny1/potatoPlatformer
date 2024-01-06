import pygame, sys

clock = pygame.time.Clock()

from pygame.locals import *
pygame.init()

pygame.display.set_caption('Potato Platformer')

WINDOW_SIZE = (400, 400)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

player_image = pygame.image.load('Megaman.png')

moving_right = False
moving_left = False

player_location = [50, 50]

while True:
    screen.fill((146, 244, 255))

    screen.blit(player_image, player_location)
    if moving_right == True:
        player_location[0] += 4
    if moving_left == True:
        player_location[0] -= 4

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_LEFT:
                moving_left = True

        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False

    pygame.display.update()
    clock.tick(60)