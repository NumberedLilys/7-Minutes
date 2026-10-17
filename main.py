import pygame
import sys

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Random title')

clock = pygame.time.Clock()

black = (0,0,0) # Get rid of to test functionality
white = (255,255,255)

orange = (214,60,43)

crashed = False
ghost_image = pygame.image.load('assets/GHOST.jpg')

def ghost(x, y):
    gameDisplay.blit(ghost_image, (x, y))

x =  (display_width * 0.15)
y = (display_height * 0.15)
        

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    gameDisplay.fill(orange)
    ghost(x, y)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()