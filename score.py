import pygame

class Score:

    def __init__(self):
        self.computer = 0
        self.player = 0
        self.font_size = 20
        pygame.font.init()
        self.myfont = pygame.font.SysFont('Comic Sans MS', self.font_size)
        self.text = 'Player: %i Computer: %i' % (self.player, self.computer)
        self.textsurface = self.myfont.render(self.text, False, (0, 0, 0))

    def paint(self, surface, screen_width):
        length, height = self.myfont.size(self.text)
        surface.blit( self.textsurface, ( screen_width // 2 - length // 2,0 ) )

    def update(self, point):
        if point == "back wall":
            self.computer += 1
            self.textsurface = self.myfont.render('Player: %i Computer: %i' % (self.player, self.computer), False, (0, 0, 0))
        elif point == "paddle":
            self.player += 1
            self.textsurface = self.myfont.render('Player: %i Computer: %i' % (self.player, self.computer), False, (0, 0, 0))
        return
