#If user wants to see leaderboard database, leaderboard.show_all(), leaderboard.show_many(), leaderboard.add(username, score)

#!Importing and Initialising of PyGame
import sqlite3
import pygame
from pygame.locals import *
from pygame import mixer 
pygame.init()
pygame.mixer.pre_init()

#?Importing Libraries
import sys
import time
import random

#!Importing other python files, Leaderboards and Button
from button import Button
import leaderboard

#?Setting up PyGame Clock
mainClock = pygame.time.Clock()
mainClock.tick(60)

'''cars_to_avoid = {
    '1':pygame.image.load('greencar.png'),
    '2':pygame.image.load('redcar.png'),
    '3':pygame.image.load('bluecar.png'),
    '4':pygame.image.load('yellowcar.png'),
    '5':pygame.image.load('purplecar.png'),
    '6':pygame.image.load('blackcar.png')
}'''
cars_to_avoid = pygame.image.load('car2.png')
user_player_car = pygame.image.load('car1.png')

#!Setting up PyGame screen and the caption on the top
pygame.display.set_caption("Shomail's Highway Menace Game")
menu_background = pygame.image.load('Background.jpeg')
game_bg = pygame.image.load('BG.png')
width, height = 1280, 720
screen_menu = pygame.display.set_mode((width, height))

#?Loading up the music
pygame.mixer.music.load('mainmenu background sound.wav') #!The background music
pygame.mixer.music.play(-1) #!Will play on repeat 
menu_select_sound = pygame.mixer.Sound('select.wav') #!The sound when selecting an option from the menu



#!Setting up variables for shapes and boundaries used in the future
'''len1, len2, x, y, X, Y, W, H = 45, 100, 0, 50, 275, 375, 50, 50'''
Key_X = 275
Key_y = 375
x = 0
y = 0
x1 = 0
y1 = -2500
#score_value = 0
cars_passed = 0
score = 0
points = 0
frames = 0

#?Setting up a function, so that size of the font can differ
def game_text(size):
    return pygame.font.Font("/Users/shomail/Desktop/NEA STUFF/pythonProject2/nokiafc22.ttf", size)

#!Setting up Boolean Logics that will be used when the user interacts with their keyboard and mouse
Left = False
Right = False
click = False
pause = False

#?Setting up the keyboard function taking inputs from the user and the car moves
def keyboard_input(keys):
    global Key_X, Key_y, Left, Right
    if keys[pygame.K_UP] == 1:
        if Key_y < 20:
            Key_y = Key_y - 5
    if keys[pygame.K_DOWN] == 1:
        if Key_y > 375:
            Key_y = Key_y + 5
    if keys[pygame.K_LEFT] == 1 and Left == False:
        Left = True
        if Key_X > 980:
            Key_X = 980
    elif keys[pygame.K_LEFT] == 0 and Left == True:
        Left = False
    if keys[pygame.K_RIGHT] == 1 and Right == False:
        Right = True
        if Key_X < 305:
            Key_X = 305
    elif keys[pygame.K_RIGHT] == 0 and Right == True:
        Right = False

#!Used to draw the shape that the user will see
def draw_shape():
    screen_menu.fill("Black")
    pygame.draw.rect(screen_menu, "Black", (Key_X, Key_y, 50, 50))

#?This is used in the Button function that allows the user to select an option on the menu and takes them to wherever selected
def draw_text(text, myfont, color, surface, x, y):
    textobj = myfont.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def game_menu():

    menu_background = pygame.image.load('Background.jpeg')
    game_bg = pygame.image.load('BG.png')
    width, height = 1280, 720
    screen_menu = pygame.display.set_mode((width, height))

    while True:
        
        screen_menu.blit(menu_background, (0, 0))

        m_menu = pygame.mouse.get_pos()

        menu = game_text(50).render("Shomail's Highway", True, "#ed8e2f")
        menu_box = menu.get_rect(center=(640, 100))
        screen_menu.blit(menu, menu_box)

        second_menu = game_text(50).render("Menace Game", True, "#ed8e2f")
        second_menu_box = second_menu.get_rect(center=(640, 170))
        screen_menu.blit(second_menu, second_menu_box)

        select_play = Button(pygame.image.load("play_button.png"), (640, 300), "PLAY", game_text(45), "#d7fcd4", "Black")
        select_instructions = Button(pygame.image.load("instructions_button.png"), (640, 400), "INSTRUCTIONS", game_text(45), "#d7fcd4", "Black")
        select_options = Button(pygame.image.load("options_button.png"), (640, 500), "OPTIONS", game_text(45), "#d7fcd4", "Black")
        select_quit = Button(pygame.image.load("quit_button.png"), (640, 600), "QUIT", game_text(45), "#d7fcd4", "Black")
       

        for button in [select_play, select_options, select_quit, select_instructions]:
            button.changeColor(m_menu)
            button.update(screen_menu)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if select_play.checkForInput(m_menu):
                    pygame.mixer.music.fadeout(1000)
                    play()
                if select_options.checkForInput(m_menu):
                    menu_select_sound.play()
                    options()
                if select_instructions.checkForInput(m_menu):
                    instructions()
                    menu_select_sound.play()
                if select_quit.checkForInput(m_menu):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def play():
    global y, x, y1, x1, score
    x_change = 0
    frames = 0
    y2 =7
    avoid_car_speed = 0
    width, height = 1280, 720
    opposition_instance = Opposition()
    game_screen = pygame.display.set_mode((width, height))
    score_value = 0
    
    bg_game = pygame.image.load("BG_new_game.png")
    running = True
    while running:
        
        frames += 1
        
        pause = True
        game_screen.blit(bg_game, (0,0))
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    paused()
         
        x+=x_change
        y2+=avoid_car_speed
           
        pos = pygame.mouse.get_pos()

        all_sprites.update()
        hits = pygame.sprite.spritecollide(player_instance, e, False)
        if hits:
            pass
        
        y1 += 5
        y += 5
    
        if not opposition_instance.alive():
            opposition_instance = Opposition()
        
        if frames%20 == 0:    
         
            frames = 0
         
            for i, inst in enumerate(e):
                if inst.rect.y >= (height - 50):
                    score += 10
                    inst.kill()
                    opposition_instance = Opposition()
                    e.add(opposition_instance)
                all_sprites.draw(game_screen)
                all_sprites.update()
            
                
        score_Text = game_text(20).render("Score: " + str(score), True, "White")
        game_screen.blit(score_Text, (50, 30))
    
        score_value = 0
        if not pygame.sprite.collide_mask(player_instance, opposition_instance):
            print("L")
        
        if pygame.sprite.collide_mask(player_instance, opposition_instance):
            print("W")
            
        if y > 2500:
            y = -2500
        if y1 > 2500:
            y1 = -2500
        all_sprites.draw(game_screen)
        
        m_play = pygame.mouse.get_pos()
        
        select_pause = Button(pygame.image.load("pause_button.png"), (1150, 50), "PAUSE", game_text(25), "#d7fcd4", "Black")
        for button in [select_pause]:
                button.changeColor(m_play)
                button.update(screen_menu)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if select_pause.checkForInput(m_play):
                        paused()
                        pygame.mixer.music.fadeout(1000)
        pygame.display.flip()
        pygame.display.update()


def paused():
    global pause
    pause = True
    while pause:
        
        
            m_pause = pygame.mouse.get_pos()
        
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()            
            
            paused = game_text(50).render("GAME PAUSE", True, "#ed8e2f")
            paused_box = paused.get_rect(center=(640, 150))
            screen_menu.blit(paused, paused_box)

            paused_line1 = game_text(30).render("SELECT RESUME TO CARRY ON PLAYING", True, "#ffffff")
            paused_line1_box = paused_line1.get_rect(center=(640, 350))
            screen_menu.blit(paused_line1, paused_line1_box)

            paused_line3 = game_text(30).render("SELECT MAIN MENU TO RETURN TO THE MAIN MENU", True, "#ffffff")
            paused_line3_box = paused_line3.get_rect(center=(640, 450))
            screen_menu.blit(paused_line3, paused_line3_box)

            select_resume = Button(pygame.image.load("play_button.png"), (250, 650), "RESUME", game_text(45), "#d7fcd4", "Black")
            select_return = Button(pygame.image.load("play_button.png"), (1000, 650), "MAIN MENU", game_text(45), "#d7fcd4", "Black")
            for button in [select_resume, select_return]:
                button.changeColor(m_pause)
                button.update(screen_menu)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if select_resume.checkForInput(m_pause):
                        
                        unpaused()
                    if select_return.checkForInput(m_pause):
                        pygame.mixer.music.fadeout(1000)
                        game_menu()
                        
            all_sprites.draw(game_screen)
            pygame.display.update()
            
score_value = 0
            
def unpaused():
    global pause
    pause=False

game_screen = pygame.display.set_mode((1280, 720))

def options():
    while True:
        m_options = pygame.mouse.get_pos()

        back_g = pygame.image.load("options_volume_scroller.png")

        screen_menu.fill("Black") 

        pygame.draw.rect(screen_menu, "#d7fcd4", pygame.Rect(485, 450, 300, 75))

        options_header = game_text(35).render("OPTIONS", True, "White")
        options_rect = options_header.get_rect(center=(640, 100))
        screen_menu.blit(options_header, options_rect)

        return_menu = Button(None, (640, 620), "BACK", game_text(75), "White", "#ccccff")

        circle_picture = pygame.image.load("volume_slider_circle.png")

        volume_circle = Button(circle_picture, (640, 360), "Suiiii", game_text(60), "Black",  "#ed8e2f")

        adjust_sound = game_text(35).render("Adjust Sound", True, "#ed8e2f")
        adjust_sound_box = adjust_sound.get_rect(center=(640, 415))
        screen_menu.blit(adjust_sound, adjust_sound_box)

        zero_sound = game_text(35).render("0%", True, "#ed8e2f")
        zero_sound_box = zero_sound.get_rect(center=(450, 490))
        screen_menu.blit(zero_sound, zero_sound_box)

        max_sound = game_text(35).render("100%", True, "#ed8e2f")
        max_sound_box = max_sound.get_rect(center=(845, 490))
        screen_menu.blit(max_sound, max_sound_box)

        scroller_line = pygame.image.load("scroller_line.png")
        screen_menu.blit(scroller_line, (495, 483))



        return_menu.changeColor(m_options)
        return_menu.update(screen_menu)     

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_menu.checkForInput(m_options):
                    game_menu()
                    menu_select_sound.play()


        pygame.display.update()

def instructions():

    while True:
        m_instructions = pygame.mouse.get_pos()

        screen_menu.fill("Black")

        instructions_header = game_text(35).render("INSTRUCTIONS", True, "White")
        instructions_rect = instructions_header.get_rect(center=(640, 100))
        screen_menu.blit(instructions_header, instructions_rect)

        instructions_text = game_text(17).render("The police are chasing you, you must use the highway to escape!", True, "White")
        i_t_rect = instructions_text.get_rect(center=(640,250))
        screen_menu.blit(instructions_text, i_t_rect)

        i_text = game_text(17).render("But, be careful! Don't hit any cars, or it will be game over for you!", True, "White")
        i_text_rect = i_text.get_rect(center=(640,280))
        screen_menu.blit(i_text, i_text_rect)

        i_goodluck = game_text(55).render("GOOD LUCK!", True, "#b68f40")
        i_goodluck_rect = i_goodluck.get_rect(center=(640, 500))
        screen_menu.blit(i_goodluck, i_goodluck_rect)

        return_menu = Button(None, (640, 620), "BACK", game_text(75), "White", "#ccccff")

        return_menu.changeColor(m_instructions)
        return_menu.update(screen_menu)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_menu.checkForInput(m_instructions):
                    game_menu()

        pygame.display.update()

def leaderboards():
    pass      


def gameover_screen(username, score):
    pass

def sound_control(x):
    pygame.mixer.music.set_volume(x)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = user_player_car
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 500
        self.mask = pygame.mask.from_surface(self.image)
        
    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        if self.rect.x < 305:
            self.rect.x = 305
        if self.rect.x > 925:
            self.rect.x = 925
            
            
class Opposition(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = cars_to_avoid
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(305, 980)
        self.rect.y = random.randrange(-100, -50)
        self.mask = pygame.mask.from_surface(self.image)
        self.vel_x = random.randrange(-1, 1)
        self.vel_y = random.randrange(1, 4)
        
    def update(self):
        self.rect.y += self.vel_y
        if self.rect.y > (height+50):
            opposition_instance.kill()
        if self.rect.x <= 305:
            self.rect.x = 305
        if self.rect.x > 925:
            self.rect.x = 925
            
            
class OppositionSpawner:
    def __init__(self):
        self.opposition_group = pygame.sprite.Group()
        self.spawn_timer = random.randrange(30, 120) #1/2 second to 2 seconds
        
    def update(self):
        self.opposition_group.update()
        if self.spawn_timer == 0:
            self.spawn_opposition()
            self.spawn_timer = random.randrange(30, 120)
        else:
            self.spawn_timer -= 1
    
    def spawn_opposition(self):
        new_opposition = Opposition()
        self.opposition_group.add(new_opposition)
        
all_sprites = pygame.sprite.Group()
e = pygame.sprite.Group()

for i in range(6):
    opposition_instance = Opposition()
    e.add(opposition_instance)
    all_sprites.add(opposition_instance)
player_instance = Player()
all_sprites.add(player_instance)

opposition_spawner = OppositionSpawner()

game_menu()
