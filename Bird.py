from Assets import *

class Bird:
    def __init__(self, x, y, screen):

        ## CONSTANTS

        self.screen = screen

        self.dimension_x = 80
        self.dimension_y = 60
        
        self.speed = 0

        self.rota_speed = 10
        self.rota = 0
        self.max_rota = 25

        self.tick_count = 0
        self.anim_time = 5

        self.bird_image = [birds[0].loaded_image(), birds[1].loaded_image(), birds[2].loaded_image()]

        ## Variables
        
        # Current position
        self.x = x
        self.y = y

        self.rect = self.bird_image[0].get_rect(topleft=(self.x, self.y)).center

        # initial y position
        self.init_y = self.y
        
        # Current image of animation
        self.image = self.bird_image[0]

        self.first_move = False
        self.image_count = 0
    
    def reset_pos(self):
        self.x = INIT_POS_BIRD_X
        self.y = INIT_POS_BIRD_Y
        self.rota = 0

    def jump(self):
        self.speed = -10.5 # Negative speed because moves UP
        self.init_y = self.y
        self.tick_count = 0

    def move(self):

        ### Use a lot of physical principle ###

        self.tick_count += 1

        ## X axis movement

        dist = self.speed * self.tick_count + 1.5 * self.tick_count ** 2 # More self.tick_count >> (= time increase), more dist increase

        if dist >= 16:
            dist = 16 # Stop increasing (Too fast otherwise)
        if dist < 0:
            dist -= 2 # If moves UP => Add some speed

        self.y += dist

        ## Rotation movement

        # If bird moves UP or begin to fall (but his position is higher than his initial position)
        if dist < 0 or self.y < self.init_y + 50:
            if self.rota < self.max_rota:
                self.rota = self.max_rota
        else:
            # If bird moves DOWN
            if self.rota > - 90:
                self.rota -= self.rota_speed

    def update_animation(self):

        self.image_count += 1

        if self.image_count < self.anim_time:
            self.image = self.bird_image[0]
        elif self.image_count < self.anim_time * 2:
            self.image = self.bird_image[1]
        elif self.image_count < self.anim_time * 3:
            self.image = self.bird_image[2]
        elif self.image_count < self.anim_time * 4:
            self.image = self.bird_image[1]
        else:
            self.image = self.bird_image[0]
            self.image_count = 0

        # If the rotation is almost vertical
        if self.rota <= -80:
            self.image = self.bird_image[1]
            self.image_count = self.anim_time * 2

        # Display the new image with the good rotation and the good position
        rotated_image = pygame.transform.rotate(self.image, self.rota)
        self.rect = rotated_image.get_rect(center=self.image.get_rect(topleft=(self.x, self.y)).center)
        self.screen.blit(rotated_image, self.rect)

    def collide_ground(self):
        if self.rect.colliderect(ground1_rect) or self.rect.colliderect(ground2_rect):
            return True
        return False

    def get_mask(self):
        return pygame.mask.from_surface(self.image)