from random import randint 
import pygame

pygame.init()

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

score = 0
nilai = 0
gravity = 1
active = 0
background_x = 0


screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption('EndlessRunner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Fonts/Natural Precision.ttf', 50)

sky_surface = pygame.image.load('bagus.jpg').convert()
spike_surface = pygame.image.load('Idle1.png').convert_alpha()
spike_surface = pygame.transform.scale(spike_surface, (90, 45))
spike_surface1 = pygame.image.load('Spikedball.png').convert_alpha()
spike_surface1 = pygame.transform.scale(spike_surface1, (50, 50))

obstacle_rect_list = []

player_surface0 = pygame.image.load('Run_01.png').convert_alpha()
player_surface1 = pygame.image.load('Run_02.png').convert_alpha()
player_surface2 = pygame.image.load('Run_03.png').convert_alpha()
player_surface3 = pygame.image.load('Run_04.png').convert_alpha()
player_surface4 = pygame.image.load('Run_05.png').convert_alpha()
player_surface5 = pygame.image.load('Run_06.png').convert_alpha()
player_surface6 = pygame.image.load('Run_07.png').convert_alpha()
player_surface7 = pygame.image.load('Run_08.png').convert_alpha()
player_surface8 = pygame.image.load('Run_09.png').convert_alpha()
player_surface9 = pygame.image.load('Run_10.png').convert_alpha()
player_surface10 = pygame.image.load('Run_11.png').convert_alpha()
player_surface11 = pygame.image.load('Run_12.png').convert_alpha()

player_surface0 = pygame.transform.scale(player_surface0, (100, 100))
player_surface1 = pygame.transform.scale(player_surface1, (100, 100))
player_surface2 = pygame.transform.scale(player_surface2, (100, 100))
player_surface3 = pygame.transform.scale(player_surface3, (100, 100))
player_surface4 = pygame.transform.scale(player_surface4, (100, 100))
player_surface5 = pygame.transform.scale(player_surface5, (100, 100))
player_surface6 = pygame.transform.scale(player_surface6, (100, 100))
player_surface7 = pygame.transform.scale(player_surface7, (100, 100))
player_surface8 = pygame.transform.scale(player_surface8, (100, 100))
player_surface9 = pygame.transform.scale(player_surface9, (100, 100))
player_surface10 = pygame.transform.scale(player_surface10, (100, 100))
player_surface11 = pygame.transform.scale(player_surface11, (100, 100))

player_surf_walk = [player_surface0,player_surface1,player_surface2,player_surface3,player_surface4,player_surface5,player_surface6,player_surface7,player_surface8,player_surface9,player_surface10,player_surface11]
player_index = 0
player_jump = pygame.image.load('Jump.png').convert_alpha()
player_jump = pygame.transform.scale(player_jump, (100,100))

player_surf = player_surf_walk[player_index]
player_rect = player_surf.get_rect(topleft=(50,480))
player_gravity = 0

player_stand = pygame.image.load('Run_07.png').convert_alpha()
player_stand = pygame.transform.scale(player_stand,(300,300))
player_stand_rect = player_stand.get_rect(center = (640,360))

game_name = test_font.render('Freggie Jump',False,white)
game_rect = game_name.get_rect(center = (640,180))

massage = test_font.render('Press SPACE to start', False,white)
massage_rect = massage.get_rect(center = (640,550))

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)

def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - score
    score_surface = test_font.render(f'{current_time}', False, white)
    score_rect = score_surface.get_rect(center = (640,50))
    screen.blit(score_surface,score_rect)
    return current_time

def obs_movement(obs_list):
    if obs_list:
        for obs_rect in obs_list:
            obs_rect.x -=10
            if obs_rect.y == 590:
                screen.blit(spike_surface,obs_rect)
            else:
                screen.blit(spike_surface1,obs_rect)
        obs_list = [obs for obs in obs_list if obs.x > -100]
        return obs_list
    else: return []

def collisions(player,obstacles):
    if obstacles:
        for obs in obstacles:
            if player.colliderect(obs):
                return 0
    return 1 

def player_anim():
    global player_surf, player_index
    if player_rect.bottom < 630:
        player_surf = player_jump
    else:
        player_index +=0.25
        if player_index > len(player_surf_walk)-1: player_index = 0
        player_surf = player_surf_walk[int(player_index)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if active == 1:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    player_gravity = -20
        if active == 0:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    active = 1
                    score = int(pygame.time.get_ticks()/1000)
        if event.type == obstacle_timer and active == 1: 
            if randint(0,2):
                obstacle_rect_list.append(spike_surface.get_rect(topleft=(randint(1200,1500),590)))
            else:
                obstacle_rect_list.append(spike_surface1.get_rect(topleft=(randint(1200,1500),400)))

    screen.blit(sky_surface, (background_x, 0))
    screen.blit(sky_surface, (background_x + WIDTH, 0))

    background_x -= 5
    if background_x <= -WIDTH:
        background_x = 0
    
    if active == 1:
        player_anim()
        screen.blit(player_surf,player_rect)
        player_gravity +=1
        player_rect.y += player_gravity
        if player_rect.bottom >= 630: player_rect.bottom = 630
        obstacle_rect_list = obs_movement(obstacle_rect_list)
        nilai = display_score()
        active = collisions(player_rect,obstacle_rect_list)
    
    if active == 0:
        screen.blit(player_stand,player_stand_rect)
        screen.blit(game_name,game_rect)
        obstacle_rect_list.clear()
        player_rect.topleft=(50,480)
        gravity = 0
        score_massage = test_font.render(f'Your score: {nilai}',False,white)
        score_massage_rect = score_massage.get_rect(center = (640,550))
        if nilai == 0:
            screen.blit(massage,massage_rect)
        else:
            screen.blit(score_massage,score_massage_rect) 
        
    # currentframe = (currentframe + 1) % frame
    pygame.display.update()
    clock.tick(60)