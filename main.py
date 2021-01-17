import pygame
import display, paddle
import game, sys, ball

pygame.init()

pygame.display.set_caption("Pong")

ball = ball.Ball()
right_paddle = paddle.Paddle("right")
left_paddle = paddle.Paddle("left")
game = game.Game(left_paddle, right_paddle)
display = display.Display()
screen = display.screen
game_count = 0
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
global color_rect
color_rect = []
global rectangles
rectangles = []

colors = [WHITE, (255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 255, 0), (1, 50, 32), (77, 77, 255), (0, 0, 255),
          (128, 0, 128), (127, 0, 255)]


def color_menu():
    def create_colors(x_cord):
        n = 50 + x_cord

        for number in range(10):
            if number <= 4:
                dimensions = (n, 200, 50, 50)
                n += 60
                rect = create_rect(dimensions, colors[number])
                rectangles.append(rect)
                color_rect.append(colors[number])

            else:
                n -= 60
                dimensions = (n, 260, 50, 50)
                rect = create_rect(dimensions, colors[number])
                rectangles.append(rect)
                color_rect.append(colors[number])

    while True:
        screen.fill((0, 0, 0))
        ball.random_moving_ball(screen)
        create_colors(0)
        create_colors(400)
        click = False
        display.create_text((50, 100),WHITE, 50,"Left Paddle", screen)
        display.create_text((450, 100), WHITE, 50, "Right Paddle", screen)


        mx, my = pygame.mouse.get_pos()
        quit_to_start = create_rect((290, 400, 230, 60),colors[1])
        display.create_text((295, 400), WHITE, 35, "Quit to menu", screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    print("click")

        if quit_to_start.collidepoint((mx, my)):
            if click:
                break

        for rect in rectangles:
            if rect.collidepoint((mx, my)):
                if click:
                    number = rectangles.index(rect)
                    if mx < 400:
                        left_paddle.color = colors[number]
                    else:
                        right_paddle.color = color_rect[number]

        pygame.display.update()


def create_rect(dimension, color):
    name = pygame.Rect(dimension)
    pygame.draw.rect(screen, color, name)
    return name



def start_menu():
    menu_running = True
    click = False
    while menu_running:

        screen.fill((0, 0, 0))
        ball.random_moving_ball(screen)
        start_button = create_rect((300, 375, 200, 50), (WHITE))
        color_button = create_rect((300, 450, 200, 50), (WHITE))
        display.display_play_message(screen, (300, 385), (0, 0, 0))
        display.display_title(screen, (200, 100), (255, 255, 255), font=150)
        display.create_text((300, 460), (BLACK), 32, "Paddle color", screen)

        mx, my = pygame.mouse.get_pos()
        if start_button.collidepoint((mx, my)):
            if click:
                return True
        if color_button.collidepoint((mx, my)):
            if click:
                color_menu()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    print("click")
        pygame.display.update()


game_active = False

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     game_active = True

    while game_active:
        game_active = game.run_game()
        if game.run_game() == False:
            quit()
        game_count += 1

        # quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_active = False
                running = False


    display.display_start_message(screen)

    if game_count != 0:
        display.display_game_over(screen)
    game_active = start_menu()
    pygame.display.update()
pygame.quit()
