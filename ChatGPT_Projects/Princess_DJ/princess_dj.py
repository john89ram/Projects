import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((750, 450))
pygame.display.set_caption('Princess DJ')
clock = pygame.time.Clock()

background = pygame.image.load('ChatGPT_Projects/Princess_DJ/background.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(background,(0,0))

    pygame.display.update()
    clock.tick(60)
