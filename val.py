import random
import pygame
from engine import load_image, start_screen, Fon, Figure, tiles_group, Checking_sistem, all_sprites,Miniature

pygame.init()
fps = 1
clock = pygame.time.Clock()
figures = ['rect', 'I', 'T', 'L1', 'L2', 'Z1', 'Z2']
screen = pygame.display.set_mode((400, 500))
box_image = load_image('box.png')
running = True
mini = Miniature()
fon_image = load_image('tetris.png')
next_figure = random.choice(figures)
figure = Figure(next_figure)
next_figure = random.choice(figures)
mini.move(next_figure)
fon = Fon()
start_screen()
check = Checking_sistem()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == 273:
            figure.turn()
        if event.type == pygame.KEYDOWN and event.key == 275:
            figure.right()
        if event.type == pygame.KEYDOWN and event.key == 276:
            figure.left()
        if event.type == pygame.KEYDOWN and event.key == 274:
            if figure.down():
                figure = Figure(next_figure)
                next_figure = random.choice(figures)
    screen.fill((0, 0, 0))
    check.check()
    if figure.down():
        figure = Figure(next_figure)
        next_figure = random.choice(figures)
        mini.move(next_figure)
    tiles_group.draw(screen)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(fps)
#####
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
