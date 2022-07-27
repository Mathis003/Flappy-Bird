from Assets import *
# A REFAIRE OUBLIER D ENREGISTRER L'ECRAN
# => COLISION, RESET_GAME


class Game:

    def __init__(self, screen, bird, pipe):
        self.screen = screen
        self.bird = bird
        self.pipe = pipe

        self.running = True

    def moove_ground(self):
        speed_ground = 8
        #Moove ground
        ground1_rect.x -= speed_ground
        ground2_rect.x -= speed_ground
        #Respawn picture if out of screen
        if ground1_rect.x <= - width:
            ground1_rect.x = 0
        if ground2_rect.x <= 0:
            ground2_rect.x = width

    def reset_game(self):
        self.bird.x = width / 2 - 80 / 2
        self.bird.y = height / 2 - 60 / 2
        self.pipe.initial_position()

    def draw_screen(self):
        self.screen.blit(background_image, background_rect)
        self.pipe.moove_alone()
        self.screen.blit(ground1_image, ground1_rect)
        self.screen.blit(ground2_image, ground2_rect)
        self.moove_ground()
        rotated_image, new_rect = self.bird.new_image_and_rect()[0], self.bird.new_image_and_rect()[1]
        self.bird.draw(rotated_image, new_rect)
        if self.collision_bird_ground(new_rect):
            self.reset_game()

    def collision_bird_ground(self, new_rect):
        rect_ground = pygame.Rect(0, 5.7 * (height / 7), width, (height / 5))
        print(new_rect)
        if new_rect.colliderect(rect_ground):
            return True
        return False

    def run(self):
        clock = pygame.time.Clock()
        while self.running:

            clock.tick(30)
            #Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if not event.key == pygame.K_ESCAPE: # Idk why 'not'...
                        self.bird.jump()

            #Displays Game
            self.bird.moove()
            self.draw_screen()
            pygame.display.update()