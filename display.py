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

    def display_title(self, window, coord, color, font):
        font = pygame.font.Font("freesansbold.ttf", font)
        press_space = font.render("Pong", True, color)
        window.blit(press_space, coord)

    def display_play_message(self, window,coord, color):
        font = pygame.font.Font("freesansbold.ttf", 32)
        play = font.render("Click to play", True, color)
        window.blit(play, coord)

    def display_continue_message(self, window, color):
        font = pygame.font.Font("freesansbold.ttf", 32)
        press_space = font.render("Press the Space    bar to move the ball", True, color)
        window.blit(press_space, (135, 300))

    def display_game_over(self, window):
        font = pygame.font.Font("freesansbold.ttf", 50)
        game_over = font.render("GAME OVER", True, (255, 255, 255))
        window.blit(game_over, (250, 200))





