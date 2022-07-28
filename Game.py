""""Create Flappy Bird's Game :)"""
"""Check the README"""


"""TO DO LIST
=> Make a 'fondu' on images
=> Change images because there are ugly...
=> Add pause button and the pause_menu
"""


#ALL CLASES AND FUNCTIONS
class Bird:
    def __init__(self, x, y, screen):
        self.x = x # x position
        self.y = y # y position
        self.screen = screen # Screen
        self.speed = 0 # Speed of bird
        self.max_rota = 25 # Rotation's maximum
        self.rota = 0 # Current rota
        self.rota_speed = 10 # Speed's rota
        self.anim_time = 5 # Time of animation
        self.tick_count = 0 # Time clock
        self.init_y = self.y # Save init y position
        self.bird_image = [bird_1_image, bird_2_image, bird_3_image] # List of bird's image
        self.image = self.bird_image[0] # Current image
        self.image_count = 0 # Count image
        self.score = 0
        self.best_score = 0
        self.first_move = False

    def jump(self):
        self.speed = - 10.5 # Negative because mooves Up !
        self.init_y = self.y # Initialisation of new y position just before the jump
        self.tick_count = 0 # Initialisation of Time clock

    def move(self):
        self.tick_count += 1

        dist = self.speed * self.tick_count + 1.5 * self.tick_count ** 2 # More self.tick_count >> (= time increase), more dist increase

        if dist >= 16:
            dist = 16 # Stop increasing (Too fast otherwise)
        if dist < 0:
            dist -= 2 # If moove_up => Add some speed

        self.y += dist # Initialise moove

        #Rota moovement
        if dist < 0 or self.y < self.init_y + 50: # If bird mooves up or begin to fall (but his position is higher than his initial position)
            if self.rota < self.max_rota:
                self.rota = self.max_rota
        else:
            if self.rota > - 90: # If bird mooves down
                self.rota -= self.rota_speed # Add some negative rota

    def new_image_and_rect(self):
        self.image_count += 1

        if self.image_count < self.anim_time: # If 0 < self.image_count < 5
            self.image = self.bird_image[0]
        elif self.image_count < self.anim_time * 2: # If 5 < self.image_count < 10
            self.image = self.bird_image[1]
        elif self.image_count < self.anim_time * 3: # If 10 < self.image_count < 15
            self.image = self.bird_image[2]
        elif self.image_count < self.anim_time * 4: # If 15 < self.image_count < 20
            self.image = self.bird_image[1]
        elif self.image_count == self.anim_time * 4 + 1: # If self.image_count = 21
            #Initialisation image and image_count
            self.image = self.bird_image[0]
            self.image_count = 0

        if self.rota <= -80: # If rota almost vertical
            self.image = self.bird_image[1]
            self.image_count = self.anim_time * 2

        #Display new_image with good rotation and good position
        rotated_image = pygame.transform.rotate(self.image, self.rota)
        new_rect = rotated_image.get_rect(center=self.image.get_rect(topleft=(self.x, self.y)).center)
        return [rotated_image, new_rect]

    def draw(self, rotated_image, new_rect):
        self.screen.blit(rotated_image, new_rect)

    def display_score(self):
        white_color = (255, 255, 255)
        font = pygame.font.SysFont("comicsans", 50)
        text_score = font.render("Score : {}".format(self.score), 1, white_color)
        text_best_score = font.render("Best Score : {}".format(self.best_score), 1, white_color)
        self.screen.blit(text_score, (width - text_score.get_width() - 10, 10))
        self.screen.blit(text_best_score, (10, 10))

    def collide_ground(self, new_rect):
        "Detect if the bird collide with the ground => True"
        if new_rect.colliderect(ground1_rect) or new_rect.colliderect(ground2_rect):
            return True
        return False

    def get_mask(self):
        return pygame.mask.from_surface(self.image)


class Pipe:
    def __init__(self, screen, bird, pipe_image):
        self.screen = screen
        self.bird = bird
        self.dimention_y_pipe = 1000
        self.dimension_x_pipe = 140
        self.distance = height / 6  # Distance between two pipes
        self.dist_min = 300 # Minimal distance near wall / ground
        self.dist_ground = int(self.dimention_y_pipe - (5.7 * (height / 7))) # Height of ground
        self.speed = 8 # Pipe's speed
        self.passed_middle = False

        self.pipe_up_image = pipe_image
        self.pos_pipe_up= [width, self.set_height()]
        self.pipe_down_image = pygame.transform.rotate(pipe_image, 180)
        self.pos_pipe_down = [width, self.pos_pipe_up[1] - self.dimention_y_pipe - self.distance]

    def reset_position(self):
        "Reset positions of the pipes"
        self.pos_pipe_up = [width, self.set_height()]
        self.pos_pipe_down = [width, self.pos_pipe_up[1] - self.dimention_y_pipe - self.distance]

    def set_height(self):
        """Generate random number between two specific numbers for 'Up' pipe's height.
           Return the random height"""
        height_number = random.randint(self.dist_min + self.distance, height - self.dist_min - self.dist_ground)
        return height_number

    def update_pos(self, new_x, new_y, image):
        "Update position for images's rects"
        x, y = new_x, new_y
        image_rect = image.get_rect(topleft=(x,y))
        return image_rect

    def moove_alone(self):
        """Moove left and update position.
           Return rect of pipe_images (with update position)"""
        self.pos_pipe_up[0] -= self.speed
        pipe_up_rect = self.update_pos(self.pos_pipe_up[0], self.pos_pipe_up[1], self.pipe_up_image)
        self.pos_pipe_down[0] -= self.speed
        pipe_down_rect = self.update_pos(self.pos_pipe_down[0], self.pos_pipe_down[1], self.pipe_down_image)

        return pipe_up_rect, pipe_down_rect

    def draw(self, rect_pipe_x, rect_pipe_y):
        "Draw bottom and top pipe correctly on the screen"
        self.screen.blit(self.pipe_up_image, rect_pipe_x)
        self.screen.blit(self.pipe_down_image, rect_pipe_y)

    def need_new_pipe(self):
        "Detect if a new pipe must be engaged"
        if not self.passed_middle:
            if self.pos_pipe_up[0] <= width / 2 - 10:
                self.passed_middle = True
                return True

        return False

    def need_destroy_pipe(self):
        "Detect if destroy's decision the pipe must be taken"
        if self.pos_pipe_up[0] <= - self.dimension_x_pipe:
            return True
        return False

    def collide_bird(self):
        """Detect if bird collide with, at least, one pipe
           => Return True
           Technique : With mask => Precision"""
        top_mask =  pygame.mask.from_surface(self.pipe_up_image)
        bottom_mask = pygame.mask.from_surface(self.pipe_down_image)
        bird_mask = self.bird.get_mask()

        top_offset = (self.pos_pipe_up[0] - self.bird.x, self.pos_pipe_up[1] - self.bird.y)
        bottom_offset = (self.pos_pipe_down[0] - self.bird.x, self.pos_pipe_down[1] - self.bird.y)

        top_point_collide = bird_mask.overlap(top_mask, top_offset) # Return None if no points collide
        bottom_point_collide = bird_mask.overlap(bottom_mask, bottom_offset) # Return None if no points collide

        if top_point_collide or bottom_point_collide: # If a point collides between the bird and, at least, one pipe
            return True
        return False


class Game:

    def __init__(self, screen, bird, pipe):
        self.screen = screen
        self.bird = bird
        self.list_pipe = [pipe] # List of pipe
        self.dico_pipe_pos = {pipe : 0}

        self.begin_menu = True
        self.end_menu = False
        self.transition_end_menu = False
        self.game = False
        self.running = True

    def move_ground(self):
        "Do the ground's animation"
        speed_ground = 8
        #Move ground
        ground1_rect.x -= speed_ground
        ground2_rect.x -= speed_ground
        #Respawn picture if out of screen
        if ground1_rect.x <= - width:
            ground1_rect.x = 0
        if ground2_rect.x <= 0:
            ground2_rect.x = width

    def reset_game(self):
        "Reset the game and reinitialise all"
        self.bird.x = width / 2 - bird_dimention_rect_x / 2
        self.bird.y = height / 2 - bird_dimention_rect_y / 2
        self.bird.score = 0
        self.list_pipe = []
        self.list_pipe.append(Pipe(self.screen, self.bird, pipe_image))

    def update_list_pipe(self):
        rem_list = []
        add_list = []
        for pipe in self.list_pipe:
            if pipe.need_new_pipe():
                add_list.append(Pipe(self.screen, self.bird, pipe_image))
                self.bird.score += 1
            if pipe.need_destroy_pipe():
                rem_list.append(pipe)

        for pipe in rem_list:
            self.list_pipe.remove(pipe)
        for pipe in add_list:
            self.list_pipe.append(pipe)

    def end_menu(self, collision):
        exit = False
        while True:
            # Finish the movement of the bird (Fall)
            if collision == "pipe" and not exit:
                self.bird.move()
                rotated_image, new_rect = self.bird.new_image_and_rect()[0], self.bird.new_image_and_rect()[1]
                self.bird.draw(rotated_image, new_rect)
                if self.bird.collide_ground(new_rect):
                    exit = True
            pygame.display.update()


    def run(self):
        clock = pygame.time.Clock()
        click_count = 0
        first_iteration_in_begin_menu = True
        speed_animation_begin_menu = 4
        pos_y_flappy_bird = height / 4
        while self.running:

            clock.tick(30) # 30 Images Per Second (= 30 FPS)

            #Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN and not self.end_menu and not self.begin_menu:
                    if not event.key == pygame.K_ESCAPE: # Idk why 'not'...
                        self.bird.first_move = True
                        if not self.transition_end_menu:
                            self.bird.jump()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos_mouse = pygame.mouse.get_pos()
                    if start_button_rect.collidepoint(pos_mouse[0], pos_mouse[1]):
                        # Initialisation for closing the begin_menu and open the game
                        self.begin_menu = False
                        self.game = True
                        self.bird.x = width / 2 - bird_dimention_rect_x / 2 - 100
                        self.bird.y = height / 2 - bird_dimention_rect_y / 2

            #Displays Game

            if self.begin_menu: # If we are in the begin menu

                #Display images
                self.screen.blit(background_image, background_rect)
                self.screen.blit(ground1_image, ground1_rect)
                self.screen.blit(ground2_image, ground2_rect)
                self.move_ground()
                self.screen.blit(flappy_bird_image, flappy_bird_rect)
                self.screen.blit(start_button_image, start_button_rect)
                self.screen.blit(score_button_image, score_button_rect)
                rotated_image, new_rect = self.bird.new_image_and_rect()[0], self.bird.new_image_and_rect()[1]
                self.bird.draw(rotated_image, new_rect)

                #Update bird's position and title's position
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
                flappy_bird_rect.topleft = (width / 12, pos_y_flappy_bird)


            if self.game: # If we are in the game

                #Update at every moment
                self.screen.blit(background_image, background_rect)
                self.screen.blit(ground1_image, ground1_rect)
                self.screen.blit(ground2_image, ground2_rect)

                #If game is running and the player is not dead
                if not self.transition_end_menu:
                    self.move_ground()

                    if not self.bird.first_move:  # If the player hasn't moved yet
                        self.screen.blit(tap_bird_image, tap_bird_rect)
                        self.screen.blit(get_ready_image, get_ready_rect)

                    if self.bird.first_move:  # If the player has already moved once

                        self.bird.move()

                        self.update_list_pipe()
                        for pipe in self.list_pipe:
                            rect_x, rect_y = pipe.moove_alone()
                            self.dico_pipe_pos[pipe] = 0
                            self.dico_pipe_pos[pipe] = [rect_x, rect_y]
                            pipe.draw(rect_x, rect_y)
                            if pipe.collide_bird():
                                if self.bird.score > self.bird.best_score:
                                    self.bird.best_score = self.bird.score
                                self.transition_end_menu = True

                        if self.bird.collide_ground(new_rect):
                            if self.bird.score > self.bird.best_score:
                                self.bird.best_score = self.bird.score
                            self.game = False
                            self.end_menu = True

                # If the player is dead => Transition to the end_menu (IF PLAYER HIT PIPE, NOT GROUND)
                if self.transition_end_menu: # The movement of the bird until he fall on the ground
                    self.bird.move()

                    for pipe in self.dico_pipe_pos:
                        self.list_pipe[0].draw(self.dico_pipe_pos[pipe][0], self.dico_pipe_pos[pipe][1]) # Same coord than when the player hit the pipe

                    if self.bird.collide_ground(new_rect):
                        self.game = False
                        self.end_menu = True

                rotated_image, new_rect = self.bird.new_image_and_rect()[0], self.bird.new_image_and_rect()[1]
                self.bird.draw(rotated_image, new_rect)
                self.bird.display_score() # Must be after the pipe's draw


            if self.end_menu:  # If we are in the end menu
                self.screen.blit(background_image, background_rect)
                self.screen.blit(ground1_image, ground1_rect)
                self.screen.blit(ground2_image, ground2_rect)
                rotated_image, new_rect = self.bird.new_image_and_rect()[0], self.bird.new_image_and_rect()[1]
                self.bird.draw(rotated_image, new_rect)

            pygame.display.update()

###### RUN THE PROGRAM ############ RUN THE PROGRAM ############ RUN THE PROGRAM ############ RUN THE PROGRAM ######
###### RUN THE PROGRAM ############ RUN THE PROGRAM ############ RUN THE PROGRAM ############ RUN THE PROGRAM ######
###### RUN THE PROGRAM ############ RUN THE PROGRAM ############ RUN THE PROGRAM ############ RUN THE PROGRAM ######

import random
from Assets import *
pygame.font.init()
pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flappy Bird IA")

#All Classes
bird = Bird(width - 80 - 40, height / 4 + 40, screen) #width / 2 - bird_dimention_rect_x / 2, height / 2 - bird_dimention_rect_y / 2, screen
pipe = Pipe(screen, bird, pipe_image)
game = Game(screen, bird, pipe)


if __name__ == '__main__':
    game.run() # Run the game