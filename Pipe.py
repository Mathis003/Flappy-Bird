import random
from Assets import *

class Pipe:
    def __init__(self, screen, pipe_image):
        self.screen = screen
        self.dimention_y_pipe = 1000
        self.distance = height / 6  # Distance between two pipes
        self.dist_min = 300 # Minimal distance near walls
        self.dist_ground = int(self.dimention_y_pipe - (5.7 * (height / 7)))
        self.speed = 8

        self.pipe1_up_image = pipe_image
        self.pos_pipe1_up= [width, self.generate_random_number()]
        self.pipe1_down_image = pygame.transform.rotate(pipe_image, 180)
        self.pos_pipe1_down = [width, self.pos_pipe1_up[1] - self.dimention_y_pipe - self.distance]
        self.pipe2_up_image = pipe_image
        self.pos_pipe2_up = [(3 / 2) * width, self.generate_random_number()]
        self.pipe2_down_image = pygame.transform.rotate(pipe_image, 180)
        self.pos_pipe2_down = [(3 / 2) * width, self.pos_pipe2_up[1] - self.dimention_y_pipe - self.distance]
        self.pipe3_up_image = pipe_image
        self.pos_pipe3_up = [2 * width, self.generate_random_number()]
        self.pipe3_down_image = pygame.transform.rotate(pipe_image, 180)
        self.pos_pipe3_down = [2 * width, self.pos_pipe3_up[1] - self.dimention_y_pipe - self.distance]

    def initial_position(self):
        self.pos_pipe1_up = [width, self.generate_random_number()]
        self.pos_pipe1_down = [width, self.pos_pipe1_up[1] - self.dimention_y_pipe - self.distance]
        self.pos_pipe2_up = [(3 / 2) * width, self.generate_random_number()]
        self.pos_pipe2_down = [(3 / 2) * width, self.pos_pipe2_up[1] - self.dimention_y_pipe - self.distance]
        self.pos_pipe3_up = [2 * width, self.generate_random_number()]
        self.pos_pipe3_down = [2 * width, self.pos_pipe3_up[1] - self.dimention_y_pipe - self.distance]

    def generate_random_number(self):
        "Generate random number between two specific numbers for 'Up' pipe"
        random_number = random.randint(self.dist_min + self.distance, height - self.dist_min - self.dist_ground)
        return random_number

    def update_pos(self, new_x, new_y, image):
        x, y = new_x, new_y
        image_rect = image.get_rect(topleft=(x,y))
        return image_rect

    def moove_alone(self):
        # Moove left and update position
        self.pos_pipe1_up[0] -= self.speed
        pipe1_up_rect = self.update_pos(self.pos_pipe1_up[0], self.pos_pipe1_up[1], self.pipe1_up_image)

        self.pos_pipe1_down[0] -= self.speed
        pipe1_down_rect = self.update_pos(self.pos_pipe1_down[0], self.pos_pipe1_down[1], self.pipe1_down_image)

        self.pos_pipe2_up[0] -= self.speed
        pipe2_up_rect = self.update_pos(self.pos_pipe2_up[0], self.pos_pipe2_up[1], self.pipe2_up_image)

        self.pos_pipe2_down[0] -= self.speed
        pipe2_down_rect = self.update_pos(self.pos_pipe2_down[0], self.pos_pipe2_down[1], self.pipe2_down_image)

        self.pos_pipe3_up[0] -= self.speed
        pipe3_up_rect = self.update_pos(self.pos_pipe3_up[0], self.pos_pipe3_up[1], self.pipe3_up_image)

        self.pos_pipe3_down[0] -= self.speed
        pipe3_down_rect = self.update_pos(self.pos_pipe3_down[0], self.pos_pipe3_down[1], self.pipe3_down_image)

        dim_pipe_image_x = width / 3.6
        # If image is out of the map => Initialise the init position
        if self.pos_pipe1_up[0] <= - dim_pipe_image_x:
            self.pos_pipe1_up[0] = width + dim_pipe_image_x
            self.pos_pipe1_up[1] = self.generate_random_number()
            self.pos_pipe1_down[0] = width + dim_pipe_image_x
            self.pos_pipe1_down[1] = self.pos_pipe1_up[1] - self.dimention_y_pipe - self.distance
            pipe1_up_rect = self.update_pos(self.pos_pipe1_up[0], self.pos_pipe1_up[1], self.pipe1_up_image)
            pipe1_down_rect = self.update_pos(self.pos_pipe1_down[0], self.pos_pipe1_down[1], self.pipe1_down_image)
        if self.pos_pipe2_up[0] <= - dim_pipe_image_x:
            self.pos_pipe2_up[0] = width + dim_pipe_image_x
            self.pos_pipe2_up[1] = self.generate_random_number()
            self.pos_pipe2_down[0] = width + dim_pipe_image_x
            self.pos_pipe2_down[1] = self.pos_pipe2_up[1] - self.dimention_y_pipe - self.distance
            pipe2_up_rect = self.update_pos(self.pos_pipe2_up[0], self.pos_pipe2_up[1], self.pipe2_up_image)
            pipe2_down_rect = self.update_pos(self.pos_pipe2_down[0], self.pos_pipe2_down[1], self.pipe2_down_image)
        if self.pos_pipe3_up[0] <= - dim_pipe_image_x:
            self.pos_pipe3_up[0] = width + dim_pipe_image_x
            self.pos_pipe3_up[1] = self.generate_random_number()
            self.pos_pipe3_down[0] = width + dim_pipe_image_x
            self.pos_pipe3_down[1] = self.pos_pipe3_up[1] - self.dimention_y_pipe - self.distance
            pipe3_up_rect = self.update_pos(self.pos_pipe3_up[0], self.pos_pipe3_up[1], self.pipe3_up_image)
            pipe3_down_rect = self.update_pos(self.pos_pipe3_down[0], self.pos_pipe3_down[1], self.pipe3_down_image)

        #Display all pipe
        self.screen.blit(self.pipe1_up_image, pipe1_up_rect)
        self.screen.blit(self.pipe1_down_image, pipe1_down_rect)
        self.screen.blit(self.pipe2_up_image, pipe2_up_rect)
        self.screen.blit(self.pipe2_down_image, pipe2_down_rect)
        self.screen.blit(self.pipe3_up_image, pipe3_up_rect)
        self.screen.blit(self.pipe3_down_image, pipe3_down_rect)