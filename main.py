from players import player
from ball import ball
from ai import Ai
import pygame, sys
import numpy as np

#values
pygame.init()
pygame.font.init()
CLOCK = pygame.time.Clock()
WIDTH, HEIGHT = 800, 600
RUNNING = True
BACKGROUND = (230, 230, 230)
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
BLOCK_SPEED = 0.60
BALL_SPEED = 50
# start
ANGLE = np.random.randint(140, 220)
balls = ball(WIDTH/2, HEIGHT/2, 25, 25, BALL_SPEED, ANGLE, DISPLAY)
players = player(WIDTH - WIDTH + 50, 250, 25, 100, BLOCK_SPEED, DISPLAY)
ai = Ai(WIDTH - 75, 250, 25, 100, BLOCK_SPEED, DISPLAY)

def draw_text(text, font_size, color, x, y):
    font = pygame.font.Font("PokemonGB.ttf", font_size)
    a, b = pygame.font.Font.size(font, str(text))
    draw = font.render(str(text), False, color)
    DISPLAY.blit(draw, (x - a/2, y))
    
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
    if balls.x < 0 - balls.width:
        balls.reset()
        players.score += 1
    if balls.x > 800:
        balls.reset()
        ai.score += 1
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
    draw_text(players.score, 40, (90, 90, 90), WIDTH - WIDTH/4, HEIGHT/2)
    draw_text(ai.score, 40, (90, 90, 90), WIDTH/4, HEIGHT/2)
    pygame.draw.line(DISPLAY, (100, 100, 100), (WIDTH/2, 0), (WIDTH/2, HEIGHT), 5)
    players.draw()
    balls.draw()
    ai.draw()
    pygame.display.flip()
    
    