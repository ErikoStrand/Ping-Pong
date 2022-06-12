from players import player
from ball import ball
from ai import Ai
import pygame, sys
import numpy as np

#values
pygame.init()
CLOCK = pygame.time.Clock()
WIDTH, HEIGHT = 800, 600
RUNNING = True
BACKGROUND = (230, 230, 230)
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
BALLS = []

# start
ANGLE = np.random.randint(0, 360)
balls = ball(WIDTH/2, HEIGHT/2, 25, 25, 50, 180, DISPLAY)
players = player(WIDTH - WIDTH + 50, 250, 25, 100, 1, DISPLAY)
ai = Ai(WIDTH - 75, 250, 25, 100, 1, DISPLAY)

def hit():
    diff = (players.y + players.height/2) - (balls.y)
    return diff
while RUNNING:
    
    dt = CLOCK.tick(60) / 100
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    #update
    players.update(dt)
    balls.update(dt)
    if balls.rect.colliderect(players.rect):
        balls.anglex -= 180
        balls.angley += hit()
        ai.predict = True
    if balls.rect.colliderect(ai.rect):
        print(balls.y, "real")
        balls.anglex += 180
    
        #print(balls.anglex, balls.angley, "x, y")
    ai.update(dt, balls.anglex, balls.angley, balls.x, balls.y)
    DISPLAY.fill(BACKGROUND)
    pygame.draw.line(DISPLAY, (100, 100, 100), (WIDTH/2, 0), (WIDTH/2, HEIGHT), 5)
    players.draw()
    balls.draw()
    ai.draw()
    pygame.display.flip()
    
    