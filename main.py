from src.Bird import Bird
from src.Pipe import Pipe
from src.Score import Score
from src.Game import *

pygame.font.init()
pygame.init()

if __name__ == '__main__':

    pygame.display.set_caption("Flappy Bird")

    bird = Bird(INIT_POS_BIRD_X, INIT_POS_BIRD_Y)
    pipe = Pipe(bird)
    score = Score()

    game = Game(bird, pipe, score)
    game.run() # Run the game