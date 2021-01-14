import pygame

class Ball:
    def __init__(self):
        self.x_cord = 387.5
        self.y_cord = 300
        self.height = 25
        self.width = 25
        self.color = (255, 255, 255)
        self.ball_y_speed = 5
        self.ball_x_speed = 5
    def reset_ball(self):
        self.x_cord = 387.5
        self.y_cord = 300