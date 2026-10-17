import pygame
import sys

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Random title')

main = True

while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            main = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print("LEFT")

            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print("RIGHT")

            if event.key == pygame.K_UP or event.key == ord('w'):
                print("UP / JUMP")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print("LEFT STOP")

            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print("RIGHT STOP")

            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False