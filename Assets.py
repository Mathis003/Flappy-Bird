import pygame

# Configs

WIDTH, HEIGHT = 800, 1200
WHITE = (255, 255, 255)

INIT_POS_BIRD_X = 17/20 * WIDTH
INIT_POS_BIRD_Y = 17/60 * HEIGHT

SPEED_GROUND = 8

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


## All images and their rect ##

# Game elements #

background = Asset("assets/game/bg.png", (WIDTH, HEIGHT), [0, 0])
background_image = background.loaded_image()
background_rect = background.get_image_rect()

pipe = Asset("assets/game/pipe.png",  (140, 1000), None)
pipe_image = pipe.loaded_image()

grounds = [Asset("assets/game/base.png", (WIDTH, HEIGHT / 5), [0, 5.7 * (HEIGHT / 7)]),
           Asset("assets/game/base.png", (WIDTH, HEIGHT / 5), [WIDTH, 5.7 * (HEIGHT / 7)])
          ]
ground1_image = grounds[0].loaded_image()
ground2_image = grounds[1].loaded_image()
ground1_rect = grounds[0].get_image_rect()
ground2_rect = grounds[1].get_image_rect()


birds = [Asset("assets/game/bird/bird1.png", (80, 60), [WIDTH - 80 - 20, HEIGHT / 4]),
         Asset("assets/game/bird/bird2.png", (80, 60), [WIDTH - 80 - 20, HEIGHT / 4]),
         Asset("assets/game/bird/bird3.png", (80, 60), [WIDTH - 80 - 20, HEIGHT / 4])
        ]

bird_1_rect = birds[0].get_image_rect()
bird_2_rect = birds[1].get_image_rect()
bird_3_rect = birds[2].get_image_rect()

# Menu elements #

flappy_bird = Asset("assets/menu/Flappy_Bird_title.png", ((WIDTH / 3) * 2.2, HEIGHT / 8), [WIDTH / 12, HEIGHT / 4])
flappy_bird_image = flappy_bird.loaded_image()
flappy_bird_rect = flappy_bird.get_image_rect()

tap_bird = Asset("assets/menu/tap_bird.png", (300, HEIGHT / 4), [270, 500])
tap_bird_image = tap_bird.loaded_image()
tap_bird_rect = tap_bird.get_image_rect()


get_ready = Asset("assets/menu/get_ready.png", (500, 100), [150, 300])
get_ready_image = get_ready.loaded_image()
get_ready_rect = get_ready.get_image_rect()

game_over = Asset("assets/menu/game_over.png", (600, 150), [100, 200])
game_over_image = game_over.loaded_image()
game_over_rect = game_over.get_image_rect()


start_button = Asset("assets/menu/start_button.jpg", (WIDTH / 3.5, HEIGHT / 15), [WIDTH / 8, 4.3 * (HEIGHT / 6)])
start_button_image = start_button.loaded_image()
start_button_rect = start_button.get_image_rect()

score_button = Asset("assets/menu/score_button.jpg", (WIDTH / 3.5, HEIGHT / 15), [4.8 * (WIDTH / 8), 4.3 * (HEIGHT / 6)])
score_button_image = score_button.loaded_image()
score_button_rect = score_button.get_image_rect()

ok_button = Asset("assets/menu/ok_button.png",  (WIDTH / 3.5, HEIGHT / 15), [WIDTH / 8, 4.3 * (HEIGHT / 6)])
ok_button_image = ok_button.loaded_image()
ok_button_rect = ok_button.get_image_rect()

share_button = Asset("assets/menu/share_button.png", (WIDTH / 3.5, HEIGHT / 15), [4.8 * (WIDTH / 8), 4.3 * (HEIGHT / 6)])
share_button_image = share_button.loaded_image()
share_button_rect = share_button.get_image_rect()


# All dimension_rect

ground_dimension_rect_x = WIDTH
ground_dimension_rect_y = HEIGHT / 5

start_x_play_button = WIDTH / 8
start_y_play_button = 4.3 * (HEIGHT / 6)