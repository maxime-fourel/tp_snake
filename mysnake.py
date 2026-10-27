from random import randint
import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()

def draw_bord(screen):
    x=0
    y=0
    noir=(0,0,0)
    screen.fill(noir)
    width, height = 20,20
    color=(255,255,255)
    i=0
    while i<=30:
        if i%2==0:
            for l in range(30):
                for m in range(30):
                    rect=pg.Rect(40*l,40*m,width,height)
                    pg.draw.rect(screen,color,rect)
            x+=40
        if i%2==1: 
            for l in range(30):
                for m in range(30):
                    rect=pg.Rect(40*l+20,40*m+20,width,height)
                    pg.draw.rect(screen,color,rect)
            x+=40 
        i+=1
    pg.display.update()
    return 

SNAKE = [
   (10, 15),
   (11, 15),
   (12, 15),
]
def draw_snake(snake):
    for segment in snake:
        x, y = segment
        rect = pg.Rect(x * 20, y * 20, 20, 20)
        pg.draw.rect(screen, (255, 0, 0), rect)
        pg.display.update()
    return

def move_snake(snake,direction):
    snake.append((snake[-1][0] + direction[0], snake[-1][1] + direction[1]))
    snake.pop(0)
    return snake

def draw_fruit(FRUIT):
    x,y=FRUIT
    rect = pg.Rect(x * 20, y * 20, 20, 20)
    pg.draw.rect(screen, (0, 255, 0), rect)
    pg.display.update()
    return

def eat_fruit(score, snake, fruit):
    if snake[-1]==fruit:
        score+=1
        snake.insert(0,(snake[0]))
        fruit=(randint(0, 29), randint(0, 29))
        draw_fruit(fruit)
    return (score,snake,fruit)

#initialisation du jeu : direction, score, snake et position d'un premier fruit
direction = (1, 0)
score=0
snake=SNAKE
fruit=(randint(0, 29), randint(0, 29))


while True:
    clock.tick(2)

    for event in pg.event.get():
        if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_q: #pour quitter le jeu en appuyant sur la croix ou sur q
            pg.quit()
    
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_UP and direction!=(0,1):
                direction=(0, -1)
            elif event.key==pg.K_DOWN and direction!=(0,-1):
                direction=(0, 1)
            elif event.key==pg.K_LEFT and direction!=(1,0):
                direction=(-1, 0)
            elif event.key==pg.K_RIGHT and direction!=(-1,0):
                direction=(1, 0)

    # random_color = (0, 0, 0)
    # screen.fill(random_color)
    # x, y = 100, 200            # coin supérieur gauche, en pixels
    # width, height = 20, 20     # largeur et hauteur, en pixels
    # color = (255, 0, 0)        # rouge, en (R, V, B)

    # rect = pg.Rect(x, y, width, height)
    # pg.draw.rect(screen, color, rect)
    

    draw_bord(screen)
    draw_snake(SNAKE)
    move_snake(SNAKE, direction)
    draw_fruit(fruit)
    score, SNAKE, fruit = eat_fruit(score, SNAKE, fruit)




