import pygame

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800


class Display:
    def __init__(self):
        self.screen = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))
        self.start_message_cord = (150, 300)

    # def display_start_message(self, window):
    #     """Creates the message to play pong"""
    #     font = pygame.font.Font("freesansbold.ttf", 32)
    #     press_space = font.render("Press the Space bar to play pong", True, (255, 255, 255))
    #     window.blit(press_space, self.start_message_cord)

    def create_text(self, coord, color, size, message, window):
        """Takes in atrributes to create text. The coord for where the text is going to be. The color for the font color. The size for size of the text. The message which is the text you want to display and the window to show the text on the screen """
        font = pygame.font.Font("freesansbold.ttf", size)
        text = font.render(f"{message}", True, color)
        window.blit(text, coord)

    def display_title(self, window, coord, color, font):
        """Creating the title of the game on the start menu"""
        font = pygame.font.Font("freesansbold.ttf", font)
        press_space = font.render("Pong", True, color)
        window.blit(press_space, coord)

    def display_play_message(self, window, coord, color):
        """Creates the click to start message on the menu for the starting button to activate the game function"""
        font = pygame.font.Font("freesansbold.ttf", 32)
        play = font.render("Click to play", True, color)
        window.blit(play, coord)

    def display_continue_message(self, window, color):
        """Creates the messages that tells the user to hit the space bar to move the ball/"""
        font = pygame.font.Font("freesansbold.ttf", 32)
        press_space = font.render("Press the Space    bar to move the ball", True, color)
        window.blit(press_space, (135, 300))

    def display_game_over(self, window):
        """The game over screen that is called after the game is is over."""
        font = pygame.font.Font("freesansbold.ttf", 50)
        game_over = font.render("GAME OVER", True, (255, 255, 255))
        window.blit(game_over, (250, 200))
