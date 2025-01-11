import pygame, sys, random
def draw_floor():
    screen.blit(floor,(floor_x_pos,650))
    screen.blit(floor,(floor_x_pos+432,650))
def create_pipe():
    random_pipe_pos = random.choice((pipe_height))
    bottom_pipe = pipe_surface.get_rect(midtop = (500,random_pipe_pos))
    if score >=5:
        top_pipe = pipe_surface.get_rect(midtop = (500,random_pipe_pos-650))
    if score >=3:
        top_pipe = pipe_surface.get_rect(midtop = (500,random_pipe_pos-670))
    else: 
        top_pipe = pipe_surface.get_rect(midtop = (500,random_pipe_pos-695))
    
    return bottom_pipe, top_pipe     
def move_pipe(pipes):            
    for pipe in pipes:
        pipe.centerx -= 2.6   
    return pipes
def craw_pipe(pipes):
    for pipe  in pipes:
        if pipe.bottom >= 450:
            screen.blit(pipe_surface,pipe)
        else:
            flip_pipe = pygame. transform.flip(pipe_surface,False,True)
            screen.blit(flip_pipe,pipe)
def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            hit_sound.play()
            return False
        if bird_rect.bottom>=650 or bird_rect.top<=-75:
            return False
    return True
def rorate_bird(birds):
    new_bird = pygame.transform.rotozoom(birds,-bird_movement*3,1)
    return new_bird
def bird_animation():
    new_bird = bird_list[bird_index]
    new_bird_rect = new_bird.get_rect(center=(100,bird_rect.centery))
    return new_bird, new_bird_rect
def score_display(game_state):
    if game_state == 'main_game':
        score_surface = game_font.render(str(int(score)),True,(255,255,255))
        score_rect = score_surface.get_rect(center = (216,100))
        screen.blit(score_surface,score_rect)
    if game_state == 'game_over':
        score_surface = game_font.render(str(int(score)),True,(255,255,255))
        score_rect = score_surface.get_rect(center = (216,100))
        screen.blit(score_surface,score_rect)
     
        hight_score_surface = game_font.render("High Score: " + str(int(hight_score)),True,(255,127,80))
        hight_score_rect = score_surface.get_rect(center = (109,730))
        screen.blit(hight_score_surface,hight_score_rect)
def update_score(score,hight_score):
    if score>hight_score:
        hight_score = score
    return hight_score
pygame.init()
from pygame import mixer
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
screen=pygame.display.set_mode((432,768))
clock = pygame.time.Clock()
game_font = pygame.font.Font('D:/Workspace/python/game/Flappy Bird/04B_19.ttf',40)
gravity= 0.25
bird_movement=0
game = False
passed_pipes =[]
   
score = 0
hight_score = 0
#TIÊu ĐỀ
pygame.display.set_caption('Flappy Bird')
#BACKGROUND
backgrounds = pygame.image.load('D:/Workspace/python/game/Flappy Bird/assets/background-night.png')
backgrounds = pygame.transform.scale2x(backgrounds)
#FLOOR  
floor = pygame.image.load('D:/Workspace/python/game/Flappy Bird/assets/floor.png')
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0
#CHIM
bird_down = pygame.image.load('D:/Workspace/python/game/Flappy Bird/assets/yellowbird-downflap.png')
bird_down = pygame.transform.scale2x(bird_down)
bird_mid= pygame.image.load('D:/Workspace/python/game/Flappy Bird/assets/yellowbird-midflap.png')
bird_mid = pygame.transform.scale2x(bird_mid)
bird_up= pygame.image.load('D:/Workspace/python/game/Flappy Bird/assets/yellowbird-upflap.png')
bird_up = pygame.transform.scale2x(bird_up)
bird_list = [bird_down,bird_mid,bird_up]
bird_index = 0 
bird = bird_list[bird_index]
bird_rect = bird.get_rect(center=(100,384))
#CHIM ĐẬP CÁNH
birdflap = pygame.USEREVENT + 1
pygame.time.set_timer(birdflap,200)
# MÀN HÍNH KẾT THÚC
game_over = pygame.image.load('D:/Workspace/python/game/Flappy Bird/assets/message.png')
game_over = pygame.transform.scale2x(game_over)
game_over_rect = game_over.get_rect(center=(216,384))
# TẠO ỐNG   
pipe_surface = pygame.image.load('D:/Workspace/python/game/Flappy Bird/assets/pipe-green.png')
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list =[]
#tao timer
spawnpipe = pygame.USEREVENT
pygame.time.set_timer(spawnpipe,1700)
pipe_height = [200,225,250,300,325,277,522,555,376,350,380,400,425,475,600]

bird_ceiling = 650 - bird.get_height()
#ÂM THANH
flap_sound = pygame.mixer.Sound('D:/Workspace/python/game/Flappy Bird/sound/sfx_wing.wav')
hit_sound = pygame.mixer.Sound('D:/Workspace/python/game/Flappy Bird/sound/sfx_hit.wav')
score_sound = pygame.mixer.Sound('D:/Workspace/python/game/Flappy Bird/sound/sfx_point.wav')
down_sound = pygame.mixer.Sound('D:/Workspace/python/game/Flappy Bird/sound/sfx_swooshing.wav')
backgroud_sound = mixer.music.load('D:/Workspace/python/game/Flappy Bird/sound/Piano-Sonata-Kufurstensonate-In-D-Major-WoO-47-No-3-1-Allegro-U-Staerk-Various-Artists.wav')
mixer.music.play()
#ẢNH MỚI
nam = pygame.image.load('D:/Workspace/python/game/Flappy Bird/assets/pixilart-drawing (1).png')
# 
while True: 
    for even in pygame.event.get():
        if even.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if even.type == pygame.KEYDOWN:
            if even.key == pygame.K_SPACE and game:
                bird_movement = 0
                bird_movement -= 6.5
                flap_sound.play()
                

            
            if even.key == pygame.K_SPACE and game == False:
                game = True
                pipe_list.clear()
                score = 0
                bird_movement=0
                bird_rect = bird.get_rect(center=(100,384))
                
                
        if even.type == spawnpipe:
            pipe_list.extend(create_pipe())
        if even.type == birdflap:
            if bird_index<2:
                bird_index += 1
            else:
                bird_index= 0
            bird, bird_rect = bird_animation()

    screen.blit(backgrounds,(0,0)) 
    if game:
        bird_movement += gravity   
        rotated_bird = rorate_bird(bird)
        bird_rect.centery += bird_movement
        if bird_rect.top >= bird_ceiling:
            bird_rect.top = bird_ceiling
        screen.blit(rotated_bird,bird_rect)
        game = check_collision(pipe_list)
        pipe_list = move_pipe(pipe_list)
        craw_pipe(pipe_list)
        for pipe in pipe_list:
            if pipe.right < bird_rect.left and pipe not in passed_pipes:
                passed_pipes.append(pipe)
                score_sound.play()
                score += 0.5 
                
        
        floor_x_pos -=2.6
        draw_floor()
        if  floor_x_pos<=-432:
            floor_x_pos=0
        score_display('main_game')
        screen.blit(nam,(0,0))
    else:
        screen.blit(game_over,game_over_rect)
        
        draw_floor()
        hight_score = update_score(score,hight_score)
        score_display('game_over')
    
   
    pygame.display.update()
    clock.tick(120)
