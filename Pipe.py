from Assets import *
import random

class Pipe:
    def __init__(self, screen, bird, pipe_image):

        ## CONSTANTS

        self.screen = screen
        self.bird = bird

        self.dimension_x = 140
        self.dimension_y = 1000

        self.speed = 8
        self.dist_ground = int(self.dimension_y - (5.7 * (HEIGHT / 7))) # Height of ground
        self.distance = HEIGHT / 6  # Distance between two pipes
        self.dist_min = 300 # Minimal distance near wall/ground

        self.image_up = pipe_image
        self.image_down = pygame.transform.rotate(pipe_image, 180)

        ## VARIABLES

        self.pos_up= [WIDTH, self.set_height()]
        self.pos_down = [WIDTH, self.pos_up[1] - self.dimension_y - self.distance]

        self.rect_up = self.image_up.get_rect(topleft=(self.pos_up[0], self.pos_up[1]))
        self.rect_down = self.image_down.get_rect(topleft=(self.pos_down[0], self.pos_down[1]))

        self.passed_middle = False
        self.passed_pipe = False

    def reset_position(self):
        self.pos_up = [WIDTH, self.set_height()]
        self.pos_down = [WIDTH, self.pos_pipe_up[1] - self.dimension_y - self.distance]

    def set_height(self):
        return random.randint(self.dist_min + self.distance, HEIGHT - self.dist_min - self.dist_ground)

    def update_pos(self, new_x, new_y, image):
        return image.get_rect(topleft=(new_x, new_y))

    def move_alone(self):
        self.pos_up[0] -= self.speed
        self.rect_up = self.update_pos(self.pos_up[0], self.pos_up[1], self.image_up)
        self.pos_down[0] -= self.speed
        self.rect_down = self.update_pos(self.pos_down[0], self.pos_down[1], self.image_down)

        self.draw(self.rect_up, self.rect_down)

    def draw(self, rect_pipe_x, rect_pipe_y):
        self.screen.blit(self.image_up, rect_pipe_x)
        self.screen.blit(self.image_down, rect_pipe_y)

    def need_new_pipe(self):
        if not self.passed_middle:
            if self.pos_up[0] <= WIDTH / 2 - 10:
                self.passed_middle = True
                return True
        return False

    def need_destroy_pipe(self):
        return (self.pos_up[0] <= - self.dimension_x)

    def bird_passed(self):
        if not self.passed_pipe:
            if self.pos_up[0] + self.dimension_x <= WIDTH / 2 - self.bird.dimension_x / 2 - 100:
                self.passed_pipe = True
                return True
        return False

    def collide_bird(self):
        top_mask =  pygame.mask.from_surface(self.image_up)
        bottom_mask = pygame.mask.from_surface(self.image_down)
        bird_mask = self.bird.get_mask()

        top_offset = (self.pos_up[0] - self.bird.x, self.pos_up[1] - self.bird.y)
        bottom_offset = (self.pos_down[0] - self.bird.x, self.pos_down[1] - self.bird.y)

        top_point_collide = bird_mask.overlap(top_mask, top_offset) # Return None if no points collide
        bottom_point_collide = bird_mask.overlap(bottom_mask, bottom_offset) # Return None if no points collide

        if top_point_collide or bottom_point_collide: # If a point collides between the bird and, at least, one pipe
            return True
        return False