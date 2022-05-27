import pygame
last_pos = None
now_pos = None

class DrawSurf(pygame.sprite.Sprite):
    def __init__(self, w, h):
        super().__init__()
        self.image = pygame.Surface([w, h], pygame.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        self.musk = pygame.mask.from_surface(self.image)

    def reset(self):
        global bool, last_pos, now_pos
        last_pos = None
        now_pos = None


    def drawing(self):
        global last_pos, now_pos

        new_pos = pygame.mouse.get_pos()
        if last_pos is None:
            last_pos = new_pos
            
        else:
            pygame.draw.line(self.image, (255, 0, 0), last_pos, new_pos, 10)

        last_pos = new_pos


