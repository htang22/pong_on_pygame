import pygame

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800

class Display:
    def __init__(self):
        self.screen = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))