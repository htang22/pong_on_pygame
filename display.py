import pygame

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800


class Display:
    def __init__(self):
        self.screen = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))
        self.start_message_cord = (150,300)

    def display_start_message(self, window):
        font = pygame.font.Font("freesansbold.ttf", 32)
        press_space = font.render("Press the Space bar to play pong", True, (255, 255, 255))
        window.blit(press_space, self.start_message_cord)

