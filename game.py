import pygame

import ball
import score
from display import Display


def get_mouse_pos():
    mx, my = pygame.mouse.get_pos()
    return mx, my


class Game:

    def __init__(self, left_player, right_player):
        self.ball = ball.Ball()
        self.score = score.Score()
        self.left_paddle = left_player
        self.right_paddle = right_player
        self.display = Display()
        self.screen = self.display.screen
        self.y_speed = 8
        self.click = False
        self.reload = pygame.image.load("reload.png")
        self.default_ball_speed = 2

    def reset_game(self):
        self.ball.ball_x_speed = self.default_ball_speed
        self.ball.ball_y_speed = self.default_ball_speed
        self.ball.x_cord = 391
        self.ball.y_cord = 300
        self.score.reset_score()
        self.ball.ball_moving_state = False
        self.left_paddle.reset_paddle("left")
        self.right_paddle.reset_paddle("right")

    def pause_screen(self, ball_x_speed, ball_y_speed, mode):
        running = True
        while running:
            self.click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True
            if mode == "pause":
                play_button = pygame.rect.Rect((300, 250, 50, 50))
                pygame.draw.rect(self.screen, (0, 255, 0), play_button)
                pygame.draw.polygon(self.screen, (255, 255, 255), ((315, 260), (315, 290), (340, 275)))
                self.display.create_text((290, 310), (255, 255, 255), 32, "Play", self.screen)
            else:
                play_button = pygame.rect.Rect((300, 250, 50, 50))
                pygame.draw.rect(self.screen, (0, 255, 0), play_button)
                self.screen.blit(self.reload, (301, 250))
                self.display.create_text((238, 200), (255, 255, 255), 50, "GAME  OVER", self.screen)
                self.display.create_text((250, 310), (255, 255, 255), 32, "Play Again", self.screen)
            home_button = pygame.rect.Rect((460, 250, 50, 50))
            pygame.draw.rect(self.screen, (0, 0, 255), home_button)
            pygame.draw.polygon(self.screen, (255, 255, 255), ((465, 270), (505, 270), (485, 255)))
            pygame.draw.rect(self.screen, (255, 255, 255), (465, 270, 15, 20))
            pygame.draw.rect(self.screen, (255, 255, 255), (491, 270, 15, 20))
            pygame.draw.rect(self.screen, (255, 255, 255), (465, 270, 40, 7.5))
            self.display.create_text((445, 310), (255, 255, 255), 32, "Home", self.screen)

            self.ball.ball_x_speed = 0
            self.ball.ball_y_speed = 0
            self.y_speed = 0
            if play_button.collidepoint((get_mouse_pos())):
                if self.click:
                    print("clicked play button")
                    self.ball.ball_x_speed = ball_x_speed
                    self.ball.ball_y_speed = ball_y_speed
                    self.y_speed = 8
                    running = False
            if home_button.collidepoint((get_mouse_pos())):
                if self.click:
                    print("Clicked Home button")
                    self.ball.ball_x_speed = ball_x_speed
                    self.ball.ball_y_speed = ball_y_speed
                    self.y_speed = 8
                    return True
            pygame.display.update()
        return

    def run_game(self):
        running = True
        while running:
            pygame.time.Clock().tick(120)
            self.click = False
            self.score.left_color = self.left_paddle.color
            self.score.right_color = self.right_paddle.color
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.reset_game()
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN:

                    if event.button == 1:
                        self.click = True
            keys = pygame.key.get_pressed()
            self.screen.fill((0, 0, 0))
            # Draw the paddles
            right_pad = pygame.draw.rect(self.screen, self.right_paddle.color,
                                         (
                                             self.right_paddle.x_cord, self.right_paddle.y_cord,
                                             self.right_paddle.width, self.right_paddle.height))
            left_pad = pygame.draw.rect(self.screen, self.left_paddle.color,
                                        (self.left_paddle.x_cord, self.left_paddle.y_cord, self.left_paddle.width,
                                         self.left_paddle.height))

            # Checks to see if a key is pressed if one is then move a paddle
            if keys[pygame.K_UP] and self.right_paddle.y_cord > 0:
                self.right_paddle.y_cord -= self.y_speed
            if keys[pygame.K_DOWN] and self.right_paddle.y_cord < 600 - self.right_paddle.height:
                self.right_paddle.y_cord += self.y_speed
            if keys[pygame.K_w] and self.left_paddle.y_cord > 0:
                self.left_paddle.y_cord -= self.y_speed
            if keys[pygame.K_s] and self.left_paddle.y_cord < 600 - self.left_paddle.height:
                self.left_paddle.y_cord += self.y_speed

            # Drawing the ball and ball movement
            game_ball = pygame.draw.rect(self.screen, self.ball.color,
                                         (self.ball.x_cord, self.ball.y_cord, self.ball.width, self.ball.height))

            if self.ball.ball_moving_state:
                # Ball movement and collision with wall
                if 575 > self.ball.y_cord > 0:
                    self.ball.y_cord += self.ball.ball_y_speed
                    self.ball.x_cord += self.ball.ball_x_speed
                else:
                    self.ball.ball_y_speed *= -1
                    self.ball.y_cord += self.ball.ball_y_speed
            else:
                if keys[pygame.K_SPACE]:
                    self.ball.ball_moving_state = True
                self.display.display_continue_message(self.screen, (49, 51, 53))

            if right_pad.colliderect(game_ball) or left_pad.colliderect(game_ball):
                self.ball.ball_x_speed *= -1
                for _ in range(2):
                    self.ball.x_cord += self.ball.ball_x_speed
                self.ball.ball_x_speed *= 1.1

            # reset ball if goes past the paddle
            if self.ball.x_cord < 0 or self.ball.x_cord > 770:
                self.ball.ball_moving_state = False
                if self.ball.x_cord < 30:
                    self.score.right_score += 1
                    self.ball.ball_x_speed = self.default_ball_speed
                elif self.ball.x_cord > 770:
                    self.score.left_score += 1
                    self.ball.ball_x_speed = self.default_ball_speed
                    self.ball.ball_x_speed *= -1
                self.ball.reset_ball()

            mx, my = pygame.mouse.get_pos()

            # score
            self.score.show_score(self.screen, (255, 255, 255))
            pause_button = pygame.rect.Rect((380, 0, 50, 50))
            pygame.draw.rect(self.screen, (0, 0, 0), pause_button)
            self.display.create_text((391, 0), (255, 255, 255), 50, "ll", self.screen)
            if pause_button.collidepoint((mx, my)):
                if self.click:
                    print("clicked pause")
                    if self.pause_screen(self.ball.ball_x_speed, self.ball.ball_y_speed, "pause"):
                        self.reset_game()
                        print("going home")
                        return True

            pygame.display.update()

            # Game over
            if self.score.game_over():
                self.score.reset_score()
                if self.pause_screen(self.ball.ball_x_speed, self.ball.ball_y_speed, "game_over"):
                    self.reset_game()
                    return True
