import os
import sys

import pygame

pygame.init()
fps = 50
screen = pygame.display.set_mode((550, 550))
clock = pygame.time.Clock()
player = None
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()


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


tiles_type = {
    'empty': load_image('grass.png'),
    'wall': load_image('box.png')

}


class Tile(pygame.sprite.Sprite):
    def __init__(self, til, x, y):
        super().__init__(tiles_group)
        self.image = tiles_type[til]
        self.rect = self.image.get_rect()
        self.rect = self.rect.move((x, y))


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
    return new_player, x, y


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["Перемещение героя", "", "Герой движется", "Фон стоит"]

    fon = pygame.transform.scale(load_image('fon.jpg'), (500, 500))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 50)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(fps)


def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


tile_images = {'wall': load_image('box.png'), 'empty': load_image('grass.png')}
player_image = load_image('mar.png')

tile_width = tile_height = 50


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(tile_height * pos_x + 15, tile_width * pos_y + 5)

    def move(self, der):
        if der == 'up':
            if player.rect.y > 0 and level[(player.rect.x - 15) // 50 - 1][(player.rect.y - 5) // 50 - 2] != '#':
                player.rect.y -= 50
        elif der == 'down':
            if player.rect.y > 0 and level[(player.rect.x - 15) // 50 + 1][(player.rect.y - 5) // 50 - 2] != '#':
                player.rect.y += 50
        elif der == 'left':
            if player.rect.x > 0 and level[(player.rect.x - 15) // 50][(player.rect.y - 5) // 50 - 3] != '#':
                player.rect.x -= 50
        elif der == 'right':
            if player.rect.x > 0 and level[(player.rect.x - 15) // 50][(player.rect.y - 5) // 50 - 1] != '#':
                player.rect.x += 50


class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - 500 // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - 500 // 2)


running = True
start_screen()
level = load_level('map1.txt')
player, level_x, level_y = generate_level(level)
camera = Camera()
#####
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            player.move('up')
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            player.move('down')
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            player.move('left')
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            player.move('right')
    screen.fill((0, 0, 0))
    camera.update(player)
    for sprite in all_sprites:
        camera.apply(sprite)
    all_sprites.draw(screen)
    tiles_group.draw(screen)
    player_group.draw(screen)
    pygame.display.flip()
    clock.tick(fps)
#####
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
