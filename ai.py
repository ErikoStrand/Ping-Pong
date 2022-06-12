import pygame
import math
class Ai:
    def __init__(self, x, y, width, height, speed, display):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.direction = 0
        self.display = display
        self.predict = False
        self.ballcenter = 0
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    def update(self, dt, anglex, angley, ballx, bally):
        self.anglex = anglex
        self.angley = angley
        self.ballx = ballx
        self.bally = bally
            
        while self.predict:
            self.ballx = self.ballx + (dt*self.speed*math.cos(math.radians(self.anglex)))
            self.bally = self.bally + (dt*self.speed*math.sin(math.radians(self.angley)))
            if self.bally < 0 + 25/2:
                self.angley -= 180
            if self.bally > 600 - 25/2:
                self.angley += 180
            if self.ballx >= 800 - 75:
                self.ballcenter = self.bally
                print(self.ballcenter + self.height/2, "preditct")
                self.predict = False
                
        #print(self.ballcenter, "ball", self.y + self.height/2, "player")
        if self.ballcenter - 10 <= self.y + self.height/2 <= self.ballcenter + 10:
            self.direction = 0
        else:
            if self.ballcenter < self.y + self.height/2:
                self.direction = -1
                    #up
            if self.ballcenter > self.y + self.height/2:
                self.direction = 1 
                    #down
            
        if self.direction == -1 and not self.y < 0:
            self.y -= 60*dt*self.speed
        elif self.direction == 1 and not self.y > 600 - self.height:
            self.y += 60*dt*self.speed
            
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    def draw(self):
        pygame.draw.rect(self.display, (160, 160, 160), self.rect)
        #print(self.rect)