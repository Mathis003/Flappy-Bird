from Assets import *
from Pipe import Pipe

class Game:

    def __init__(self, bird, pipe, score):
        
        self.bird = bird
        self.score = score
        self.list_pipe = [pipe]

        self.begin_menu = True
        self.transition_end_menu = False
        self.end_menu = False
        self.game = False
        self.running = True
        self.FPS = 30

        self.clock = pygame.time.Clock()
        self.click_count = 0
        self.first_iteration_in_begin_menu = True
        self.speed_anim_title = 4
        self.title_pos_y = HEIGHT / 4

    def move_ground(self):
        ground1_rect.x -= SPEED_GROUND
        ground2_rect.x -= SPEED_GROUND
        
        if ground1_rect.x <= - WIDTH:
            ground1_rect.x = 0
        if ground2_rect.x <= 0:
            ground2_rect.x = WIDTH

    def reset_game(self):
        self.bird.reset_pos()
        self.score.score = 0
        self.list_pipe = [Pipe(self.bird)]
        self.bird.first_move = False

    def update_list_pipe(self):
        remove_list = []
        add_list = []
        for pipe in self.list_pipe:
            if pipe.need_new_pipe():
                add_list.append(Pipe(self.bird))
            if pipe.need_destroy_pipe():
                remove_list.append(pipe)

        for pipe in remove_list:
            self.list_pipe.remove(pipe)
        for pipe in add_list:
            self.list_pipe.append(pipe)
    

    def display_begin_menu(self):
        screen.blit(background_image, background_rect)
        screen.blit(ground1_image, ground1_rect)
        screen.blit(ground2_image, ground2_rect)
        self.move_ground()
        screen.blit(flappy_bird_image, flappy_bird_rect)
        screen.blit(start_button_image, start_button_rect)
        screen.blit(score_button_image, score_button_rect)
        self.bird.update_animation()
        self.click_count += 1
    
    def title_animation(self):
        if self.first_iteration_in_begin_menu:
            if self.click_count % 10 == 0:  # after 0.33 second
                self.speed_anim_title *= -1
                self.first_iteration_in_begin_menu = False
                self.click_count = 0
        else:
            if self.click_count % 20 == 0:  # after 0.66 second
                self.speed_anim_title *= -1

        self.bird.y += self.speed_anim_title
        self.title_pos_y += self.speed_anim_title
        flappy_bird_rect.topleft = (WIDTH / 12, self.title_pos_y)


    def run(self):

        while self.running:

            self.clock.tick(self.FPS)

            ### Events

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False
                    self.score.addBestScore()
                    pygame.quit()

                if event.type == pygame.KEYDOWN and self.game:
                    if not event.key == pygame.K_ESCAPE:
                        self.bird.first_move = True
                        if not self.transition_end_menu:
                            self.bird.jump()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos_mouse = pygame.mouse.get_pos()
                    if self.begin_menu:
                        if start_button_rect.collidepoint(pos_mouse[0], pos_mouse[1]):
                            # Initialisation for closing the begin_menu and open the game
                            self.begin_menu = False
                            self.game = True
                            self.bird.x -= WIDTH / 8
                    if self.end_menu:
                        if ok_button_rect.collidepoint(pos_mouse[0], pos_mouse[1]):
                            self.end_menu = False
                            self.begin_menu = True
                            self.reset_game()


            ### Displays Game

            # If the player is in the begin menu
            if self.begin_menu:
                self.display_begin_menu()
                self.title_animation()

            # If the player is in the game
            elif self.game:

                screen.blit(background_image, background_rect)

                # If the game is running and the player is not dead
                if not self.transition_end_menu:

                    self.move_ground()

                    # If the player hasn't moved yet
                    if not self.bird.first_move:
                        screen.blit(tap_bird_image, tap_bird_rect)
                        screen.blit(get_ready_image, get_ready_rect)

                    # If the player has already moved once
                    else:
                        self.bird.move()

                        self.update_list_pipe()
                        for pipe in self.list_pipe:

                            if pipe.bird_passed():
                                self.score.score += 1

                            pipe.move_alone()
                            if pipe.collide_bird():
                                self.score.addBestScore()
                                self.score.score = 0
                                self.transition_end_menu = True

                        if self.bird.collide_ground():
                            self.score.addBestScore()
                            self.score.score = 0
                            self.game = False
                            self.end_menu = True

                    self.bird.update_animation()
                    self.score.display_score()

                    screen.blit(ground1_image, ground1_rect)
                    screen.blit(ground2_image, ground2_rect)

                # If the player is dead => Transition to the end_menu
                if self.transition_end_menu: # Correspond to the movement of the bird until he fall on the ground
                    self.bird.move()

                    for pipe in self.list_pipe:
                        pipe.draw()

                    self.bird.update_animation()
                    self.score.display_score()

                    screen.blit(ground1_image, ground1_rect)
                    screen.blit(ground2_image, ground2_rect)

                    if self.bird.collide_ground():
                        self.game = False
                        self.end_menu = True
                        self.transition_end_menu = False

            # If the player is in the end menu
            else:
                screen.blit(background_image, background_rect)

                for pipe in self.list_pipe:
                        pipe.draw()

                self.bird.update_animation()

                screen.blit(ground1_image, ground1_rect)
                screen.blit(ground2_image, ground2_rect)

                screen.blit(game_over_image, game_over_rect)
                screen.blit(ok_button_image, ok_button_rect)
                screen.blit(share_button_image, share_button_rect)

            pygame.display.update()