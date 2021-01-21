import pygame


class Score:
    def __init__(self):
        self.right_score = 0
        self.left_score = 0
        self.right_cord = (465, 50)
        self.left_cord = (300, 50)
        self.left_color = (0, 0, 0)
        self.right_color = (0, 0, 0)

    def show_score(self, window, color):
        """Takes the window and color and creates a right and left score which are text and also creates rectangles showing the middle and the different sides."""
        font = pygame.font.Font("freesansbold.ttf", 80)
        right_score = font.render(f"{self.right_score}", True, self.right_color)
        left_score = font.render(f"{self.left_score}", True, self.left_color)
        pygame.draw.rect(window, color, (400, 0, 10, 275))
        pygame.draw.rect(window, color, (400, 350, 10, 275))
        window.blit(right_score, self.right_cord)
        window.blit(left_score, self.left_cord)

    def game_over(self):
        """Checks to see if the score of the left or right is equal to 7. Then returns True or False"""
        if self.left_score == 7 or self.right_score == 7:
            return True
        else:
            return False

    def reset_score(self):
        """Resets the score for the right and left score to 0"""
        self.right_score = 0
        self.left_score = 0
