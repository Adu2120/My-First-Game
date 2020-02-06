import pygame
import time

pygame.init()

screen = pygame.display.set_mode((500, 800))

# icon and title
Running = True
game_over = False
pygame.display.set_caption("FootBall")
icon = pygame.image.load('ball.png')
# Back = pygame.image.load('bachground.jpg')
pygame.display.set_icon(icon)

# Create A Player image
Playerimg = pygame.image.load('Player.png')
Player_x = 237           #237-266
Player_y = 651
size = 30
Ball_size = 20
Change_x = 0
Change_y = 0
ball = pygame.image.load('ball.png')
# Create A Obstacle image
Obstacalimg = pygame.image.load('obstacal.png')
# obstacalx = 168
# obstracaly = 158
ChangeUx = [0.3,0.5,0.7,0.9,1.1,1.2,1.3,1.4]
ChangeUy = [0.3,0.5,0.7,0.9,1.1,1.2,1.3,1.4]
#Bondries of obstacal
obstacal_x_start = [190,115,24,237,115,24,237,115]
obstacal_x_end = [284,357,237,450,357,237,450,357]

obstacalx = [284,115,24,237,116,24,237,115]
obstacaly = [52,93,193,193,293,393,393,493]

Ball_speed = 0
# create background image
ground = pygame.image.load('Football_Ground.jpg')

font=pygame.font.SysFont(None,55)

def player(x, y):
    screen.blit(Playerimg, (x, y))

def Football(x, y):
    screen.blit(ball, (x, y))

def obstacal(x, y):
    screen.blit(Obstacalimg, (x, y))

def text_screen(text,x,y):
    screen_text=font.render(text,True,(255,0,0))
    screen.blit(screen_text,[x,y])
ball_y = Player_y - 20

while Running:
    ball_x = Player_x + 3
    if Ball_speed == 0:
        ball_y = Player_y - 20


    if game_over:
        screen.fill((0,0,0))

        text_screen("Game Over!", 150, 400)
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                Running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_over = False

    elif ball_y!=40:
        screen.fill((255, 255, 255))
        screen.blit(ground, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False
            if event.type == pygame.KEYDOWN:  # KEYDOWN = key is pressed
                if event.key == pygame.K_LEFT:
                    Change_x = -0.5
                elif event.key == pygame.K_RIGHT:
                    Change_x = 0.5
                elif event.key == pygame.K_DOWN:
                    Change_y = 0.5
                elif event.key == pygame.K_UP:
                    Change_y = -0.5
                elif event.key == pygame.K_LEFT and event.key == pygame.K_UP:
                    Change_x = -0.5
                    Change_y = -0.5
                elif event.key == pygame.K_LEFT and event.key == pygame.K_DOWN:
                    Change_x = -0.5
                    Change_y = 0.5
                elif event.key == pygame.K_RIGHT and event.key == pygame.K_UP:
                    Change_x = 0.5
                    Change_y = -0.5
                elif event.key == pygame.K_RIGHT and event.key == pygame.K_DOWN:
                    Change_x = 0.5
                    Change_y = 0.5
                elif event.key == pygame.K_SPACE:
                    Ball_speed = 1
                    #if event.key == pygame.K_SPACE:


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    Change_x = 0
                    Change_y = 0

        Player_x += Change_x
        Player_y += Change_y
        ball_y -= Ball_speed
        if Player_x <= 24:
            Player_x = 24
        if Player_x >= 450:
            Player_x = 450
        if Player_y <= 147:
            Player_y = 147
            """for event in pygame.event.get():
                if event.key == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        while ball_y != 40:
                            ball_y += Ball_speed
                            Football(ball_x, ball_y)
                            pygame.display.update()"""
        if Player_y >= 780:
            Player_y = 780
        # 1
        for i in range(0,8):
            obstacal(obstacalx[i],obstacaly[i])
        for i in range(0,8):
            obstacalx[i] += ChangeUx[i]
            if obstacalx[i] <= obstacal_x_start[i]:
                ChangeUx[i] = ChangeUy[i]
            elif obstacalx[i] >= obstacal_x_end[i]:
                ChangeUx[i] = -ChangeUy[i]

        #Check Collision of:
        #1. Player + Ball
        for i in range(0,8):
            if abs(obstacaly[i] + size - Player_y - size + 30) < 30 and abs( obstacaly[i] + size - Player_y - size + 20) >= -30:
                if abs(obstacalx[i] + size - Player_x - size) < 30 and abs( obstacalx[i] + size - Player_x - size) >= -30:
                    game_over = True
        #2. Only Ball
        for i in range(0,8):
            if abs(obstacaly[i] + size - ball_y - Ball_size) < 20 and abs( obstacaly[i] + size - ball_y - Ball_size) >= -20:
                if abs(obstacalx[i] + size - ball_x - Ball_size) < 20 and abs( obstacalx[i] + size - ball_x - Ball_size) >= -20:
                    game_over = True
        player(Player_x, Player_y)
        Football(ball_x, ball_y)
        #print(Player_x, Player_y)
    #print(event)
    elif ball_x > 190 and ball_x < 284:
        screen.fill((0,0,0))
        text_screen("You Won!", 150, 400)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False
    else:
        game_over = True
    #print(event)
    pygame.display.update()