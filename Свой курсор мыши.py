import pygame
import os


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)

    return image

pygame.init()
width, height = 500, 500
size = width, height
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))

clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
cursor_image = load_image('arrow.png')
cursor = pygame.sprite.Sprite(all_sprites)
cursor.image = cursor_image
cursor.rect = cursor.image.get_rect()
pygame.mouse.set_visible(False)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            cursor.rect.topleft = event.pos
    screen.fill((0, 0, 0))
    if pygame.mouse.get_focused():
        all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
pygame.quit()
