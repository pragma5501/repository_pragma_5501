import pygame
import math
import random

pygame.init()

X = 0
Y = 1

R = 0
G = 1
B = 2

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PINK = (255, 181,197)


map_size = [1024, 800]
SCREEN_WIDTH  = map_size[0]
SCREEN_HEIGHT = map_size[1]

MAP_WIDTH  = 1024
MAP_HEIGHT = 800

REAL_MAP_WIDTH  = MAP_WIDTH/2
REAL_MAP_HEIGHT = MAP_HEIGHT/2


screen = pygame.display.set_mode(map_size)

pygame.display.set_caption("gradation")


done = False
clock = pygame.time.Clock()

class circle:
    def __init__(self, color, list_pos, radius, has_fill, mass):
        self.color    = color
        self.list_pos = list_pos
        self.radius   = radius
        if has_fill == 0:
            self.has_fill = 2
        else:
            self.has_fill = 0
        self.mass     = mass

    def set_v2(self, list_circle_v2):
        self.list_circle_v2 = list_circle_v2

    def set_pos(self, list_pos):
        self.list_pos = list_pos

    def judging_collosion(self):
        if (self.list_pos[X] + self.radius) >= MAP_WIDTH:
            self.list_pos[X] = MAP_WIDTH - self.radius
            self.list_circle_v2[X] = -self.list_circle_v2[X]


        if (self.list_pos[X] - self.radius) <= 0:
            self.list_pos[X] = self.radius
            self.list_circle_v2[X] = -self.list_circle_v2[X]

        if(self.list_pos[Y] + self.radius) >= MAP_HEIGHT:
            self.list_pos[Y] = MAP_HEIGHT - self.radius
            self.list_circle_v2[Y] =-self.list_circle_v2[Y]

        if (self.list_pos[Y] - self.radius) <= 0:
            self.list_pos[Y] = self.radius
            self.list_circle_v2[Y] = -self.list_circle_v2[Y]

    def F(self, F_x, F_y):
        self.list_circle_v2[X] += F_x
        self.list_circle_v2[Y] += F_y
    def move_circle(self):
        self.list_pos[X] += self.list_circle_v2[X]
        self.list_pos[Y] += self.list_circle_v2[Y]
    def draw_circle(self):
        pygame.draw.circle(screen, self.color, self.list_pos, self.radius, self.has_fill)

    list_circle_v2 = [0,0]


def draw_circle_gradation(radius, circle_main_color, list_pos):
    for i in range(0, radius):
        gradation_circle_main_color = [ circle_main_color[R] * (i / radius) % 0xff, circle_main_color[G] * (i / radius) % 0xff,
                                       circle_main_color[B] * (i / radius) % 0xff]

        pygame.draw.circle(screen, gradation_circle_main_color, list_pos, i, 2)



while not done:

    number_of_circle = 10
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)



    draw_circle_gradation(500, PINK, [500, 500])
    #list_mouse_previous_pos = list_mouse_pos

    pygame.display.flip()




pygame.quit()
