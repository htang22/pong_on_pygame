import pygame
from display import Display
import paddle
import ball
import score

class Game:
    def __init__(self):
        self.ball = ball.Ball()
        self.score = score.Score()
        self.left_paddle = paddle.Paddle("left")
        self.right_paddle = paddle.Paddle("right")
        self.display = Display()
        self.screen = self.display.screen
        self.y_speed = 15

    def run_game(self):
        keys = pygame.key.get_pressed()
        self.screen.fill((0, 0, 0))
        # Draw the paddles
        right_pad = pygame.draw.rect(self.screen, self.right_paddle.color,
                                     (
                                     self.right_paddle.x_cord, self.right_paddle.y_cord, self.right_paddle.width, self.right_paddle.height))
        left_pad = pygame.draw.rect(self.screen, self.left_paddle.color,
                                    (self.left_paddle.x_cord, self.left_paddle.y_cord, self.left_paddle.width, self.left_paddle.height))


        if keys[pygame.K_UP] and self.right_paddle.y_cord > 0:
            self.right_paddle.y_cord -= self.y_speed
        if keys[pygame.K_DOWN] and self.right_paddle.y_cord < 600 - self.right_paddle.height:
            self.right_paddle.y_cord += self.y_speed
        if keys[pygame.K_w] and self.left_paddle.y_cord > 0:
            self.left_paddle.y_cord -= self.y_speed
        if keys[pygame.K_s] and self.left_paddle.y_cord < 600 - self.left_paddle.height:
            self.left_paddle.y_cord += self.y_speed


        # Drawing the ball and ball movement
        game_ball = pygame.draw.rect(self.screen, self.ball.color, (self.ball.x_cord, self.ball.y_cord, self.ball.width, self.ball.height))

        if self.ball.ball_moving_state:
            # Ball movement and collision with wall
            if self.ball.y_cord < 575 and self.ball.y_cord > 0:
                self.ball.y_cord += self.ball.ball_y_speed
                self.ball.x_cord += self.ball.ball_x_speed
            else:
                self.ball.ball_y_speed *= -1
                self.ball.y_cord += self.ball.ball_y_speed
        else:
            if keys[pygame.K_SPACE]:
                self.ball.ball_moving_state = self.ball.move_ball()
            self.display.display_continue_message(self.screen, (49, 51, 53))


        if right_pad.colliderect(game_ball) or left_pad.colliderect(game_ball):
            self.ball.ball_x_speed *= -1
            for _ in range(2):
                self.ball.x_cord += self.ball.ball_x_speed
            self.ball.ball_x_speed *= 1.1

        # reset ball if goes past the paddle
        if self.ball.x_cord < 30 or self.ball.x_cord > 770:
            self.ball.ball_moving_state = False
            if self.ball.x_cord < 30:
                self.score.right_score += 1
                self.ball.ball_x_speed = 5
            elif self.ball.x_cord > 770:
                self.score.left_score += 1
                self.ball.ball_x_speed = 5
                self.ball.ball_x_speed *= -1
            self.ball.reset_ball()


        # score
        self.score.show_score(self.screen, (255, 255, 255))



        # Game over
        if self.score.game_over():
            self.screen.fill((0, 0, 0))
            self.score.reset_score()

            return False
        else:
            return True

        # Checks to see if a key is pressed if one is then move a paddle



