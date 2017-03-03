import pygame
import game_mouse
import ball
import paddle
import score

# Starter code for PyGame applications

class PygameStarter(game_mouse.Game):

    def __init__(self, width, height, fps):
        game_mouse.Game.__init__(self, "Pygame Starter",
                                 width,
                                 height,
                                 fps)
        self.ball = ball.Ball(width, height)
        self.paddle = paddle.Paddle(width, height)
        self.score = score.Score()
        return
    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position):
        x = mouse_position[0]
        y = mouse_position[1]

        if pygame.K_a in newkeys:
            print("a key pressed")

        if 1 in newbuttons:
            print("button clicked")


        self.paddle.move_logic(keys)
        point = self.ball.collision_logic(self.paddle.x, self.paddle.y, self.paddle.height, self.paddle.width)
        self.score.update(point)
        self.ball.move()

        #self.ball.x = x
        #self.ball.y = y
        return

    def paint(self, surface):
        surface.fill((255,255,255))
        self.score.paint(surface, self.width)
        self.ball.paint(surface)
        self.paddle.paint(surface)
        return

def main():
    screen_width = 500
    screen_height = 500
    frames_per_second = 20
    game = PygameStarter(screen_width, screen_height, frames_per_second)
    game.main_loop()
    return

if __name__ == "__main__":
    main()
