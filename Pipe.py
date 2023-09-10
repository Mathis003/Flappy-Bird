from Assets import *
import random

class Pipe:
    def __init__(self, screen, bird, pipe_image):
        self.screen = screen
        self.bird = bird
        self.dimension_y = 1000
        self.dimension_x = 140
        self.distance = HEIGHT / 6  # Distance between two pipes
        self.dist_min = 300 # Minimal distance near wall / ground
        self.dist_ground = int(self.dimension_y - (5.7 * (HEIGHT / 7))) # Height of ground
        self.speed = 8 # Pipe's speed
        self.passed_middle = False
        self.passed_pipe = False

        self.pipe_up_image = pipe_image
        self.pos_pipe_up= [WIDTH, self.set_height()]
        self.pipe_down_image = pygame.transform.rotate(pipe_image, 180)
        self.pos_pipe_down = [WIDTH, self.pos_pipe_up[1] - self.dimension_y - self.distance]

    def reset_position(self):
        "Reset positions of the pipes"
        self.pos_pipe_up = [WIDTH, self.set_height()]
        self.pos_pipe_down = [WIDTH, self.pos_pipe_up[1] - self.dimension_y - self.distance]

    def set_height(self):
        """Generate random number between two specific numbers for 'Up' pipe's height.
           Return the random height"""
        height_number = random.randint(self.dist_min + self.distance, HEIGHT - self.dist_min - self.dist_ground)
        return height_number

    def update_pos(self, new_x, new_y, image):
        "Update position for images's rects"
        x, y = new_x, new_y
        image_rect = image.get_rect(topleft=(x,y))
        return image_rect

    def move_alone(self):
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
            if self.pos_pipe_up[0] <= WIDTH / 2 - 10:
                self.passed_middle = True
                return True

        return False

    def need_destroy_pipe(self):
        "Detect if destroy's decision the pipe must be taken"
        if self.pos_pipe_up[0] <= - self.dimension_x:
            return True
        return False

    def bird_deserve_score(self):
        "Return True if the bird has passed completely the pipe, False otherwise"
        if not self.passed_pipe:
            if self.pos_pipe_up[0] + self.dimension_x <= WIDTH / 2 - self.bird.dimension_x / 2 - 100:
                self.passed_pipe = True
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