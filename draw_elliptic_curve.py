#타원 곡선 그래프 그리기

import pygame
import math

pygame.init()


x_position_array       = []
y_plus_position_array  = []
y_minus_position_array = []



#define the colors : RGB

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

#set screen components
MAP_WIDTH  = 1000
MAP_HEIGHT = 800

REAL_MAP_WIDTH  = 500
REAL_MAP_HEIGHT = 400

MAP_SIZE = [MAP_WIDTH, MAP_HEIGHT]

screen = pygame.display.set_mode(MAP_SIZE)

pygame.display.set_caption("elliptic curve graph")

#loop until the user clicks the close button


clock = pygame.time.Clock()

def get_x(real_x):
    return REAL_MAP_WIDTH  + real_x
def get_y(real_y):
    return REAL_MAP_HEIGHT - real_y

def get_real_x(x):
    return  x - REAL_MAP_WIDTH
def get_real_y(y):
    return -y + REAL_MAP_HEIGHT

def real_elliptic_curve(real_x, a, b):
    return_value = real_x ** 3 + a * real_x + b
    if return_value >= 0:
        y_plus_position_array.append(  get_y( 5 * math.sqrt( return_value ) ) )
        y_minus_position_array.append( get_y( 5 * -math.sqrt( return_value ) ) )
        return True
    else:
        return False

playing = True

def play(playing):

    while playing:

        clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False




        print("a : ")
        a = input()
        a = int(a)

        print("b : ")
        b = input()
        b = int(b)

        screen.fill(WHITE)

        True_count = 0
        for x_position_index in range(0, MAP_WIDTH):
            x_position_index = x_position_index
            judging_draw_elliptic_graph = real_elliptic_curve( get_real_x( x_position_index)/10, a, b )
            if judging_draw_elliptic_graph == True:
                True_count += 1

                if True_count == 2:
                    pygame.draw.aaline(screen, RED, [ x_position_index - 2, y_plus_position_array[ True_count - 2] ], [ x_position_index - 2, y_minus_position_array[ True_count -2]], True)
                if True_count >= 2:
                    print("draw")
                    pygame.draw.aaline(screen, RED, [ x_position_index-2, y_plus_position_array[ True_count - 2] ], [ x_position_index -1, y_plus_position_array[ True_count -1 ] ], True)
                    pygame.draw.aaline(screen, RED, [ x_position_index-2, y_minus_position_array[ True_count - 2] ], [ x_position_index -1, y_minus_position_array[ True_count-1 ] ], True)
                    pygame.display.flip()
            if x_position_index == MAP_WIDTH -1:
                print("Do you want to quit this program : y or n")
                y_or_n = input()
                if y_or_n == 'y':
                    playing = False
        #y_minus_position_array = []
        #y_plus_position_array  = []
        pygame.display.flip()


play(playing)
pygame.quit()


