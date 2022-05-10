import pygame , sys
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
(screenWidth, screenHeight) = (1500.0, 900.0)
screen = pygame.display.set_mode((screenWidth, screenHeight))

drawing = False
last_pos = None
now_pos = None
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False

    if drawing:
        pygame.draw.circle(screen, (255, 0, 0), pygame.mouse.get_pos(), 15)
        if pygame.mouse.get_pos() != last_pos:
            incline = pygame.mouse.get_pos()[1] - last_pos[1] / pygame.mouse.get_pos()[0] - last_pos[0]

            for i in range(min(pygame.mouse.get_pos()[0], last_pos[0]), max(pygame.mouse.get_pos()[0], last_pos[0])):
                print(i)
                pygame.draw.circle(screen, (255, 0, 0), (pygame.mouse.get_pos()[0]+i, pygame.mouse.get_pos()[1]+incline, 15))

    pygame.display.flip()
    clock.tick(60)
    last_pos = pygame.mouse.get_pos()
