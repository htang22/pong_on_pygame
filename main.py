import pygame
import display
import paddle

pygame.init()
y_speed = 15
# screen = pygame.display.set_mode(size=(600,600))
pygame.display.set_caption("Pong")

display = display.Display()
screen = display.screen
left_paddle = paddle.Paddle("left")
right_paddle = paddle.Paddle("right")


running = True
while running:
    pygame.time.delay(100)
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, right_paddle.color,
                     (right_paddle.x_cord, right_paddle.y_cord, right_paddle.width, right_paddle.height))
    pygame.draw.rect(screen, left_paddle.color, (left_paddle.x_cord, left_paddle.y_cord, left_paddle.width, left_paddle.height))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and right_paddle.y_cord > 0:
        right_paddle.y_cord -= y_speed
    if keys[pygame.K_DOWN] and right_paddle.y_cord < 600 - right_paddle.height:
        right_paddle.y_cord += y_speed
    if keys[pygame.K_w] and left_paddle.y_cord > 0:
        left_paddle.y_cord -= y_speed
    if keys[pygame.K_s] and left_paddle.y_cord < 600 - left_paddle.height:
        left_paddle.y_cord += y_speed

        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
pygame.quit()