import pygame


pygame.init()
# win_width = 1000
# win_height = 500
win = pygame.display.set_mode ((1000, 500))
bg_img = pygame.image.load('Projek Akhir Game/bagus.jpg')
background= pygame.transform.scale(bg_img, (1000,500))

width = 1000
i = 0


def display():
    global i

    win.fill((0,0,0))
    win.blit(background, (0, 0))
    win.blit(background, (i,0))
    win.blit(background, (width+i, 0))

    if i == -width:
        win.blit(background, (width+i, 0))
        i= 0
    i -= 1
   

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display()
    pygame.display.update()

pygame.quit()