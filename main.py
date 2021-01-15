import pygame
import display
import paddle
import ball
import score


pygame.init()
y_speed = 15
pygame.display.set_caption("Pong")

ball = ball.Ball()
score = score.Score()
display = display.Display()
screen = display.screen

left_paddle = paddle.Paddle("left")
right_paddle = paddle.Paddle("right")
game_active = False


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        game_active = True

    while game_active:
        screen.fill((0, 0, 0))
        #Draw the paddles
        right_pad = pygame.draw.rect(screen, right_paddle.color,
                         (right_paddle.x_cord, right_paddle.y_cord, right_paddle.width, right_paddle.height))
        left_pad = pygame.draw.rect(screen, left_paddle.color, (left_paddle.x_cord, left_paddle.y_cord, left_paddle.width, left_paddle.height))

        #Drawing the ball and ball movement
        game_ball = pygame.draw.rect(screen, ball.color, (ball.x_cord, ball.y_cord, ball.width, ball.height))

        #collision with wall
        if ball.y_cord < 575 and ball.y_cord > 0:
            ball.y_cord += ball.ball_y_speed
            ball.x_cord += ball.ball_x_speed
        else:
            ball.ball_y_speed *= -1
            ball.y_cord += ball.ball_y_speed

        if right_pad.colliderect(game_ball) or left_pad.colliderect(game_ball):
            ball.ball_x_speed *= -1
            for _ in range(2):
                ball.x_cord += ball.ball_x_speed
            ball.ball_x_speed *= 1.1

        # reset ball if goes past the paddle
        if ball.x_cord < 30 or ball.x_cord > 770:

            if ball.x_cord < 30:
                score.right_score += 1
                score.show_score(screen)
            elif ball.x_cord > 770:
                score.left_score += 1
                score.show_score(screen)
            ball.ball_x_speed *= -1
            ball.reset_ball()
            ball.ball_x_speed = 5

        #score
        score.show_score(screen)

        #Game over
        score.game_over()

        #Checks to see if a key is pressed if one is then move a paddle
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and right_paddle.y_cord > 0:
            right_paddle.y_cord -= y_speed
        if keys[pygame.K_DOWN] and right_paddle.y_cord < 600 - right_paddle.height:
            right_paddle.y_cord += y_speed
        if keys[pygame.K_w] and left_paddle.y_cord > 0:
            left_paddle.y_cord -= y_speed
        if keys[pygame.K_s] and left_paddle.y_cord < 600 - left_paddle.height:
            left_paddle.y_cord += y_speed

        #quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_active = False
                running = False

        pygame.display.update()
        pygame.time.delay(40)
    display.display_start_message(screen)
    pygame.display.update()


pygame.quit()