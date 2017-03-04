import pygame

class Paddle:

    def __init__(self, width, height, x):
        self.screen_width = width
        self.screen_height = height
        self.x = x
        self.y = 20
        self.dy = 10
        self.height = 100
        self.width = 10
        self.color = (100,100,100)

    def paint(self, surface):
        pygame.draw.rect(surface, self.color, (self.x,self.y, self.width, self.height))

    def move_logic(self, keys):
        if pygame.K_w in keys and self.y >= 0:
            self.y -= self.dy
            if self.y < 0:
                self.y = 0

        if pygame.K_s in keys and self.y +self.height <= self.screen_height:
            self.y += self.dy
            if self.y + self.height > self.screen_height:
                self.y = self.screen_height - self.height

    def move_logic2(self, keys):
        if pygame.K_UP in keys and self.y >= 0:
            self.y -= self.dy
            if self.y < 0:
                self.y = 0

        if pygame.K_DOWN in keys and self.y +self.height <= self.screen_height:
            self.y += self.dy
            if self.y + self.height > self.screen_height:
                self.y = self.screen_height - self.height
