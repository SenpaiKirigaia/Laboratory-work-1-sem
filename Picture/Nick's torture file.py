import pygame
from pygame.draw import *
import random

pygame.init()

COLOR = {
    'black':(0, 0, 0),
    'notblack':(1, 0, 0), #Данный черный цвет используется у автора картины))
    'white':(255, 255, 255),
    'red': (255, 0, 0),
    'lime': (0, 255, 0),
    'blue': (0, 0, 255),
    'yellow': (255, 255, 0),
    'cyan': (0, 255, 255),
    'gray': (128, 128, 128),
    'purple': (128, 0, 128),
    'green': (0, 128, 0),
    'gold': (255, 215, 0),
    'house': (186, 196, 199),
    'tower1': (222, 227, 226),
    'tower2': (118, 144, 138),
    'tower3': (153, 171, 167)
    }

S_w = 794
S_h = 1123

FPS = 30
screen = pygame.display.set_mode((S_w, S_h))
screen.fill((255, 255, 255))

def draw_car(x, y, size, a, color): #car(300, 1000, 0.3, a)
    """
    draw_car рисует машину
    x, y -- координаты расположения машины
    size -- коэффицент, для размера машины 
    a -- направление машины (0.3 - влево, 1 - вправо) 
    #a было использованно у автора, данного творения, и я его оставил, так как оно работает?
    color - цвет в ординарных ковычках, example: 'black'
    """
    ellipse(screen, (10, 33, 42), (x - 30 * size + a * 330 * size, y + 42 * size, 60 * size, 10 * size))
    rect(screen, COLOR[color], (x, y, 330 * size, 60 * size)) #корпус
    rect(screen, COLOR[color], (25 * a * size + 70 * size + x, y - 30 * size, 165 * size, 60 * size)) #кабина
    rect(screen, (220, 245, 254), (25 * a * size + 80 * size + x, y - 20 * size, 50 * size, 25 * size))
    rect(screen, (220, 245, 254), (25 * a * size + 170 * size + x, y - 20 * size, 50 * size, 25 * size))
    ellipse(screen, (10, 33, 42), (35 * size + x, 42 * size + y, 60 * size, 40 * size))
    ellipse(screen, (10, 33, 42), (235 * size + x, 42 * size + y, 60 * size, 40 * size))



def draw_background(color, N):
    """
    draw_background - рисует наборы из различных прямоугольников и эллипсов
    N - количество наборов, состоящих из двух прямоугольников и эллипса
    color - цвет в ординарных ковычках, example: 'black'
    """
    for i in range(N):
        SURFACE_background = pygame.Surface((S_w, S_h), pygame.SRCALPHA)
        x1 = random.randint(0, 1123)
        y1 = random.randint(0, 300)
        rect_width = random.randint(80, 200)
        rect_height = random.randint(200, 300)
        rect(SURFACE_background, (COLOR[color] + (50,)), (x1, y1, rect_width, rect_height))

        x2 = random.randint(0, 1123)
        y2 = random.randint(0, 300)
        rect_width = random.randint(80, 200)
        rect_height = random.randint(200, 300)
        rect(SURFACE_background, (COLOR[color] + (100,)), (x2, y2, rect_width, rect_height))

        x3 = random.randint(0, 1123)
        y3 = random.randint(0, 300)
        rect_width = random.randint(80, 200)
        rect_height = random.randint(200, 300)
        ellipse(SURFACE_background, (COLOR[color] +(150,)), (x3, y3, rect_width, rect_height))
        screen.blit(SURFACE_background, (0, 0))



def draw_road(color):
    """
    draw_road - рисует дорогу?)
    color - цвет в ординарных ковычках, example: 'black'
    """
    rect(screen, (color), (0, 461, 794, 762)) #Дорога



element = [0 for i in range(100)]
def draw_circles1_background(color):
    """
    draw_circle -- рисует красивые рассходящиеся эллипсы? не знаю честно как это назвать
    я думал добавть сюда еще и расположение по x, y, но их и так почти не видно, поэтому решил без этого
    color - цвет в ординарных ковычках, example: 'black'
    """
    for i in range(50):
        element[i] = pygame.Surface((S_w, S_h), pygame.SRCALPHA)
        element[i].fill((0))
        ellipse(element[i], (COLOR[color] +(6,)), (0 - 3 * i, -10 - 3 * i, 40 + 12 * i, 20 + 6 * i))
def draw_circles2_background(color):
    """
    draw_circle -- рисует красивые рассходящиеся эллипсы? не знаю честно как это назвать
    я думал добавть сюда еще и расположение по x, y, но их и так почти не видно, поэтому решил без этого
    color - цвет в ординарных ковычках, example: 'black'
    """
    for i in range(50):
        ellipse(element[i], (COLOR[color] +(10,)), (200 - 6 * i, 220 - 6 * i, 40 + 24 * i, 20 + 12 * i))
def draw_circles3_background(color):
    """
    draw_circle -- рисует красивые рассходящиеся эллипсы? не знаю честно как это назвать
    я думал добавть сюда еще и расположение по x, y, но их и так почти не видно, поэтому решил без этого
    color - цвет в ординарных ковычках, example: 'black'
    """
    for i in range(35):
        ellipse(element[i], (COLOR[color] +(8,)), (750 - 6 * i, 100 - 6 * i, 40 + 24 * i, 20 + 12 * i))
        screen.blit(element[i], (0, 0))
def draw_circles4_background(color):
    """
    draw_circle -- рисует красивые рассходящиеся эллипсы? не знаю честно как это назвать
    я думал добавть сюда еще и расположение по x, y, но их и так почти не видно, поэтому решил без этого
    color - цвет в ординарных ковычках, example: 'black'
    """
    for i in range(35):
        element[i] = pygame.Surface((S_w, S_h), pygame.SRCALPHA)
        element[i].fill((0))
        ellipse(element[i], (COLOR[color] +(8,)), (300 - 12 * i, 1000 - 12 * i, 40 + 48 * i, 20 + 24 * i))
        screen.blit(element[i], (0, 0))



def draw_house(x, y, color):
    """
    draw_house -- рисует домик с обводочкой
    x, y -- расположение дома
    color - цвет в ординарных ковычках, example: 'black'
    """
    house = pygame.Surface((S_w, S_h), pygame.SRCALPHA)
    rect(house, COLOR[color], (x, y, 444, 521)) #дом правый
    rect(house, (255, 255, 255), (x, y, 444, 521), 3) #Обводка правого дома
    screen.blit(house, (0, 0))



def draw_tower(x, y, a, b, color):
    """
    draw_tower -- рисует башенки? перед домами
    x, y -- расположение башенок
    a, b -- р
    азмеры башенки по x и по y
    color - цвет в ординарных ковычках, example: 'black'
    """
    rect(screen, COLOR[color], (x, y, a, b)) #башня 4



draw_circles1_background('cyan')
draw_circles2_background('blue')
draw_circles3_background('gold')
draw_circles4_background('green')

draw_background('black', 10)

draw_road('gray')

draw_house(400, 256, 'house')
draw_house(0, 206, 'house')

draw_tower(280, 249, 119, 450, 'tower1')
draw_tower(260, 410, 119, 430, 'tower2')
draw_tower(610, 302, 119, 470, 'tower3')

draw_car(50, 847, 0.3, 1, 'cyan')
draw_car(80, 907, 1, 0, 'red')
draw_car(300, 857, 0.3, 1, 'black')
draw_car(444, 847, 0.3, 1, 'blue')
draw_car(634, 877, 0.3, 1, 'gold')
draw_car(424, 1007, 1, 1, 'green')

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()