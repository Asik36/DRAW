import pygame


last_pos = None
now_pos = None


def reset():
    global bool, last_pos, now_pos
    last_pos = None
    now_pos = None


def drawing(screen):
    global last_pos, now_pos

    new_pos = pygame.mouse.get_pos()
    if last_pos is None:
        last_pos = new_pos

    else:
        pygame.draw.line(screen, (255, 0, 0), last_pos, new_pos, 10)

    last_pos = new_pos
