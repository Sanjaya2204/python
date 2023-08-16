import pygame
import random

pygame.init()
#init()=Initializes all of the imported Pygame modules (returns a tuple indicating success and failure of initializations)
 
white = (255, 255, 255)
seagreen = (180,238,180)
black = (0, 0, 0)
red = (213, 50, 80)
frgreen = (34,139,34)
blue = (50,50,50)
pink=(250,0,200)
coral=(139,62,47)
olive=(188,238,104)
gray=(105,105,105)
#color scheme used in Pygame is RGB i.e “Red Green Blue”.
#In case you set all these to 0’s, the color will be black 
#all 255’s will be white.

dis_width = 1000
dis_height =600
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game ')
"""""
icon=pygame.image.load("snakeimg.png")
pygame.display.set_icon(icon)
"""""
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 15
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
inst_font = pygame.font.SysFont("comicsansms", 30)


def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, gray)
    dis.blit(value, [0, 0])
    #“Your_score”. This function will display the length of the snake subtracted by 1 because that is the initial size of the snake
 
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis,black, [x[0], x[1], snake_block, snake_block])
        #draw.rect() which will help yo draw the rectangle with the desired color and size.
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def instruction():
    a="Game Instructions:\n 1:Use the arrow keys to move the snake around the board.\n2:As the snake eats the food, it grows larger.\n3:The game ends when the snake either moves off the screen or moves into itself.\n4:The goal is to make the snake as large as possible before that happens"
    lines=a.split('\n')
    x=0
    y=0
    for line in lines:
        inst = inst_font.render(line, True,coral)
        dis.blit(inst, [x,y])
        y=y+100
        # updates the frames of the game
        pygame.display.update()
    clock.tick(0.5)


    
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    instruction()
 
    while not game_over:
 
        while game_close == True:
            dis.fill(black)
            message("      You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(olive)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            a = score_font.render("Yummy!!", True, frgreen)
            dis.blit(a, [x1,y1])
            pygame.display.update()
            clock.tick(30)
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()
