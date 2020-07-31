#    ------------------------------------------------------------------------------------------
#    Author         : Mohammad Montasim -Al- Mamun Shuvo
#    Copyright      : Copyright 2020, Mohammad Montasim -Al- Mamun Shuvo
#    Email          : montasimmamun@gmail.com
#    Github         : https://github.com/montasimmamun/
#    Date           : Created on 27/07/2020
#    Version        : 1.0.1
#    Template Name  : Welcome Template Advance
#    ------------------------------------------------------------------------------------------

#    for game
import pygame
#   for random functionality
import random
#   for file operation
import os
# for sleep
import time

#   initialize sound
pygame.mixer.init()

#   initialize pygame
pygame.init()

#   set game window size
screen_width = 800
screen_height = 600

# Colors
grey = (119, 118, 110)
black = (0, 0, 0)
red = (255, 0, 0)

gameName = (255, 0, 77)
enterToPlay = (0, 181, 184)
quitGame = (254, 225, 26)
scoreHighScore = (254, 225, 26)
gameOver = (255, 0, 77)
enterToContinue = (90, 39, 193)
qToQuit = (39, 159, 0)
food = (255, 0, 77)

# Game control variables
exit_game = False
game_over = False

#   set game window size to 600 x 400
game_display = pygame.display.set_mode((screen_width, screen_height))

#   set game background image
backgroundImage = pygame.image.load("images/gameImage.png")
#   display game background image
backgroundImage = pygame.transform.scale(backgroundImage, (screen_width, screen_height)).convert_alpha()

#   set game name
pygame.display.set_caption("Car Racing Game")
#   display game name
pygame.display.update()

#   set game icon
icon = pygame.image.load("images/icon.png")
#   display game icon
pygame.display.set_icon(icon)

#   set game font
font = pygame.font.SysFont(None, 30)

#   set game fps
fps = 60
#   set clock for fps
clock = pygame.time.Clock()


#   display score to screen
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    game_display.blit(screen_text, [x, y])


#   event handling
def Event():
    for event in pygame.event.get():
        #   if cross is pressed exit game window
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        #   if any key from keyboard is pressed set action
        if event.type == pygame.KEYDOWN:
            #   if enter key is pressed start game
            if event.key == pygame.K_RETURN:
                Game_Loop()

            #   if q/Q key is pressed exit game window
            if event.key == pygame.K_q:
                #   game quit function
                quit()


#   welcome screen
def Welcome():
    #   set welcome screen sound
    pygame.mixer.music.load('sounds/game.mp3')
    #   play welcome sound
    pygame.mixer.music.play()

    global exit_game
    while not exit_game:
        #   set welcome image
        welcome_image = pygame.image.load("images/welcome_image.png")
        #   convert welcome image for display
        welcome_image = pygame.transform.scale(welcome_image, (screen_width, screen_height)).convert_alpha()
        #   display welcome image
        game_display.blit(welcome_image, (0, 0))

        #   display game option
        text_screen("Welcome Template By Montasim", gameName, 250, 50)
        text_screen("Press Enter To Play", enterToPlay, 315, 545)
        text_screen("Press Q to Quit", quitGame, 333, 575)

        #   call event function
        Event()

        #   display above changes
        pygame.display.update()
        #   set fps to game
        clock.tick(fps)


#   game control variable
bumped = False

#   scores
hi_score = 0
score = 0
passed = 0
level = 0

#   initial car position
x = int(screen_width * 0.45)
y = int(screen_height * 0.8)

#   change position of car
x_change = 0


# Game Loop
def Game_Loop():
    car_image = pygame.image.load("images/car.jpg")
    background_image = pygame.image.load("images/grass.jpg")
    road_strip_image = pygame.image.load("images/yellow_strip.jpg")
    strip_image = pygame.image.load("images/strip.jpg")
    car_width = 56

    obstacle_speed = 9
    obstacle = 0
    y_change = 0
    obstacle_startx = random.randrange(200, (screen_width - 200))
    obstacle_starty = 750
    obstacle_width = 56
    obstacle_height = 125

    def Text_Objects(text, font):
        text_surface = font.render(text, True, black)
        return text_surface, text_surface.get_rect()

    def Message_Display(text):
        large_text = pygame.font.Font("freesansbold.ttf", 80)
        text_surf, text_rect = Text_Objects(text, large_text)
        text_rect.center = (int(screen_width / 2), int(screen_height / 2))
        game_display.blit(text_surf, text_rect)
        pygame.display.update()
        time.sleep(3)

    #   road
    def Background():
        game_display.blit(background_image, (0, 0))
        game_display.blit(background_image, (0, 200))
        game_display.blit(background_image, (0, 400))

        game_display.blit(background_image, (700, 0))
        game_display.blit(background_image, (700, 200))
        game_display.blit(background_image, (700, 400))

        game_display.blit(road_strip_image, (400, 0))
        game_display.blit(road_strip_image, (400, 100))
        game_display.blit(road_strip_image, (400, 200))

        game_display.blit(road_strip_image, (400, 300))
        game_display.blit(road_strip_image, (400, 400))
        game_display.blit(road_strip_image, (400, 500))

        game_display.blit(strip_image, (120, 0))
        game_display.blit(strip_image, (120, 100))
        game_display.blit(strip_image, (120, 200))

        game_display.blit(strip_image, (680, 0))
        game_display.blit(strip_image, (680, 100))
        game_display.blit(strip_image, (680, 200))

    #   car
    def Car(x, y):
        game_display.blit(car_image, (x, y))

    def Obstacle(obstacle_startx, obstacle_starty, obstacle):
        if obstacle == 0:
            obstacle_car_pick = pygame.image.load("images/car1.jpg")

        if obstacle == 1:
            obstacle_car_pick = pygame.image.load("images/car2.jpg")

        if obstacle == 2:
            obstacle_car_pick = pygame.image.load("images/car3.jpg")

        if obstacle == 3:
            obstacle_car_pick = pygame.image.load("images/car4.jpg")

        if obstacle == 4:
            obstacle_car_pick = pygame.image.load("images/car5.jpg")

        if obstacle == 5:
            obstacle_car_pick = pygame.image.load("images/car6.jpg")

        if obstacle == 6:
            obstacle_car_pick = pygame.image.load("images/car7.jpg")
            
        game_display.blit(obstacle_car_pick, (int(obstacle_startx), int(obstacle_starty)))

    #   check if Hi Score.txt exists
    if (not os.path.exists("Hi Score.txt")):
        with open("Hi Score.txt", "w") as f:
            f.write("0")

    def Score(passed, score):
        font = pygame.font.SysFont(None, 30)
        text = font.render("Passed: " + str(passed), True, black)
        score = font.render("Score: " + str(score), True, red)

        game_display.blit(score, (0, 30))
        game_display.blit(text, (0, 60))



    global bumped
    while not bumped:
        #   get every event inside car game
        for event in pygame.event.get():
            global x_change
            global x
            #   if cross is pressed exit game
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            #   if left arrow key is pressed move car position to left
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -15

                if event.key == pygame.K_RIGHT:
                    x_change = 15

                if event.key == pygame.K_a:
                    obstacle_speed += 2

                if event.key == pygame.K_b:
                    obstacle_speed -= 2

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

            x += x_change

        game_display.fill(grey)
        Background()
        obstacle_starty -= (obstacle_speed / 4)
        Obstacle(obstacle_startx, obstacle_starty, obstacle)
        obstacle_starty += obstacle_speed
        Car(x, y)

        global passed
        global score
        global level
        global hi_score

        Score(passed, score)

        if x > 690 - car_width or x < 110:
            Game_Over()

        if x > screen_width - (car_width + 110) or x < 110:
            Game_Over()

        if obstacle_starty > screen_height:
            obstacle_starty = 0 - obstacle_height
            obstacle_startx = random.randrange(170, (screen_width - 170))
            obstacle = random.randrange(0, 7)

            passed += 1
            score = passed * 10

            #   change hiScore
            if score > int(hi_score):
                hi_score = score

            if int(passed) % 10 == 0:
                level += 1
                obstacle_speed += 2

                large_text = pygame.font.Font("freesansbold.ttf", 80)
                text_surf, text_rect = Text_Objects("LEVEL: " + str(level), large_text)
                text_rect.center = (int(screen_width / 2), int(screen_height / 2))
                game_display.blit(text_surf, text_rect)
                pygame.display.update()
                time.sleep(3)

        if y < obstacle_starty + obstacle_height:
            if obstacle_startx < x < obstacle_startx + obstacle_width or obstacle_startx < x + car_width < obstacle_startx + obstacle_width:
                Game_Over()

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

#   game over screen
def Game_Over():
    #   set game over screen sound
    pygame.mixer.music.load('sounds/gameover.mp3')
    #   play game over screen sound
    pygame.mixer.music.play()

    global exit_game
    global hi_score
    while not exit_game:
        #   set welcome image
        welcome_image = pygame.image.load("images/game_over_image.png")
        #   convert welcome image for display
        welcome_image = pygame.transform.scale(welcome_image, (screen_width, screen_height)).convert_alpha()
        #   display welcome image
        game_display.blit(welcome_image, (0, 0))

        #   write high score
        with open("Hi Score.txt", "w", encoding='utf-8') as f:
            f.write(str(hi_score))
            f.close()

        #   show high score
        with open("Hi Score.txt", "r", encoding='utf-8') as f:
            hi_score = f.read()
            f.close()

        #   display game option
        text_screen("Game Over", gameName, 360, 50)
        text_screen("Score: " + str(score) + ", High Score: " + str(hi_score), scoreHighScore, 300, 80)
        text_screen("Enter To Play Again", enterToPlay, 315, 525)
        text_screen("Press Q to Quit", quitGame, 333, 555)

        #   call event function
        Event()

        #   display above changes
        pygame.display.update()
        #   set fps to game
        clock.tick(fps)

Welcome()
