import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))
sound = pygame.mixer.Sound('2.wav')
sound.play()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))
    pygame.display.flip()

pygame.quit()
