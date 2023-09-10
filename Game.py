from Assets import *
from Pipe import Pipe

class Game:

    def __init__(self, screen, bird, pipe, score):
        self.screen = screen
        self.bird = bird
        self.score = score
        self.list_pipe = [pipe] # List of pipe
        self.dico_pipe_pos = {pipe : 0}

        self.begin_menu = True
        self.transition_end_menu = False
        self.end_menu = False
        self.game = False
        self.running = True
        self.FPS = 30

    def move_ground(self):
        "Make the ground's animation"
        ground1_rect.x -= SPEED_GROUND
        ground2_rect.x -= SPEED_GROUND
        
        if ground1_rect.x <= - WIDTH:
            ground1_rect.x = 0
        if ground2_rect.x <= 0:
            ground2_rect.x = WIDTH

    def reset_game(self):
        "Reset the game and reinitialise all"
        self.bird.x = WIDTH / 2 - self.bird.dimension_x / 2
        self.bird.y = HEIGHT / 2 - self.bird.dimension_y / 2
        self.score.score = 0
        self.list_pipe = []
        self.list_pipe.append(Pipe(self.screen, self.bird, pipe_image))

    def update_list_pipe(self):
        rem_list = []
        add_list = []
        for pipe in self.list_pipe:
            if pipe.need_new_pipe():
                add_list.append(Pipe(self.screen, self.bird, pipe_image))
            if pipe.need_destroy_pipe():
                rem_list.append(pipe)

        for pipe in rem_list:
            self.list_pipe.remove(pipe)
        for pipe in add_list:
            self.list_pipe.append(pipe)


    def run(self):

        clock = pygame.time.Clock()
        click_count = 0
        first_iteration_in_begin_menu = True
        speed_animation_begin_menu = 4
        pos_y_flappy_bird = HEIGHT / 4

        while self.running:

            clock.tick(self.FPS)

            #Events
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
                            self.bird.x = WIDTH / 2 - self.bird.dimension_x / 2 - 100
                            self.bird.y = HEIGHT / 2 - self.bird.dimension_y / 2
                    if self.end_menu:
                        if ok_button_rect.collidepoint(pos_mouse[0], pos_mouse[1]):
                            self.end_menu = False
                            self.begin_menu = True
                            self.bird.reset_pos()
                            self.bird.first_move = False
                            self.list_pipe = [Pipe(self.screen, self.bird, pipe_image)]
                            self.dico_pipe_pos = {}


            # Displays Game

            if self.begin_menu: # If we are in the begin menu

                # Display images
                self.screen.blit(background_image, background_rect)
                self.screen.blit(ground1_image, ground1_rect)
                self.screen.blit(ground2_image, ground2_rect)
                self.move_ground()
                self.screen.blit(flappy_bird_image, flappy_bird_rect)
                self.screen.blit(start_button_image, start_button_rect)
                self.screen.blit(score_button_image, score_button_rect)
                self.bird.update_animation()

                # Update bird's position and title's position
                click_count += 1

                if first_iteration_in_begin_menu:
                    if click_count % 10 == 0:  # after 0.33 second
                        speed_animation_begin_menu *= -1
                        first_iteration_in_begin_menu = False
                        click_count = 0
                else:
                    if click_count % 20 == 0:  # after 0.66 second
                        speed_animation_begin_menu *= -1

                self.bird.y += speed_animation_begin_menu
                pos_y_flappy_bird += speed_animation_begin_menu
                flappy_bird_rect.topleft = (WIDTH / 12, pos_y_flappy_bird)

            if self.game: # If we are in the game

                # Update at every moment
                self.screen.blit(background_image, background_rect)

                # If the game is running and the player is not dead
                if not self.transition_end_menu:

                    self.move_ground()

                    if not self.bird.first_move:  # If the player hasn't moved yet
                        self.screen.blit(tap_bird_image, tap_bird_rect)
                        self.screen.blit(get_ready_image, get_ready_rect)

                    if self.bird.first_move:  # If the player has already moved once

                        self.bird.move()

                        self.update_list_pipe()
                        for pipe in self.list_pipe:

                            if pipe.bird_deserve_score():
                                self.score.score += 1

                            rect_x, rect_y = pipe.move_alone()
                            self.dico_pipe_pos[pipe] = 0
                            self.dico_pipe_pos[pipe] = [rect_x, rect_y]
                            pipe.draw(rect_x, rect_y)
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
                    self.score.display_score()  # Must be after the pipe's draw
                    self.screen.blit(ground1_image, ground1_rect)
                    self.screen.blit(ground2_image, ground2_rect)

                # If the player is dead => Transition to the end_menu
                if self.transition_end_menu: # The movement of the bird until he fall on the ground
                    self.bird.move()

                    for pipe in self.dico_pipe_pos:
                        self.list_pipe[0].draw(self.dico_pipe_pos[pipe][0], self.dico_pipe_pos[pipe][1]) # Same coord than when the player hit the pipe

                    self.bird.update_animation()
                    self.score.display_score()  # Must be after the pipe's draw
                    self.screen.blit(ground1_image, ground1_rect)
                    self.screen.blit(ground2_image, ground2_rect)

                    if self.bird.collide_ground():
                        self.game = False
                        self.end_menu = True
                        self.transition_end_menu = False


            if self.end_menu:  # If we are in the end menu
                self.screen.blit(background_image, background_rect)
                for pipe in self.dico_pipe_pos:
                    self.list_pipe[0].draw(self.dico_pipe_pos[pipe][0], self.dico_pipe_pos[pipe][1])  # Same coord than when the player hit the pipe
                self.bird.update_animation()
                self.screen.blit(ground1_image, ground1_rect)
                self.screen.blit(ground2_image, ground2_rect)
                self.screen.blit(game_over_image, game_over_rect)
                self.screen.blit(ok_button_image, ok_button_rect)
                self.screen.blit(share_button_image, share_button_rect)

            pygame.display.update()