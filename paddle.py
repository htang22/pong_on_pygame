import pygame
import display

screen = display.Display()

class Paddle:
    def __init__(self, position):
        self.color = (255, 255, 255)
        self.x_cord = 0
        self.y_cord = 0
        self.width = 25
        self.height = 150
        if position == "left":
            self.x_cord = 30
            self.y_cord = 250
        else:
            self.x_cord = 740
            self.y_cord = 250





