import sys

import pygame

import ball
import display
import game
import paddle

# Inititizes the game and set the screen name
pygame.init()
pygame.display.set_caption("Pong")

# Creating all the objects and variable in the game.
ball = ball.Ball()
right_paddle = paddle.Paddle("right")
left_paddle = paddle.Paddle("left")
game = game.Game(left_paddle, right_paddle, ball)
display = display.Display()
screen = display.screen
# game_count = 0
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
global ball_speed
ball_speed = []
global color_rect
color_rect = []
global rectangles
rectangles = []
colors = [WHITE, (255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 255, 0), (1, 50, 32), (77, 77, 255), (0, 0, 255),
          (128, 0, 128), (127, 0, 255)]


def create_rect(dimension, color):
    """Takes the dimension (x_cord, y_cord, rect_width, rect_height) of the desired rectangle and color and create a rectangle returns the name the rect angle """
    name = pygame.Rect(dimension)
    pygame.draw.rect(screen, color, name)
    return name


def game_menu():
    """The game menu is the function to change the ball speed and paddle colors"""

    def create_colors(x_cord):
        """The x_cord of the desired placement of the colors and then creates the colors. Then creates the ball speed modes and lets the user choose what colors and speed they want. Breaks out of loop and function once the user quits"""
        n = 50 + x_cord
        # Creates the rectangle and colors then adds them to a list to be later used to decide what rectangle was pressed
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

    def create_ball_speed_mode():
        """Creates the ball speed mode and rectangles to show which speeds"""
        n = 50
        display.create_text((15, 370), WHITE, 50, "Ball Speed", screen)

        for number in range(0, 3):
            dimensions = (n, 450, 50, 50)
            create_rect((n - 2, 448, 54, 54), (WHITE))
            rect = create_rect(dimensions, (0, 0, 0))
            ball_speed.append(rect)
            n += 60
        display.create_text((55, 460), WHITE, 32, "1x", screen)
        display.create_text((115, 460), WHITE, 32, "2x", screen)
        display.create_text((175, 460), WHITE, 32, "3x", screen)

    # Loop to chek if buttons are pressed
    while True:
        # Calls the create colors function and ball speed modes which creates rectangles
        screen.fill((0, 0, 0))
        ball.random_moving_ball(screen)
        create_colors(0)
        create_colors(400)
        create_ball_speed_mode()
        click = False
        display.create_text((50, 100), WHITE, 50, "Left Paddle", screen)
        display.create_text((450, 100), WHITE, 50, "Right Paddle", screen)

        # Check the mouse position and creates the quit button
        mx, my = pygame.mouse.get_pos()
        quit_to_start = create_rect((290, 400, 230, 60), colors[1])
        display.create_text((295, 415), WHITE, 35, "Quit to menu", screen)
        pygame.display.update()

        # Checks to see if the user quits or presses the mouse. If they press the mouse down then it will return click as True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    print("click")

        # if the mouse position and click are on the quit button/rect breaks out of game menu
        if quit_to_start.collidepoint((mx, my)):
            if click:
                break

        # Checks to see if any of the rect/buttons for the ball speed are pressed if they are then speed is set to speeds.
        for rect in ball_speed:
            if rect.collidepoint((mx, my)):
                if click:
                    if rect[0] == 50:
                        print("Left")
                        if ball.ball_x_speed > 0:
                            ball.ball_x_speed = 2
                        else:
                            ball.ball_x_speed = -2
                    elif rect[0] == 110:
                        print("Middle")
                        if ball.ball_x_speed > 0:
                            ball.ball_x_speed = 4
                        else:
                            ball.ball_x_speed = -4
                    else:
                        print("Right")
                        if ball.ball_x_speed > 0:
                            ball.ball_x_speed = 6
                        else:
                            ball.ball_x_speed = -6

        # Check to see if the any of the color buttons/rect have been pressed if they have then the color is set to the corresponding paddle
        for rect in rectangles:
            if rect.collidepoint((mx, my)):
                if click:
                    number = rectangles.index(rect)
                    if mx < 400:
                        left_paddle.color = colors[number]
                    else:
                        right_paddle.color = color_rect[number]


def start_menu():
    """The starting menu creates a randomly moving ball, teh title pong and 2 buttons teh start button which runs the game and teh game menu which brings up the game menu which then the player could change the game settings."""
    menu_running = True
    click = False
    while menu_running:

        # Creates the random moving ball and start and game menu button. Shows the title as well.
        screen.fill((0, 0, 0))
        ball.random_moving_ball(screen)
        start_button = create_rect((300, 375, 200, 50), WHITE)
        game_menu_button = create_rect((300, 450, 200, 50), WHITE)
        display.display_play_message(screen, (300, 385), (0, 0, 0))
        display.display_title(screen, (200, 100), (255, 255, 255), font=150)
        display.create_text((305, 460), BLACK, 33, "Game Menu", screen)

        # check to see what button is pressed if the game_menu_button is pressed then calls the game_menu function if the start_button is pressed then call the run game function from teh game object
        mx, my = pygame.mouse.get_pos()
        if start_button.collidepoint((mx, my)):
            if click:
                game.run_game(ball.ball_x_speed)
        if game_menu_button.collidepoint((mx, my)):
            if click:
                game_menu()

        # Checks to see if the user quits or presses the mouse. If they press the mouse down then it will return click as True
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    print("click")
        pygame.display.update()


game_active = False
# Main game loop
running = True
while running:
    # Checks to see if the user quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     game_active = True

    # while the start menu active
    while start_menu():
        # Checks to see if the game is still active if the user quits using the exit button then exits the program if the user presses home button then calls the start menu.
        game_active = game.run_game()
        if not game.run_game():
            quit()
        if game.run_game():
            start_menu()
        # game_count += 1

        # quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_active = False
                running = False

    # display.display_start_message(screen)
    #
    # if game_count != 0:
    #     display.display_game_over(screen)
    pygame.display.update()
pygame.quit()
