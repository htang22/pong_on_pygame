import pygame
import display
import game, sys



pygame.init()

pygame.display.set_caption("Pong")

game = game.Game()
display = display.Display()
screen = display.screen
game_count = 0

def start_menu():
    menu_running = True
    click = False
    while menu_running:

        screen.fill((0, 0, 0))
        start_button = pygame.Rect(300, 375, 200, 50)
        pygame.draw.rect(screen, (255, 255, 255), start_button)
        display.display_play_message(screen, (300, 385), (0, 0, 0))
        display.display_title(screen, (200, 100), (255, 255, 255), font=150)

        mx, my = pygame.mouse.get_pos()

        if start_button.collidepoint((mx, my)):
            if click:
                return True

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
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        game_active = True

    while game_active:
        game_active = game.run_game()
        game_count += 1

        #quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_active = False
                running = False

        pygame.display.update()
        pygame.time.delay(40)
    display.display_start_message(screen)

    if game_count != 0:
        display.display_game_over(screen)
    game_active = start_menu()
    pygame.display.update()

pygame.quit()