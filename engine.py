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
small_box_image = load_image('minibox.png')


class Line(pygame.sprite.Sprite):
    def __init__(self, y, group):
        super().__init__(group)
        self.image = line_imege
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(15, y)
        self.bal = 0

    def check(self):
        colliding_quantity = 0
        for collide_test in tiles_group:
            if pygame.sprite.collide_mask(self, collide_test):
                colliding_quantity += 1
        if colliding_quantity == 10:
            pygame.sprite.spritecollide(self, tiles_group, dokill=True)
            self.bal += 100
            redowning = pygame.sprite.Group()
            for picsel in tiles_group:
                if picsel.down():
                    redowning.add(picsel)
                for pic in redowning:
                    pic.down()

    def bals(self):
        return self.bal

    def down(self):
        pass


class Checking_sistem:
    def __init__(self):
        self.line1 = Line(485, check_group)
        self.line2 = Line(455, check_group)
        self.line3 = Line(425, check_group)
        self.line4 = Line(395, check_group)
        self.line5 = Line(365, check_group)
        self.line6 = Line(335, check_group)
        self.line7 = Line(305, check_group)
        self.line8 = Line(275, check_group)
        self.line9 = Line(245, check_group)
        self.line10 = Line(215, check_group)
        self.line11 = Line(185, check_group)
        self.line12 = Line(155, check_group)
        self.line13 = Line(125, check_group)
        self.line14 = Line(95, check_group)
        self.line_check = Line(515, check_group)
        self.line = Line(545, all_sprites)

    def check(self):
        self.line14.check()
        self.line13.check()
        self.line12.check()
        self.line11.check()
        self.line10.check()
        self.line9.check()
        self.line8.check()
        self.line7.check()
        self.line6.check()
        self.line5.check()
        self.line4.check()
        self.line3.check()
        self.line2.check()
        self.line1.check()
        return self.line_check.bals()


class Fon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.image = fon_image
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(-5, -5)

    def down(self):
        pass


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
        for collide_test in all_sprites:
            if pygame.sprite.collide_mask(self, collide_test):
                colliding_quantity += 1
        if colliding_quantity:
            return False
        return True

    def down(self):
        self.rect = self.rect.move(0, 30)
        colliding_quantity = -1
        for collide_test in all_sprites:
            if pygame.sprite.collide_mask(self, collide_test):
                colliding_quantity += 1
        if colliding_quantity:
            self.rect = self.rect.move(0, -30)
            return True
        return False

    def left(self):
        self.rect = self.rect.move(-30, 0)
        colliding_quantity = -1
        for collide_test in all_sprites:
            if pygame.sprite.collide_mask(self, collide_test):
                colliding_quantity += 1
        if colliding_quantity:
            self.rect = self.rect.move(30, 0)
            return True
        return False

    def right(self):
        self.rect = self.rect.move(30, 0)
        colliding_quantity = -1
        for collide_test in all_sprites:
            if pygame.sprite.collide_mask(self, collide_test):
                colliding_quantity += 1
        if colliding_quantity:
            self.rect = self.rect.move(-30, 0)
            return True
        return False

    def line(self, y):
        self.rect.y = y


class Small_picsel(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.image = small_box_image
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x, y)

    def move(self, x, y):
        self.rect.x = x
        self.rect.y = y


class Figure:
    def __init__(self, figure_type):
        self.figure_type = figure_type
        if self.figure_type == 'Z1':
            self.pics1 = Picsel(90, 20)
            self.pics2 = Picsel(120, 20)
            self.pics3 = Picsel(120, 50)
            self.pics4 = Picsel(150, 50)
            self.rotate = 1
        if self.figure_type == 'Z2':
            self.pics1 = Picsel(120, 20)
            self.pics2 = Picsel(150, 20)
            self.pics3 = Picsel(90, 50)
            self.pics4 = Picsel(120, 50)
            self.rotate = 1
        if self.figure_type == 'L1':
            self.pics1 = Picsel(90, 20)
            self.pics2 = Picsel(120, 20)
            self.pics3 = Picsel(150, 20)
            self.pics4 = Picsel(150, 50)
            self.rotate = 1
        if self.figure_type == 'L2':
            self.pics1 = Picsel(90, 20)
            self.pics2 = Picsel(120, 20)
            self.pics3 = Picsel(150, 20)
            self.pics4 = Picsel(90, 50)
            self.rotate = 1
        if self.figure_type == 'T':
            self.pics1 = Picsel(90, 20)
            self.pics2 = Picsel(120, 20)
            self.pics3 = Picsel(150, 20)
            self.pics4 = Picsel(120, 50)
            self.rotate = 1
        if self.figure_type == 'I':
            self.pics1 = Picsel(90, 20)
            self.pics2 = Picsel(120, 20)
            self.pics3 = Picsel(150, 20)
            self.pics4 = Picsel(180, 20)
            self.rotate = 1
        if self.figure_type == 'rect':
            self.pics1 = Picsel(120, 20)
            self.pics2 = Picsel(150, 20)
            self.pics3 = Picsel(120, 50)
            self.pics4 = Picsel(150, 50)
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
                self.pics3.move(-60, 30)
                self.pics4.move(-30, 0)
                if self.pics4.movecontrol() and self.pics3.movecontrol() \
                        and self.pics2.movecontrol() and self.pics1.movecontrol():
                    self.rotate = 2
                else:
                    self.pics1.move(-30, 30)
                    self.pics3.move(60, -30)
                    self.pics4.move(30, 0)
            elif self.rotate == 2:
                self.pics1.move(-30, 0)
                self.pics2.move(-30, 0)
                self.pics3.move(30, -30)
                self.pics4.move(30, -30)
                if self.pics4.movecontrol() and self.pics3.movecontrol() \
                        and self.pics2.movecontrol() and self.pics1.movecontrol():
                    self.rotate = 3
                else:
                    self.pics1.move(30, 0)
                    self.pics2.move(30, 0)
                    self.pics3.move(30, 30)
                    self.pics4.move(-30, 30)
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

    def gameover(self):
        go = self.pics4.movecontrol() and self.pics3.movecontrol() and self.pics2.movecontrol() \
             and self.pics1.movecontrol()
        return not go


class Miniature:
    def __init__(self):
        self.pics1 = Small_picsel(-20, -20)
        self.pics2 = Small_picsel(-20, -20)
        self.pics3 = Small_picsel(-20, -20)
        self.pics4 = Small_picsel(-20, -20)

    def move(self, figure_type):
        if figure_type == 'Z2':
            self.pics1.move(340, 30)
            self.pics2.move(360, 30)
            self.pics3.move(320, 50)
            self.pics4.move(340, 50)
        if figure_type == 'Z1':
            self.pics1.move(320, 30)
            self.pics2.move(340, 30)
            self.pics3.move(340, 50)
            self.pics4.move(360, 50)
        if figure_type == 'L2':
            self.pics1.move(320, 30)
            self.pics2.move(340, 30)
            self.pics3.move(360, 30)
            self.pics4.move(320, 50)
        if figure_type == 'L1':
            self.pics1.move(320, 30)
            self.pics2.move(340, 30)
            self.pics3.move(360, 30)
            self.pics4.move(360, 50)
        if figure_type == 'T':
            self.pics1.move(320, 30)
            self.pics2.move(340, 30)
            self.pics3.move(360, 30)
            self.pics4.move(340, 50)
        if figure_type == 'I':
            self.pics1.move(310, 40)
            self.pics2.move(330, 40)
            self.pics3.move(350, 40)
            self.pics4.move(370, 40)
        if figure_type == 'rect':
            self.pics1.move(330, 30)
            self.pics2.move(350, 30)
            self.pics3.move(330, 50)
            self.pics4.move(350, 50)
