import pygame


class Ball:
    def __init__(self):
        self.x_cord = 491
        self.y_cord = 300
        self.height = 25
        self.width = 25
        self.color = (255, 255, 255)
        self.ball_y_speed = 5
        self.ball_x_speed = 5
        self.ball_moving_state = False

    def reset_ball(self):
        self.x_cord = 391
        self.y_cord = 300

    def move_ball(self):
        return True
