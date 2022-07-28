import pygame

width, height = 800, 1200

class Asset:
    def __init__(self, link_image, dimension, rect):
        self.link_image = link_image
        self.dimension = dimension
        self.rect = rect

    def loaded_image(self):
        image = pygame.image.load(self.link_image)
        image = pygame.transform.scale(image, self.dimension)
        return image

    def get_image_rect(self):
        image_rect = self.loaded_image().get_rect(topleft=(self.rect[0], self.rect[1]))
        return image_rect

#All images and their rect
ground = Asset("assets/base.png", (width, height / 5), [0, 5.7 * (height / 7)])
ground2 = Asset("assets/base.png", (width, height / 5), [width, 5.7 * (height / 7)])
background = Asset("assets/bg.png", (width, height), [0, 0])
bird_1 = Asset("assets/bird1.png", (80, 60), [200, 600])
bird_2 = Asset("assets/bird2.png", (80, 60), [200, 600])
bird_3 = Asset("assets/bird3.png", (80, 60), [200, 600])

pipe_image = pygame.image.load("../../Flappy Bird - Latest_version/Flappy-Bird/assets/pipe.png")
pipe_image = pygame.transform.scale(pipe_image, (140, 1000))

ground1_image = ground.loaded_image()
ground2_image = ground2.loaded_image()
background_image = background.loaded_image()
bird_1_image = bird_1.loaded_image()
bird_2_image = bird_2.loaded_image()
bird_3_image = bird_3.loaded_image()

ground1_rect = ground.get_image_rect()
ground2_rect = ground2.get_image_rect()
background_rect = background.get_image_rect()
bird_1_rect = bird_1.get_image_rect()
bird_2_rect = bird_2.get_image_rect()
bird_3_rect = bird_3.get_image_rect()

#All dimention_rect
bird_dimention_rect_x = 80
bird_dimention_rect_y = 60
ground_dimention_rect_x = width
ground_dimention_rect_y = height / 5