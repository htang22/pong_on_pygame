import display

screen = display.Display()


class Paddle:
    def __init__(self, position):
        self.color = (255, 255, 255)
        self.x_cord = 0
        self.y_cord = 0
        self.width = 25
        self.height = 150
        # Checks which position the paddle is created and creates a "left" or "right" paddle
        if position == "left":
            self.reset_paddle(position)
        else:
            self.reset_paddle(position)

    def reset_paddle(self, left):
        """Resets the left and right paddle to the default position in the middle"""
        if left == "left":
            self.x_cord = 30
            self.y_cord = 250
        else:
            self.x_cord = 740
            self.y_cord = 250
