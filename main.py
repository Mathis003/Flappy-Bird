"""Create Flappy Bird's Game with IA :)"""
from Assets import *
from Bird import Bird
from Game import Game
from Pipe import Pipe

pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flappy Bird IA")
bird = Bird(width / 2 - 80 / 2, height / 2 - 60 / 2, screen) # 80, 60 = dimension_rect_x, dimension_rect_y
pipe_image = pygame.image.load("../../Flappy Bird - Latest_version/Flappy-Bird/assets/pipe.png")
pipe_image = pygame.transform.scale(pipe_image, (140, 1000))
pipe = Pipe(screen, pipe_image)

game = Game(screen, bird, pipe)
if __name__ == '__main__':
    game.run()