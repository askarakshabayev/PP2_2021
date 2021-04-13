import pygame
windowSize = (500,500)
white = (255,255,255)
black = (0,0,0)

pygame.init()
screen = pygame.display.set_mode(windowSize)
running = 1

screen.fill(white)
while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            rect = pygame.Rect(event.dict["pos"],(30,50))
            pygame.draw.rect(screen,black,rect,1)
    pygame.display.flip()