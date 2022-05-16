import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, size_x, size_y, speed = 6):
        super().__init__()
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x, self.y, size_x, size_y)
        self.size_x = size_x
        self.size_y = size_y
        self.color = (250, 120, 60)
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = speed

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

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