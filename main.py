import pygame, sys

import draw
from player import *





if __name__ == "__main__":

    # general settings
    pygame.init()
    pygame.font.init()
    clock = pygame.time.Clock()

    # Window settings
    (screenWidth, screenHeight) = (1500, 900)
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    dr = draw.DrawSurf(screenWidth, screenHeight)
    draw_screen = pygame.sprite.GroupSingle(dr)



    # player
    p = Player(300, 300, 100, 100)
    player_group = pygame.sprite.GroupSingle(p)

    eye = Eye(p)
    eye_group = pygame.sprite.GroupSingle(eye)

    drawing_bool = False

    collition_left = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing_bool = True
            if event.type == pygame.MOUSEBUTTONUP:
                drawing_bool = False
                draw_screen.sprite.reset()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player_group.sprite.left_pressed = True
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player_group.sprite.right_pressed = True
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    player_group.sprite.up_pressed = True
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    player_group.sprite.down_pressed = True
                if event.key == pygame.K_LSHIFT:
                    p.fast()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player_group.sprite.left_pressed = False
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player_group.sprite.right_pressed = False
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    player_group.sprite.up_pressed = False
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    player_group.sprite.down_pressed = False
                if event.key == pygame.K_LSHIFT:
                    p.slow()
        player_group.sprite.out_of_bounds(screenWidth, screenHeight)

        if drawing_bool and pygame.mouse.get_pos() != 3:
            draw_screen.sprite.drawing()

        # collide
        if eye.collide(draw_screen) and (player_group.sprite.right_pressed or player_group.sprite.left_pressed):
            p.stop()
        elif not eye.collide(draw_screen):
            p.go()

        # update
        player_group.update()
        player_group.draw(screen)
        if player_group.sprite.left_pressed or player_group.sprite.right_pressed or player_group.sprite.up_pressed or \
                player_group.sprite.down_pressed:

            eye_group.update()
            eye_group.draw(screen)
        # draw
        pygame.display.flip()
        screen.fill((12, 24, 36))
        screen.blit(draw_screen.sprite.image, (0, 0))
        clock.tick(60)
        #print(int(clock.get_fps()))

