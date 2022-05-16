import pygame, sys

import draw
from player import *


def out_of_bounds():
    if player.rect.right >= screenWidth:
        player.right_pressed = False
        player.x = screenWidth - player.size_x
    if player.rect.left <= 0:
        player.left_pressed = False
        player.x = 0
    if player.rect.top <= 0:
        player.up_pressed = False
        player.y = 0
    if player.rect.bottom >= screenHeight:
        player.down_pressed = False
        player.y = screenHeight - player.size_y


if __name__ == "__main__":

    # general settings
    pygame.init()
    pygame.font.init()
    clock = pygame.time.Clock()

     # Window settings
    (screenWidth, screenHeight) = (1500, 900)
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    game_surf = pygame.Surface([screenWidth, screenHeight], pygame.SRCALPHA, 32)
    game_surf = game_surf.convert_alpha()

    player = Player(300, 300, 100, 100)
    player_group = pygame.sprite.GroupSingle(player)
    drawing_bool = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing_bool = True
            if event.type == pygame.MOUSEBUTTONUP:
                drawing_bool = False
                draw.reset()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.left_pressed = True
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.right_pressed = True
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    player.up_pressed = True
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    player.down_pressed = True
                if event.key == pygame.K_LSHIFT:
                    player.speed = 100
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.left_pressed = False
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.right_pressed = False
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    player.up_pressed = False
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    player.down_pressed = False
                if event.key == pygame.K_LSHIFT:
                    player.speed = 6
        out_of_bounds()

        if drawing_bool:
            draw.drawing(game_surf)
        player_group.update()
        player.draw(screen)
        pygame.display.flip()
        screen.fill((12, 24, 36))
        screen.blit(game_surf,  (0, 0))
        clock.tick(60)

