import pygame
from math import sqrt
from random import randint

class Ball:

    def __init__(self, width, height):
        pygame.mixer.pre_init(44100, -16, 2, 4096) #frequency, size, channels, buffersize
        pygame.init() #turn all of pygame on.
        self.wall_hit = pygame.mixer.Sound("sounds/ping_pong_8bit_plop.wav")
        self.paddle_hit = pygame.mixer.Sound("sounds/ping_pong_8bit_beeep.wav")
        self.paddle_hit.set_volume(.4)
        self.back_wall_hit = pygame.mixer.Sound("sounds/ping_pong_8bit_peeeeeep.wav")
        self.back_wall_hit.set_volume(.3)
        self.screen_width = width
        self.screen_height = height
        self.radius = 10
        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = 0
        self.set_speed_and_position()
        self.color = (100,100,100)

    def set_speed_and_position(self, side = 1):
        if side == 1:
            self.dx = randint(10,20)
            self.x = self.screen_width // 3
        else:
            self.dx = randint(-20,-10)
            self.x = (self.screen_width // 3) * 2
        self.dy = randint(-20,20)
        if self.dy == 0:
            self.dy = -1
        self.y = randint(0,self.screen_height)

    def paint(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.y += self.dy
        self.x += self.dx
        return

    def collision_wall(self):
        if self.x + self.radius >= self.screen_width:
            self.dx *= -1
            self.x = self.screen_width - self.radius
            self.set_speed_and_position(2)
            self.back_wall_hit.play()
            return "right wall"
        elif self.x - self.radius <= 0:
            self.set_speed_and_position()
            self.back_wall_hit.play()
            return "left wall"
        elif self.y + self.radius >= self.screen_height:
            self.dy *= -1
            self.y = self.screen_height - self.radius
            self.wall_hit.play()
            return "bottom wall"
        elif self.y - self.radius <= 0:
            self.dy *= -1
            self.y = self.radius
            self.wall_hit.play()
            return "top wall"

    def collision_paddle1(self, paddle_x, paddle_y, paddle_height, paddle_width, surface = None):
        if sqrt(abs(self.radius**2 - (self.x-self.radius)**2)) <= paddle_x + paddle_width and self.x > paddle_x + paddle_width // 2:
            if sqrt(abs(self.radius**2 - (self.y + self.radius)**2)) >= paddle_y:
                if sqrt(abs(self.radius**2 - (self.y - self.radius)**2)) <= paddle_y + paddle_height:
                    myfont = pygame.font.SysFont('Comic Sans MS', 30)
                    text = 'Bounce'
                    textsurface = myfont.render(text, False, (0, 0, 0))
                    surface.blit( textsurface, (0,0) )
                    if self.y - paddle_y < 0: # UP
                        if self.dy > 0:
                            self.dy *= -1
                    elif self.y - paddle_y > paddle_height: # DOWN
                        if self.dy < 0:
                            self.dy *= -1
                    self.dx *= -1
                    self.x = paddle_x + paddle_width + self.radius
                    self.paddle_hit.play()
                    return "paddle"
        return "none"

    def collision_paddle2(self, paddle_x, paddle_y, paddle_height, paddle_width, surface = None):
        if sqrt(abs(self.radius**2 - (self.x + self.radius)**2)) >= paddle_x and self.x < paddle_x + paddle_width // 2:
            if sqrt(abs(self.radius**2 - (self.y + self.radius)**2)) >= paddle_y:
                if sqrt(abs(self.radius**2 - (self.y - self.radius)**2)) <= paddle_y + paddle_height:
                    myfont = pygame.font.SysFont('Comic Sans MS', 30)
                    text = 'Bounce'
                    textsurface = myfont.render(text, False, (0, 0, 0))
                    surface.blit( textsurface, (0,0) )
                    if self.y - paddle_y < 0: # UP
                        if self.dy > 0:
                            self.dy *= -1
                    elif self.y - paddle_y > paddle_height: # DOWN
                        if self.dy < 0:
                            self.dy *= -1
                    self.dx *= -1
                    self.x = paddle_x - self.radius
                    self.paddle_hit.play()
                    return "paddle"
        return "none"
