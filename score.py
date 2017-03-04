import pygame

class Score:

    def __init__(self):
        self.player1 = 0
        self.player2 = 0
        self.font_size = 20
        pygame.font.init()
        self.myfont = pygame.font.SysFont('Comic Sans MS', self.font_size)
        self.text = 'Player 1: %i Player 2: %i' % (self.player1, self.player2)
        self.textsurface = self.myfont.render(self.text, False, (0, 0, 0))

    def paint(self, surface, screen_width):
        length, height = self.myfont.size(self.text)
        surface.blit( self.textsurface, ( screen_width // 2 - length // 2,0 ) )

    def update(self, point):
        if point == "left wall":
            self.player2 += 1
            self.textsurface = self.myfont.render('Player 1: %i Player 2: %i' % (self.player1, self.player2), False, (0, 0, 0))
        elif point == "right wall":
            self.player1 += 1
            self.textsurface = self.myfont.render('Player 1: %i Player 2: %i' % (self.player1, self.player2), False, (0, 0, 0))
        return
