import pygame

class Ball:

    def __init__(self, width, height):
        self.screen_width = width
        self.screen_height = height
        self.radius = 10
        self.x = 50
        self.y = 50
        self.dx = 10
        self.dy = 2
        self.color = (100,100,100)

    def paint(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def move_logic(self, paddle_x, paddle_y, paddle_height, paddle_width):

        if self.x + self.radius >= self.screen_width or self.x - self.radius <= 0:
            self.dx *= -1
        if self.y + self.radius >= self.screen_height or self.y - self.radius <= 0:
            self.dy *= -1
        if self.x - self.radius <= paddle_x + paddle_width and self.y <= paddle_y + paddle_height and self.y >= paddle_y:
            self.dx *= -1
        self.y += self.dy
        self.x += self.dx
