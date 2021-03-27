import pygame

pygame.init()

# RGB (255, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
C = (100, 100, 100)

size = (400, 500)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("PyGame example")

text_rotate_degrees = 1
clock = pygame.time.Clock() # FPS

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)
    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render("Programming Technologies", True, BLACK)
    text = pygame.transform.rotate(text, text_rotate_degrees)
    screen.blit(text, (100, 100))
    text_rotate_degrees += 1
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
