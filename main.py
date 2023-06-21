from Bird import Bird
from Pipe import Pipe
from Score import Score
from Game import *

pygame.font.init()
pygame.init()

if __name__ == '__main__':

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Flappy Bird")

    bird = Bird(WIDTH - 80 - 40, HEIGHT / 4 + 40, screen)
    pipe = Pipe(screen, bird, pipe_image)
    score = Score(screen)

    game = Game(screen, bird, pipe, score)
    game.run() # Run the game