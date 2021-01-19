import pygame


class Ball:
    def __init__(self):
        self.x_cord = 391
        self.y_cord = 300
        self.height = 25
        self.width = 25
        self.color = (255, 255, 255)
        self.ball_y_speed = 3
        self.ball_x_speed = 3
        self.ball_moving_state = False

    def reset_ball(self):
        self.x_cord = 391
        self.y_cord = 300

    def random_moving_ball(self, screen):
        pygame.time.Clock().tick(120)
        self.x_cord += self.ball_x_speed
        self.y_cord += self.ball_y_speed
        if 575 > self.y_cord > 0:
            self.y_cord += self.ball_y_speed
            self.x_cord += self.ball_x_speed
        else:
            self.ball_y_speed *= -1
            self.y_cord += self.ball_y_speed
        if 0 < self.x_cord < 775:
            pass
        else:
            self.ball_x_speed *= -1
            self.x_cord += self.ball_x_speed
        pygame.draw.rect(screen, self.color, (self.x_cord, self.y_cord, self.width, self.height))
