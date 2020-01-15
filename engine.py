import os

import pygame

pygame.init()
fps = 1
clock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 500))
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
check_group = pygame.sprite.Group()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def start_screen():
    fon = pygame.transform.scale(load_image('fon.jpg'), (400, 500))
    screen.blit(fon, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(fps)


box_image = load_image('box.png')
fon_image = load_image('tetris.png')
line_imege = load_image('check_line.png')


class Fon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(tiles_group, all_sprites)
        self.image = fon_image
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(-5, -5)


class Picsel(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(tiles_group, all_sprites)
        self.image = box_image
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x, y)

    def move(self, x, y):
        self.rect = self.rect.move(x, y)

    def movecontrol(self):
        colliding_quantity = -1
        for collide_test in tiles_group:
            if pygame.sprite.collide_mask(self, collide_test):
                colliding_quantity += 1
        if colliding_quantity:
            return False
        return True

    def down(self):
        self.rect = self.rect.move(0, 30)
        colliding_quantity = -1
        for collide_test in tiles_group:
            if pygame.sprite.collide_mask(self, collide_test):
                colliding_quantity += 1
        if colliding_quantity:
            self.rect = self.rect.move(0, -30)
            return True
        return False

    def left(self):
        self.rect = self.rect.move(-30, 0)
        colliding_quantity = -1
        for collide_test in tiles_group:
            if pygame.sprite.collide_mask(self, collide_test):
                colliding_quantity += 1
        if colliding_quantity:
            self.rect = self.rect.move(30, 0)
            return True
        return False

    def right(self):
        self.rect = self.rect.move(30, 0)
        colliding_quantity = -1
        for collide_test in tiles_group:
            if pygame.sprite.collide_mask(self, collide_test):
                colliding_quantity += 1
        if colliding_quantity:
            self.rect = self.rect.move(-30, 0)
            return True
        return False


class Figure:
    def __init__(self, figure_type):
        self.figure_type = figure_type
        if self.figure_type == 'Z1':
            self.pics1 = Picsel(90, 10)
            self.pics2 = Picsel(120, 10)
            self.pics3 = Picsel(120, 40)
            self.pics4 = Picsel(150, 40)
            self.rotate = 1
        if self.figure_type == 'Z2':
            self.pics1 = Picsel(120, 10)
            self.pics2 = Picsel(150, 10)
            self.pics3 = Picsel(90, 40)
            self.pics4 = Picsel(120, 40)
            self.rotate = 1
        if self.figure_type == 'L1':
            self.pics1 = Picsel(90, 10)
            self.pics2 = Picsel(120, 10)
            self.pics3 = Picsel(150, 10)
            self.pics4 = Picsel(150, 40)
            self.rotate = 1
        if self.figure_type == 'L2':
            self.pics1 = Picsel(90, 10)
            self.pics2 = Picsel(120, 10)
            self.pics3 = Picsel(150, 10)
            self.pics4 = Picsel(90, 40)
            self.rotate = 1
        if self.figure_type == 'T':
            self.pics1 = Picsel(90, 10)
            self.pics2 = Picsel(120, 10)
            self.pics3 = Picsel(150, 10)
            self.pics4 = Picsel(120, 40)
            self.rotate = 1
        if self.figure_type == 'I':
            self.pics1 = Picsel(90, 10)
            self.pics2 = Picsel(120, 10)
            self.pics3 = Picsel(150, 10)
            self.pics4 = Picsel(180, 10)
            self.rotate = 1
        if self.figure_type == 'rect':
            self.pics1 = Picsel(120, 10)
            self.pics2 = Picsel(150, 10)
            self.pics3 = Picsel(120, 40)
            self.pics4 = Picsel(150, 40)
            self.rotate = 1

    def turn(self):
        if self.figure_type == 'Z1':
            if self.rotate:
                self.pics1.move(30, 0)
                self.pics2.move(-30, 30)
                self.pics4.move(-60, 30)
                if self.pics4.movecontrol() and self.pics3.movecontrol() \
                        and self.pics2.movecontrol() and self.pics1.movecontrol():
                    self.rotate = 0
                else:
                    self.pics1.move(-30, 0)
                    self.pics2.move(30, -30)
                    self.pics4.move(60, -30)
            else:
                self.pics1.move(-30, 0)
                self.pics2.move(30, -30)
                self.pics4.move(60, -30)
                if self.pics4.movecontrol() and self.pics3.movecontrol() \
                        and self.pics2.movecontrol() and self.pics1.movecontrol():
                    self.rotate = 1
                else:
                    self.pics1.move(30, 0)
                    self.pics2.move(-30, 30)
                    self.pics4.move(-60, 30)
        if self.figure_type == 'Z2':
            if self.rotate:
                self.pics2.move(-30, 30)
                self.pics3.move(60, 0)
                self.pics4.move(30, 30)
                if self.pics4.movecontrol() and self.pics3.movecontrol() \
                        and self.pics2.movecontrol() and self.pics1.movecontrol():
                    self.rotate = 0
                else:
                    self.pics2.move(30, -30)
                    self.pics3.move(-60, 0)
                    self.pics4.move(-30, -30)
            else:
                self.pics2.move(30, -30)
                self.pics3.move(-60, 0)
                self.pics4.move(-30, -30)
                if self.pics4.movecontrol() and self.pics3.movecontrol() \
                        and self.pics2.movecontrol() and self.pics1.movecontrol():
                    self.rotate = 1
                else:
                    self.pics2.move(-30, 30)
                    self.pics3.move(60, 0)
                    self.pics4.move(30, 30)
        if self.figure_type == 'L1':
            if self.rotate == 1:
                self.pics1.move(30, -30)
                self.pics3.move(-30, 30)
                self.pics4.move(-60, 0)
                if self.pics4.movecontrol() and self.pics3.movecontrol() \
                        and self.pics2.movecontrol() and self.pics1.movecontrol():
                    self.rotate = 2
                else:
                    self.pics1.move(-30, 30)
                    self.pics3.move(30, -30)
                    self.pics4.move(60, 0)
            elif self.rotate == 2:
                self.pics1.move(-30, 0)
                self.pics2.move(-30, 0)
                self.pics3.move(0, -30)
                self.pics4.move(60, -30)
                if self.pics4.movecontrol() and self.pics3.movecontrol() \
                        and self.pics2.movecontrol() and self.pics1.movecontrol():
                    self.rotate = 3
                else:
                    self.pics1.move(30, 0)
                    self.pics2.move(30, 0)
                    self.pics3.move(0, 30)
                    self.pics4.move(-60, 30)
            elif self.rotate == 3:
                self.pics1.move(30, 0)
                self.pics2.move(60, -30)
                self.pics4.move(-30, 30)
                if self.pics4.movecontrol() and self.pics3.movecontrol() \
                        and self.pics2.movecontrol() and self.pics1.movecontrol():
                    self.rotate = 0
                else:
                    self.pics1.move(-30, 0)
                    self.pics2.move(-60, 30)
                    self.pics4.move(30, -30)
            else:
                self.pics1.move(-30, 30)
                self.pics2.move(-30, 30)
                self.pics3.move(30, 0)
                self.pics4.move(30, 0)
                if self.pics4.movecontrol() and self.pics3.movecontrol() \
                        and self.pics2.movecontrol() and self.pics1.movecontrol():
                    self.rotate = 1
                else:
                    self.pics1.move(30, -30)
                    self.pics2.move(30, -30)
                    self.pics3.move(-30, 0)
                    self.pics4.move(-30, 0)
        if self.figure_type == 'L2':
            if self.rotate == 1:
                self.pics1.move(0, -30)
                self.pics2.move(0, -30)
                self.pics3.move(-30, 0)
                self.pics4.move(30, 0)
                if self.pics4.movecontrol() and self.pics3.movecontrol() \
                        and self.pics2.movecontrol() and self.pics1.movecontrol():
                    self.rotate = 2
                else:
                    self.pics1.move(0, 30)
                    self.pics2.move(0, 30)
                    self.pics3.move(30, 0)
                    self.pics4.move(-30, 0)
            elif self.rotate == 2:
                self.pics1.move(60, 0)
                self.pics2.move(-30, 30)
                self.pics4.move(30, -30)
                if self.pics4.movecontrol() and self.pics3.movecontrol() \
                        and self.pics2.movecontrol() and self.pics1.movecontrol():
                    self.rotate = 3
                else:
                    self.pics1.move(-60, 0)
                    self.pics2.move(30, -30)
                    self.pics4.move(-30, 30)
            elif self.rotate == 3:
                self.pics1.move(-30, 0)
                self.pics2.move(30, 0)
                self.pics3.move(0, 30)
                self.pics4.move(0, 30)
                if self.pics4.movecontrol() and self.pics3.movecontrol() \
                        and self.pics2.movecontrol() and self.pics1.movecontrol():
                    self.rotate = 0
                else:
                    self.pics1.move(30, 0)
                    self.pics2.move(-30, 0)
                    self.pics3.move(0, -30)
                    self.pics4.move(0, -30)
            else:
                self.pics1.move(-30, 30)
                self.pics3.move(30, -30)
                self.pics4.move(-60, 0)
                if self.pics4.movecontrol() and self.pics3.movecontrol() \
                        and self.pics2.movecontrol() and self.pics1.movecontrol():
                    self.rotate = 1
                else:
                    self.pics1.move(30, -30)
                    self.pics3.move(-30, 30)
                    self.pics4.move(60, 0)
        if self.figure_type == 'T':
            if self.rotate == 1:
                self.pics1.move(30, -30)
                self.pics2.move(-30, 0)
                self.pics3.move(-30, 0)
                if self.pics4.movecontrol() and self.pics3.movecontrol() \
                        and self.pics2.movecontrol() and self.pics1.movecontrol():
                    self.rotate = 2
                else:
                    self.pics1.move(-30, 30)
                    self.pics2.move(30, 0)
                    self.pics3.move(30, 0)
            elif self.rotate == 2:
                self.pics4.move(30, -30)
                if self.pics4.movecontrol() and self.pics3.movecontrol() \
                        and self.pics2.movecontrol() and self.pics1.movecontrol():
                    self.rotate = 3
                else:
                    self.pics4.move(-30, 30)
            elif self.rotate == 3:
                self.pics2.move(30, 0)
                self.pics3.move(30, 0)
                self.pics4.move(-30, 30)
                if self.pics4.movecontrol() and self.pics3.movecontrol() \
                        and self.pics2.movecontrol() and self.pics1.movecontrol():
                    self.rotate = 0
                else:
                    self.pics2.move(-30, 0)
                    self.pics3.move(-30, 0)
                    self.pics4.move(30, -30)
            else:
                self.pics1.move(-30, 30)
                if self.pics4.movecontrol() and self.pics3.movecontrol() \
                        and self.pics2.movecontrol() and self.pics1.movecontrol():
                    self.rotate = 1
                else:
                    self.pics1.move(30, -30)
        if self.figure_type == 'I':
            if self.rotate == 1:
                self.pics1.move(30, -30)
                self.pics3.move(-30, 30)
                self.pics4.move(-60, 60)
                if self.pics4.movecontrol() and self.pics3.movecontrol() \
                        and self.pics2.movecontrol() and self.pics1.movecontrol():
                    self.rotate = 2
                else:
                    self.pics1.move(-30, 30)
                    self.pics3.move(30, -30)
                    self.pics4.move(60, - 60)
            elif self.rotate == 2:
                self.pics1.move(-60, 30)
                self.pics2.move(-30, 0)
                self.pics3.move(0, -30)
                self.pics4.move(30, -60)
                if self.pics4.movecontrol() and self.pics3.movecontrol() \
                        and self.pics2.movecontrol() and self.pics1.movecontrol():
                    self.rotate = 3
                else:
                    self.pics1.move(60, -30)
                    self.pics2.move(30, 0)
                    self.pics3.move(0, 30)
                    self.pics4.move(-30, 60)
            elif self.rotate == 3:
                self.pics1.move(60, -60)
                self.pics2.move(30, -30)
                self.pics4.move(-30, 30)
                if self.pics4.movecontrol() and self.pics3.movecontrol() \
                        and self.pics2.movecontrol() and self.pics1.movecontrol():
                    self.rotate = 0
                else:
                    self.pics1.move(-60, 60)
                    self.pics2.move(-30, 30)
                    self.pics4.move(30, -30)
            else:
                self.pics1.move(-30, 60)
                self.pics2.move(0, 30)
                self.pics3.move(30, 0)
                self.pics4.move(60, -30)
                if self.pics4.movecontrol() and self.pics3.movecontrol() \
                        and self.pics2.movecontrol() and self.pics1.movecontrol():
                    self.rotate = 1
                else:
                    self.pics1.move(30, -60)
                    self.pics2.move(0, -30)
                    self.pics3.move(-30, 0)
                    self.pics4.move(-60, 30)

    def down(self):
        if self.pics4.down():
            return True
        elif self.pics3.down():
            self.pics4.move(0, -30)
            return True
        elif self.pics2.down():
            self.pics3.move(0, -30)
            self.pics4.move(0, -30)
            return True
        elif self.pics1.down():
            self.pics2.move(0, -30)
            self.pics3.move(0, -30)
            self.pics4.move(0, -30)
            return True

    def right(self):
        if not self.pics4.right():
            if self.pics3.right():
                self.pics4.move(-30, 0)
            elif self.pics2.right():
                self.pics3.move(-30, 0)
                self.pics4.move(-30, 0)
            elif self.pics1.right():
                self.pics2.move(-30, 0)
                self.pics3.move(-30, 0)
                self.pics4.move(-30, 0)

    def left(self):
        if not self.pics1.left():
            if self.pics2.left():
                self.pics1.move(30, 0)
            elif self.pics3.left():
                self.pics2.move(30, 0)
                self.pics1.move(30, 0)
            elif self.pics4.left():
                self.pics3.move(30, 0)
                self.pics2.move(30, 0)
                self.pics1.move(30, 0)
