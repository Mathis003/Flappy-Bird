from Assets import *

class Score:

    def __init__(self):
        self.score = 0

    def readBestScore(self):
        try:
            with open("BestScore.txt", "r") as file:
                best_score = file.read()
                return best_score
        except:
            return "0"
    
    def writeBestScore(self, best_score):
        with open("BestScore.txt", "w") as file:
            file.write(str(best_score))
    
    def addBestScore(self):
        bestScore = self.readBestScore()
        if int(bestScore) < self.score:
           self.writeBestScore(self.score)
    
    def display_score(self):
        font = pygame.font.SysFont("comicsans", 50)
        text_score = font.render("Score : {}".format(self.score), 1, WHITE)
        best_score_str = self.readBestScore()
        text_best_score = font.render("Best Score : {}".format(best_score_str), 1, WHITE)
        screen.blit(text_score, (79/80 * WIDTH - text_score.get_width(), WIDTH/80))
        screen.blit(text_best_score, (WIDTH/80, WIDTH/80))