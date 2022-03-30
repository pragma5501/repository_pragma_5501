
import pygame
import math

pygame.init()



BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PINK = (255, 181,197)


size = [1000, 1000]
SCREEN_WIDTH  = size[0]
SCREEN_HEIGHT = size[1]

screen = pygame.display.set_mode(size)


pygame.display.set_caption("수학창작물 대회 3306김경민")

#position_processing
X = 0
Y = 1

#string
string_position_x_array   = []
string_position_y_array   = []
string_position_y_default = SCREEN_HEIGHT / 2

string_weight = 1
list_string_weight = []

delta_y_limit = 100

for x in range(0, SCREEN_WIDTH):
    string_position_x_array.append( x )
    string_position_y_array.append( string_position_y_default )

    list_string_weight.append( string_weight )



#mouse

mouse_circle_radius = 30
list_mouse_now_pos      = pygame.mouse.get_pos()
list_mouse_previous_pos = pygame.mouse.get_pos()

#vector
direction_vector_2D = [0.0, 0.0]



done = False
clock = pygame.time.Clock()

while not done:

    has_collision = False
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)

    list_mouse_pos = pygame.mouse.get_pos()
    pygame.draw.circle(screen, PINK, list_mouse_pos, mouse_circle_radius)

    if -10 < direction_vector_2D[X] < 10 and -10 < direction_vector_2D[Y] < 10:
    #원이 줄에 닿아는지 체크
        for x in range(0 , SCREEN_WIDTH ):
            distance_btw_circle_string = math.sqrt(   (list_mouse_pos[X] - string_position_x_array[x] ) ** 2
                                                    + ( list_mouse_pos[Y] - string_position_y_array[x] ) ** 2 )

            if distance_btw_circle_string <= mouse_circle_radius:
                has_collision = True
                list_mouse_next_pos = pygame.mouse.get_pos()
                direction_vector_2D = [ -list_mouse_next_pos[X] + list_mouse_now_pos[X],
                                       -list_mouse_next_pos[Y] + list_mouse_now_pos[Y]]


                print(list_mouse_now_pos[X] - list_mouse_previous_pos[X])


                for i in range(0, SCREEN_WIDTH):
                    if( i <= x and x>0):
                        list_string_weight[i] = i / x * (math.pi/2)
                    else:
                        list_string_weight[i] = ( SCREEN_WIDTH - i ) / ( SCREEN_WIDTH - x ) * (math.pi/2)
                    if abs( string_position_y_array[i] - string_position_y_default ) < delta_y_limit:
                        string_position_x_array[i] = string_position_x_array[i] + direction_vector_2D[X] * math.sin( list_string_weight[i] )
                        string_position_y_array[i] = string_position_y_array[i] + direction_vector_2D[Y] * math.sin( list_string_weight[i] )

                break

    if has_collision == False:
        BOUNCE = 0.95
        direction_vector_2D = [ -BOUNCE * direction_vector_2D[X], -BOUNCE * direction_vector_2D[Y]  ]

        for x in range(0, SCREEN_WIDTH):

            string_position_x_array[x] = string_position_x_array[x] + 2*direction_vector_2D[X] * math.sin( list_string_weight[x] )
            string_position_y_array[x] = string_position_y_array[x] + 2*direction_vector_2D[Y] * math.sin( list_string_weight[x] )



    for x in range(0, SCREEN_WIDTH-1):
        previous_x = string_position_x_array[x]
        previous_y = string_position_y_array[x]

        next_x     = string_position_x_array[x+1]
        next_y     = string_position_y_array[x+1]

        pygame.draw.aaline(screen, BLUE, [previous_x, previous_y], [next_x, next_y], True )

    #list_mouse_previous_pos = list_mouse_pos
    pygame.display.flip()




pygame.quit()
