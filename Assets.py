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
bird_1 = Asset("assets/bird1.png", (80, 60), [width - 80 - 20, height / 4]) # 200, 600
bird_2 = Asset("assets/bird2.png", (80, 60), [width - 80 - 20, height / 4])
bird_3 = Asset("assets/bird3.png", (80, 60), [width - 80 - 20, height / 4])
flappy_bird = Asset("assets/Flappy_Bird-removebg-preview.png", ((width / 3) * 2.2, height / 8), [width / 12, height / 4])
start_button = Asset("assets/start_button.jpg", (width / 3.5, height / 15), [width / 8, 4.3 * (height / 6)])
score_button = Asset("assets/score_button.jpg", (width / 3.5, height / 15), [4.8 * (width / 8), 4.3 * (height / 6)])
tap_bird = Asset("assets/tap_bird-removebg-preview.png", (300, height / 4), [270, 500])
get_ready = Asset("assets/get_ready.png", (500, 100), [150, 300])

get_ready_image = get_ready.loaded_image()
get_ready_rect = get_ready.get_image_rect()

tap_bird_image = tap_bird.loaded_image()
tap_bird_rect = tap_bird.get_image_rect()

start_button_image = start_button.loaded_image()
start_button_rect = start_button.get_image_rect()

score_button_image = score_button.loaded_image()
score_button_rect = score_button.get_image_rect()

flappy_bird_image = flappy_bird.loaded_image()
flappy_bird_rect = flappy_bird.get_image_rect()

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
start_x_play_button = width / 8
start_y_play_button = 4.3 * (height / 6)