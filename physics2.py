#### 빗면에서의 물체의 운동 ####



import pygame
import math

pygame.init()

#define index of a velocity list
X = 0
Y = 1

previous_circle_pos_x = []
previous_circle_pos_y = []

#define the colors : RGB

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

#set screen components
MAP_WIDTH  = 1024
MAP_HEIGHT = 800

REAL_MAP_WIDTH  = MAP_WIDTH/2
REAL_MAP_HEIGHT = MAP_HEIGHT/2


def get_x(real_x):
    return REAL_MAP_WIDTH  + real_x
def get_y(real_y):
    return REAL_MAP_HEIGHT - real_y

def get_real_x(x):
    return  x - REAL_MAP_WIDTH
def get_real_y(y):
    return -y + REAL_MAP_HEIGHT

def judging_collision_btw_circle_and_slope(circle_radius, list_circle_pos, slope_inclination, slope_y_intercept): #이거 고쳐야함.... 완료
    list_circle_pos_x = get_real_x( list_circle_pos[X] )
    list_circle_pos_y = get_real_y( list_circle_pos[Y] )
    d = abs( -slope_inclination * list_circle_pos_x + list_circle_pos_y - slope_y_intercept ) / math.sqrt( slope_inclination**2 + 1 )
    if d <= circle_radius:
        print("collision : ( " + str(list_circle_pos_x) + "," + str(list_circle_pos_y) + " )")
        return True
    else:
        return False

MAP_SIZE = [MAP_WIDTH, MAP_HEIGHT]

screen = pygame.display.set_mode(MAP_SIZE)

pygame.display.set_caption("physics2")

#loop until the user clicks the close button


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

class slope:

    def __init__(self, color, has_aa, inclination, y_intercept):
        self.color       = color
        self.has_aa      = has_aa
        self.inclination = inclination
        self.y_intercept = y_intercept

    def set_start_end_point(self, list_start_point, list_end_point):
        self.list_start_point = list_start_point
        self.list_end_point   = list_end_point

    def draw_aaline(self):
        pygame.draw.aaline(screen, self.color, self.list_start_point, self.list_end_point, self.has_aa)
    def get_real_slope_y(self, real_x):
        return self.inclination * real_x + self.y_intercept

#set physics components

#gravity
g   = [0, 0.1]


def play(playing):

    #임시 영역
    print("원의 질량: ")
    temp_mass = input()
    temp_mass = int(temp_mass)

    print("원의 반지름")
    temp_r = input()
    temp_r = int(temp_r)

    print("원 시작 x:")
    temp_x = input()
    print("원 위치 y:")
    temp_y = input()
    temp_list_circle_pos = [get_x(int(temp_x)), get_y(int(temp_y))]

    #__init__ class area
    new_slope        = slope(color = BLACK, has_aa=True, inclination=1, y_intercept=-10)
    new_circle       = circle(color = BLUE , list_pos = temp_list_circle_pos, radius = temp_r, has_fill = 1, mass = temp_mass)

    # 비탈길 그리기
    # 비탈면 함수의 정의역과 시작점,끝점 정의
    slope_domain_x = [-REAL_MAP_WIDTH, REAL_MAP_WIDTH]

    start_x = get_x(slope_domain_x[0])
    end_x   = get_x(slope_domain_x[1])


    start_y = get_y(new_slope.get_real_slope_y(slope_domain_x[0]))
    end_y   = get_y(new_slope.get_real_slope_y(slope_domain_x[1]))

    new_slope.set_start_end_point(list_start_point=[start_x, start_y], list_end_point=[end_x, end_y])

    #직선과 원 충돌 판단 변수
    has_collision_btw_circle_and_slope = False
    while playing:

        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False


        screen.fill(WHITE)

        #previous_circle_pos
        previous_circle_pos_x.append(new_circle.list_pos[X])
        previous_circle_pos_y.append(new_circle.list_pos[Y])

        #draw
        new_slope.draw_aaline()
        new_circle.draw_circle()

        total_delta_x = 0
        total_delta_y = 0
        #물리적 처리


        new_circle.F(g[X], g[Y])
        new_circle.move_circle()

        #원 화면과 충돌판정
        new_circle.judging_collosion()
        #def judging_collision_btw_circle_and_slope(circle_radius, list_circle_pos, slope_inclination, slope_y_intercept):
        has_collision_btw_circle_and_slope        = judging_collision_btw_circle_and_slope(new_circle.radius, new_circle.list_pos, new_slope.inclination, new_slope.y_intercept)
        #충돌로 인한 판정 바로잡기

        if new_circle.list_pos[Y] > get_y( new_slope.get_real_slope_y( get_real_x( new_circle.list_pos[X]) ) ):
            delta_h = int(new_circle.radius / math.cos(math.atan(new_slope.inclination)))
            real_y = new_slope.get_real_slope_y(get_real_x(new_circle.list_pos[X])) + delta_h
            new_circle.set_pos(list_pos=[new_circle.list_pos[X], get_y(real_y)])

        #첫번째 빗면과 충돌이 참이면
        if has_collision_btw_circle_and_slope == True:
            delta_h = int(new_circle.radius / math.cos( math.atan(new_slope.inclination) ))
            real_y = new_slope.get_real_slope_y( get_real_x(new_circle.list_pos[X]) ) + delta_h
            new_circle.set_pos(list_pos=[new_circle.list_pos[X], get_y(real_y)])

            abs_circle_v = math.sqrt( new_circle.list_circle_v2[X]**2 + new_circle.list_circle_v2[Y]**2) #속도 절대값
            #theta = math.acos( (new_circle.list_circle_v2[X]*1 + -new_circle.list_circle_v2[Y]*new_slope.inclination) / (abs_circle_v * math.sqrt(1 + new_slope.inclination**2)) )
            if (new_circle.list_circle_v2[X]*1 + -new_circle.list_circle_v2[Y]*new_slope.inclination) > 0:
                theta = math.acos(
                    -(new_circle.list_circle_v2[X] * 1 + -new_circle.list_circle_v2[Y] * new_slope.inclination) / (
                                abs_circle_v * math.sqrt(1 + new_slope.inclination ** 2)))
                temp_v_x = (
                            new_circle.list_circle_v2[X] * math.cos(2 * theta) - new_circle.list_circle_v2[
                        Y] * math.sin(2 * theta))
                temp_v_y =  (
                            new_circle.list_circle_v2[Y] * math.cos(2 * theta) + new_circle.list_circle_v2[
                        X] * math.sin(2 * theta))
                new_circle.set_v2(list_circle_v2=[temp_v_x, temp_v_y])  # 이게 문제였다.




            else:
                theta = math.acos(
                    (new_circle.list_circle_v2[X] * 1 + -new_circle.list_circle_v2[Y] * new_slope.inclination) / (
                                abs_circle_v * math.sqrt(1 + new_slope.inclination ** 2)))
                temp_v_x = ( new_circle.list_circle_v2[X]*math.cos(2*theta) + new_circle.list_circle_v2[Y]*math.sin(2*theta))
                temp_v_y = ( new_circle.list_circle_v2[Y]*math.cos(2*theta) - new_circle.list_circle_v2[X]*math.sin(2*theta))
                new_circle.set_v2(list_circle_v2=[temp_v_x,temp_v_y] ) # 이게 문제였다.

            # 변경한 좌표 적용
            new_circle.move_circle()




        #draw #원의 중심의 자취 그리기
        for i in range(  len( previous_circle_pos_x ) - 1 ):
            pygame.draw.aaline(screen, GREEN,[ previous_circle_pos_x[i], previous_circle_pos_y[i] ], [ previous_circle_pos_x[i+1], previous_circle_pos_y[i+1] ], True )
        #화면 초기화 + 값 초기화
        pygame.display.flip()

#get slope's function


#get real coordinate system position





play(True)
pygame.quit()





