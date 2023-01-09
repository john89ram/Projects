import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Test Game')
clock = pygame.time.Clock()

sky_surface = pygame.image.load('Game_Start/Art/Backgrounds/sky.png')
ground = pygame.image.load('Game_Start/Art/Backgrounds/ground.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(sky_surface,(0,0))
    screen.blit(ground,(0,250))

    pygame.display.update()
    clock.tick(60)
