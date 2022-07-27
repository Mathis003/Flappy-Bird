from Assets import *

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

    def jump(self):
        self.speed = - 10.5 # Negative because mooves Up !
        self.init_y = self.y # Initialisation of new y position just before the jump
        self.tick_count = 0 # Initialisation of Time clock

    def moove(self):
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

    def get_mask(self): # FOR LATER
        return pygame.mask.from_surface(self.image)