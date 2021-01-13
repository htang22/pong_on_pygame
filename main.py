import pygame
import display

pygame.init()

# screen = pygame.display.set_mode(size=(600,600))
pygame.display.set_caption("Pong")

display = display.Display()
screen = display.screen

running = True
while running:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()