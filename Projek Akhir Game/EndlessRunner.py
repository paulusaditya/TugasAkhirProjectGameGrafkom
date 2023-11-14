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
pause = False

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Block Runner")
background_img = pygame.image.load('bagus.jpg')
bg_start = pygame.transform.scale(pygame.image.load('bagus.jpg'),(WIDTH,HEIGHT))
background = pygame.transform.scale(background_img,(WIDTH,HEIGHT))
fps = 60 
font = pygame.font.Font("Fonts/Natural Precision.ttf", 16)
timer = pygame.time.Clock()


def x():
    global active,obstacles,score,obstacles_speed,player
    if not pause:
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
# # Inisialisasi variabel bayangan ekor
# trail_length = 10  # Panjang trail
# trail_color = (255, 255, 0)  # Warna trail (misalnya kuning)
# player_trail = []  # Daftar pemain salinan untuk trail

def show_start_screen():
    pygame.mixer.music.stop()
    start_music ='Sky Jump.mp3'
    pygame.mixer.music.load(start_music)
    pygame.mixer.music.play(-1)

    start_font = pygame.font.Font('Fonts/Natural Precision.ttf', 46)
    exit_font = pygame.font.Font('Fonts/Natural Precision.ttf', 46)
    nama_font = pygame.font.Font('Fonts/Natural Precision.ttf', 76)

    start_text = start_font.render("Start", True, (0, 0, 0))
    exit_text = exit_font.render("Exit", True, (0, 0, 0))
    nama_text = nama_font.render("Block Runner", True, (0, 0, 0))


    start_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    exit_rect = exit_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 130))
    nama_rect = nama_text.get_rect(center=(WIDTH//2, 100))

    start_screen = True
    while start_screen:
        screen.blit(bg_start, (0, 0))
        screen.blit(start_text, start_rect)
        screen.blit(exit_text, exit_rect)
        screen.blit(nama_text,nama_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start_rect.collidepoint(mouse_pos):
                    start_screen = False
                    pygame.mixer.music.stop()
                    break
                elif exit_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    quit()

show_start_screen()
music_lvl1 = pygame.mixer.music.load('Sky Jump.mp3')
pygame.mixer.music.play(-1)

running = True
while running:
    timer.tick(fps)
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    screen.blit(background, (i, 0))
    screen.blit(background, (WIDTH+i, 0))

    i -= obstacles_speed
    if i <= -WIDTH:
        i = 0
        screen.blit(background, (i, 0))
        screen.blit(background, (i + WIDTH, 0))


    if not active : 
        instructions_text = font.render(f'Space Bar to Start', True,black)
        screen.blit(instructions_text, (800,100))
        instructions_text2 = font.render(f'Space Bar Jumps', True,black)
        screen.blit(instructions_text2, (800,140))

    score_text = font.render(f"Score : {score}", True, black)
    screen.blit(score_text,(100,100))
    tanah = pygame.draw.rect(screen, green, [0,630, WIDTH,10])
    player = pygame.draw.rect(screen, purple, [player_x, player_y, 25, 25])
    obstacle0 = pygame.draw.rect(screen, red, [obstacles[0], 630,100,20])
    obstacle1 = pygame.draw.rect(screen, red, [obstacles[1], 630,100,20])
    obstacle2 = pygame.draw.rect(screen, red, [obstacles[2], 630,100,20])

    if pause:
        restart,quit = draw_pause()

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and not active:
            if event.key == pygame.K_SPACE:
                obstacles = [600, 900, 1280]
                player_x = 50
                score = 0
                active = True
                running = True

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

    for obstacle in [obstacle0, obstacle1, obstacle2]:
        if player.colliderect(obstacle):
            active = False
            running = False
    x()
    

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





    #     # Tambahkan pemain saat ini ke daftar pemain trail
    # player_trail.append(player.copy())
    # if len(player_trail) > trail_length:
    #     player_trail.pop(0)  # Hapus salinan yang paling tua jika daftar terlalu panjang

    # # Gambar salinan pemain dengan warna trail
    # for i, trail_player in enumerate(player_trail):
    #     trail_surface = pygame.Surface((25, 25), pygame.SRCALPHA)
    #     pygame.draw.rect(trail_surface, trail_color, (0, 0, 25, 25))
    #     screen.blit(trail_surface, trail_player)

    
    # pygame.display.flip()
    pygame.display.update()
pygame.quit()
