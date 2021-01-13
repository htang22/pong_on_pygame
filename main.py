import pygame
import display
import paddle

pygame.init()

# screen = pygame.display.set_mode(size=(600,600))
pygame.display.set_caption("Pong")

display = display.Display()
screen = display.screen
left_paddle = paddle.Paddle("left")
right_paddle = paddle.Paddle("right")


running = True
while running:
    pygame.time.delay(100)
    pygame.draw.rect(screen, right_paddle.color,
                     (right_paddle.x_cord, right_paddle.y_cord, right_paddle.width, right_paddle.height))
    pygame.draw.rect(screen, left_paddle.color, (left_paddle.x_cord, left_paddle.y_cord, left_paddle.width, left_paddle.height))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()