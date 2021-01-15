import pygame
import display
import game


pygame.init()

pygame.display.set_caption("Pong")

game = game.Game()
display = display.Display()
screen = display.screen
game_count = 0


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
    pygame.display.update()

pygame.quit()