from Bird import Bird
from Pipe import Pipe
from Score import Score
from Game import *

pygame.font.init()
pygame.init()

if __name__ == '__main__':

    pygame.display.set_caption("Flappy Bird")

    bird = Bird(INIT_POS_BIRD_X, INIT_POS_BIRD_Y)
    pipe = Pipe(bird)
    score = Score()

    game = Game(bird, pipe, score)
    game.run() # Run the game