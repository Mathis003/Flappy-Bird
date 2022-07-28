""""Create Flappy Bird's Game :)"""
"""Check the README"""

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
        self.anim_time = 3 # Time of animation
        self.tick_count = 0 # Time clock
        self.init_y = self.y # Save init y position
        self.bird_image = [bird_1_image, bird_2_image, bird_3_image] # List of bird's image
        self.image = self.bird_image[0] # Current image
        self.image_count = 0 # Count image
        self.score = 0

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

        if self.image_count < self.anim_time: # If 0 < self.image_count < 3
            self.image = self.bird_image[0]
        elif self.image_count < self.anim_time * 2: # If 3 < self.image_count < 6
            self.image = self.bird_image[1]
        elif self.image_count < self.anim_time * 3: # If 6 < self.image_count < 9
            self.image = self.bird_image[2]
        elif self.image_count < self.anim_time * 4: # If 9 < self.image_count < 12
            self.image = self.bird_image[1]
        elif self.image_count == self.anim_time * 4 + 1: # If self.image_count = 13
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
        text = font.render("Score : {}".format(self.score), 1, white_color)
        self.screen.blit(text, (width - text.get_width() - 10, 10))

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

        return [pipe_up_rect, pipe_down_rect]

    def draw(self):
        "Draw bottom and top pipe correctly on the screen"
        rect_pipe = self.moove_alone()
        self.screen.blit(self.pipe_up_image, rect_pipe[0])
        self.screen.blit(self.pipe_down_image, rect_pipe[1])

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

    def run(self):
        clock = pygame.time.Clock()
        while self.running:

            clock.tick(30) # 30 Images Per Second (= 30 FPS)

            #Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if not event.key == pygame.K_ESCAPE: # Idk why 'not'...
                        self.bird.jump()

            #Displays Game
            self.bird.move()

            self.screen.blit(background_image, background_rect)

            self.update_list_pipe()
            for pipe in self.list_pipe:
                pipe.draw()
                if pipe.collide_bird():
                    self.reset_game()

            self.bird.display_score()

            self.screen.blit(ground1_image, ground1_rect)
            self.screen.blit(ground2_image, ground2_rect)
            self.move_ground()

            rotated_image, new_rect = self.bird.new_image_and_rect()[0], self.bird.new_image_and_rect()[1]
            self.bird.draw(rotated_image, new_rect)
            if self.bird.collide_ground(new_rect):
                self.reset_game()

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
bird = Bird(width / 2 - bird_dimention_rect_x / 2, height / 2 - bird_dimention_rect_y / 2, screen) # 80, 60 = dimension_rect_x, dimension_rect_y
pipe = Pipe(screen, bird, pipe_image)
game = Game(screen, bird, pipe)


if __name__ == '__main__':
    game.run() # Run the game