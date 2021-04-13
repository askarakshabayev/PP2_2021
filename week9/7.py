import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

BLOCK_SIZE = 50

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_rect = screen.get_rect()

rects = []

for x in range(10):
    rects.append(pygame.Rect(x * (BLOCK_SIZE + 5), BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

selected = None

clock = pygame.time.Clock()
is_running = True

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                i = 0
                for r in rects:
                    if r.collidepoint(event.pos):
                        selected = i
                        selected_offset_x = r.x - event.pos[0]
                        selected_offset_y = r.y - event.pos[1]
                        break
                    i += 1

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                selected = None

        elif event.type == pygame.MOUSEMOTION:
            if selected is not None:  # selected can be `0` so `is not None` is required
                # move object
                rects[selected].x = event.pos[0] + selected_offset_x
                rects[selected].y = event.pos[1] + selected_offset_y
    screen.fill(BLACK)
    for r in rects:
        pygame.draw.rect(screen, RED, r)

    pygame.display.update()
    clock.tick(25)
pygame.quit()
