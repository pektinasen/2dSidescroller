from character import Char
import pygame

pygame.init()

size = [400,300]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("example")
test_image = pygame.image.load("char.png")

ch1 = Char(test_image,[0,300])

#Loop through
clock = pygame.time.Clock()
done = False

while not done:
    clock.tick(10)   
    screen.fill((255,255,255))
    screen.blit(ch1.show_yourself(),ch1.pos)

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            ch1.jump()
