import pygame

class player:
    def __init__(self, x, y, width, height, speed, display):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.direction = 0
        self.display = display
        #self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    def update(self, dt):
        self.direction = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            #print("down")
            self.direction = 1
        if keys[pygame.K_UP]:
            #print("up")
            self.direction = -1
        if self.direction == -1 and not self.y < 0:
            self.y -= 60*dt*self.speed
        elif self.direction == 1 and not self.y > 600 - self.height:
            self.y += 60*dt*self.speed
            
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    def draw(self):
        pygame.draw.rect(self.display, (160, 160, 160), self.rect)
        #print(self.rect)