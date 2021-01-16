import pygame


class Score:
    def __init__(self):
        self.right_score = 0
        self.left_score = 0
        self.right_cord = (465, 50)
        self.left_cord = (300, 50)

    def show_score(self,window, color):
        font = pygame.font.Font("freesansbold.ttf", 80)
        right_score = font.render(f"{self.right_score}", True, color)
        left_score = font.render(f"{self.left_score}", True, color)
        pygame.draw.rect(window, color, (400, 0, 10, 275))
        pygame.draw.rect(window, color, (400, 350, 10, 275))
        window.blit(right_score, self.right_cord)
        window.blit(left_score, self.left_cord)

    def game_over(self):
        if self.left_score == 7 or self.right_score == 7:
            return True
        else:
            return False
    def reset_score(self):
        self.right_score = 0
        self.left_score = 0





