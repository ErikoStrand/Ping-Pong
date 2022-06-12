import pygame
import math
import numpy as np
class ball:
    def __init__(self, x, y, width, height, speed, starting_angle, display):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.anglex = starting_angle
        self.angley = starting_angle
        self.display = display
        self.direction = 0
        
    def update(self, dt):
        #print(self.anglex, self.angley, "angles x, y")
        if self.y < 0 + self.width/2:
            self.angley -= 180
        if self.y > 600 - self.width/2:
            self.angley += 180    
        self.x = self.x + (dt*self.speed*math.cos(math.radians(self.anglex)))
        self.y = self.y + (dt*self.speed*math.sin(math.radians(self.angley)))
        self.rect = pygame.Rect(self.x, self.y - self.width/2, self.width, self.height)
        #print(self.x, self.y)
    def draw(self):
        pygame.draw.rect(self.display, (170, 170, 170), self.rect)
    def reset(self):
        angle = np.random.randint(0, 360)
        self.anglex = angle
        self.angley = angle
        self.x = 400
        self.y = 300
        