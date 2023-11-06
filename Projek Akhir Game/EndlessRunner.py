import random
import pygame

pygame.init()

#Game Constants
white = (255,255,255)
black = (0,0,0)
blue =  (68,214,255)
green = (123,168,85)
purple = (97,12,159)
red = (216,0,50)
orange = (255, 176, 0)
yellow = (244, 232, 105)
brown = (154, 68, 68)

color = [blue,purple,red,orange,yellow]
WIDTH = 1280
HEIGHT = 720 
i = 0



#Game Variabels
score = 0
player_x = 100
player_y = 10
y_change = 0 
x_change = 0
gravity = 1
obstacles = [900,1050,1280]
obstacles_speed = 5
active = False

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Block Runner")
background_img = pygame.image.load('bagus.jpg')
background = pygame.transform.scale(background_img,(WIDTH,HEIGHT))
fps = 60
font = pygame.font.Font("freesansbold.ttf", 16)
timer = pygame.time.Clock()


# Inisialisasi variabel bayangan ekor
trail_length = 10  # Panjang trail
trail_color = (255, 255, 0)  # Warna trail (misalnya kuning)
player_trail = []  # Daftar pemain salinan untuk trail


running = True
while running:
    timer.tick(fps)
    screen.fill((0,0,0))
    screen.blit(background, (0, 0))
    screen.blit(background, (i,0))
    screen.blit(background, (WIDTH+i, 0))

    if i == -WIDTH:
        screen.blit(background, (WIDTH+i, 0))
        i= 0
    i -= 1

    if not active : 
        instructions_text = font.render(f'Space Bar to Start', True,black,blue)
        screen.blit(instructions_text, (800,100))
        instructions_text2 = font.render(f'Space Bar Jumps', True,black,blue)
        screen.blit(instructions_text2, (800,140))
    score_text = font.render(f"Score : {score}", True, black, blue)
    screen.blit(score_text,(100,100))
    tanah = pygame.draw.rect(screen, green, [0,630, WIDTH,10])
    player = pygame.draw.rect(screen, yellow, [player_x, player_y, 25, 25])
    obstacle0 = pygame.draw.rect(screen, red, [obstacles[0], 630,100,20])
    obstacle1 = pygame.draw.rect(screen, red, [obstacles[1], 630,100,20])
    obstacle2 = pygame.draw.rect(screen, red, [obstacles[2], 630,100,20])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and not active:
            if event.key == pygame.K_SPACE:
                obstacles = [600,900,1280]
                player_x = 50
                score = 0
                active = True

        if event.type == pygame.KEYDOWN and active:
            if event.key == pygame.K_SPACE and y_change == 0:
                y_change = 30
            if event.key == pygame.K_RIGHT:
                x_change = 10
            if event.key == pygame.K_LEFT:
                x_change = -10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                x_change = 0
            if event.key == pygame.K_LEFT:
                x_change = 0

    for i in range (len(obstacles)):
        if active:
            obstacles[i] -= obstacles_speed
            if obstacles[i] < -720:
                obstacles[i] = random.randint(1100, 1280)
                score += 1

            if score % 5 == 0:  # Contoh: Tingkatkan setiap 5 poin
                    obstacles_speed += 0.01  # Atau sesuaikan peningkatan sesuai keinginan

            if player.colliderect(obstacle0) or player.colliderect(obstacle1) or player.colliderect(obstacle2):
                active = False

    if 0 <= player_x <= 1800:
        player_x += x_change
    if player_x < 0:
        player_x = 0
    if player_x > 1800:
        player_x = 1800


    if y_change > 0 or player_y <630:
        player_y -= y_change
        y_change -= gravity
    if player_y > 630:
        player_y = 630
    if player_y == 630 and y_change < 0:
        y_change = 0

        # Tambahkan pemain saat ini ke daftar pemain trail
    player_trail.append(player.copy())
    if len(player_trail) > trail_length:
        player_trail.pop(0)  # Hapus salinan yang paling tua jika daftar terlalu panjang

    # Gambar salinan pemain dengan warna trail
    for i, trail_player in enumerate(player_trail):
        trail_surface = pygame.Surface((25, 25), pygame.SRCALPHA)
        pygame.draw.rect(trail_surface, trail_color, (0, 0, 25, 25))
        screen.blit(trail_surface, trail_player)

    
    # pygame.display.flip()
    pygame.display.update()
pygame.quit()
