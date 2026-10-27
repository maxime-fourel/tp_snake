from random import randint
import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()

while True:
    clock.tick(1)

    for event in pg.event.get():
        if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_q: #pour quitter le jeu en appuyant sur la croix ou sur q
            pg.quit()

    random_color = (0, 0, 0)
    screen.fill(random_color)
    x, y = 100, 200            # coin supérieur gauche, en pixels
    width, height = 20, 20     # largeur et hauteur, en pixels
    color = (255, 0, 0)        # rouge, en (R, V, B)

    rect = pg.Rect(x, y, width, height)
    pg.draw.rect(screen, color, rect)
    
    pg.display.update()

def draw_bord():
    

