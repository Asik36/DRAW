import pygame , sys
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
(screenWidth, screenHeight) = (1500.0, 900.0)
screen = pygame.display.set_mode((screenWidth, screenHeight))

drawing = False
temp = None
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
        if pygame.mouse.get_pos() != temp:
            incline = pygame.mouse.get_pos()[1] - temp[1]/pygame.mouse.get_pos()[0] - temp[0]

            for i in range(max(pygame.mouse.get_pos()[0], temp[0]),min(pygame.mouse.get_pos()[0], temp[0])):
                print("f")
    pygame.display.flip()
    clock.tick(60)
    temp = pygame.mouse.get_pos()
