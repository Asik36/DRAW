import pygame


def run_once(f):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)

    wrapper.has_run = False
    return wrapper


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, size_x, size_y, speed=6):
        super().__init__()

        self.image = pygame.Surface((size_x, size_y))
        self.rect = self.image.get_rect()
        self.musk = pygame.mask.from_surface(self.image)
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y
        self.image.fill((250, 120, 60))
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.shift_pressed = False

        self.speed = speed
        self.speed_original = speed

    def out_of_bounds(self, width, height):
        if self.rect.right >= width:
            self.right_pressed = False
            self.x = width - self.size_x
        if self.rect.left <= 0:
            self.left_pressed = False
            self.x = 0
        if self.rect.top <= 0:
            self.up_pressed = False
            self.y = 0
        if self.rect.bottom >= height:
            self.down_pressed = False
            self.y = height - self.size_y

    #@run_once
    def stop(self):
        self.speed = 0

    #@run_once
    def go(self):
        self.speed = 8

    def fast(self):
        self.speed *= 3

    def slow(self):
        self.speed = self.speed_original

    def update(self):
            self.velX = 0
            self.velY = 0
            if self.left_pressed and not self.right_pressed:
                self.velX = -self.speed
            if self.right_pressed and not self.left_pressed:
                self.velX = self.speed
            if self.up_pressed and not self.down_pressed:
                self.velY = -self.speed
            if self.down_pressed and not self.up_pressed:
                self.velY = self.speed

            self.x += self.velX
            self.y += self.velY
            self.rect = pygame.Rect(int(self.x), int(self.y), self.size_x, self.size_y)


class Eye(pygame.sprite.Sprite):
    def __init__(self, p):
        super().__init__()
        self.image = pygame.Surface((3, p.size_y))
        self.image.fill((60, 150, 30))
        self.rect = self.image.get_rect()
        self.musk = pygame.mask.from_surface(self.image)
        self.p = p

    def collide(self, surface):
        if pygame.sprite.spritecollide(self, surface, False, pygame.sprite.collide_mask):
            self.image.fill((30, 150, 200))
            return True
        else:
            self.image.fill("green")
            return False


    def update(self):
        if self.p.right_pressed:
            self.rect.topleft = self.p.rect.topright
        elif self.p.left_pressed:
            self.rect.topright = self.p.rect.topleft


