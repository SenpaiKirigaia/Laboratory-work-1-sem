import pygame
import json
from pygame.draw import *
from random import randint

pygame.init()

FPS = 15
screen = pygame.display.set_mode((1200, 900))

BORDER_EDGES = [1000, 800]
N = 10
L = 0
end = 0
count = 0
f = pygame.font.Font(None,36) 

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

Name = ""

end_text = f.render('Выход', True, (178, 103, 49))
name_text = f.render('Напишите ваше имя', True, CYAN)

class Ball:
    def __init__(self, coord, velocity, color, r, randmove):
        """
        Задает все начальные значения для шарика
        coord - координаты [x, y]
        velocity - скорость [v_x, v_y]
        color - цвет шарика
        r - радиус шарика
        randmove - дополнение к движению (ускорение,
        направленное к какой либо из стенок
        (зависящее от начальных скоростей шарика))
        """
        self.coord = coord
        self.color = color
        self.velocity = velocity
        self.r = r
        self.flag = True 
        self.randmove = randmove
        if self.randmove == 1:
            if vx_dir == 1 and vy_dir == 1:
                acc_x = -1
                acc_y = 0
            if vx_dir == 1 and vy_dir == -1:
                acc_x = 0
                acc_y = 1
            if vx_dir == -1 and vy_dir == 1:
                acc_x = 0
                acc_y = -1
            if vx_dir == -1 and vy_dir == -1:
                acc_x = 1
                acc_y = 0
        else:
            acc_x = 0
            acc_y = 0
        self.acc_x = acc_x
        self.acc_y = acc_y

    def move(self):
        """
        функция движения шарика, которая в том числе и рисует его
        два типа движения, которые отличаются наличием randmove:
        -обычное:
            прямолинейное движение, просто по начальным V_x и V_y
        -необычное:
            движение под силой гравитации (наличие притяжения у одной из стенок)
        """
        circle(screen, self.color, self.coord, self.r)
        v0_x, v0_y = self.velocity
        self.coord[0] += v0_x
        self.coord[1] += v0_y
        self.velocity[0] += self.acc_x
        self.velocity[1] += self.acc_y
        

    def collisions(self):
        """
        функция сдерживающая шарики в "клетке"
        работает 2-мя способами:
        -При касании стенки скорость меняется на противоположную
        с тем же модулем
        -При выходе шарика "далеко" за рамки, просто телепортирует шарик в клетку
        """
        if self.coord[0] <= 40 or self.coord[0] >= BORDER_EDGES[0]:
            self.velocity[0] *= -1
        if self.coord[1] <= 40 or self.coord[1] >= BORDER_EDGES[1]:
            self.velocity[1] *= -1
        if self.coord[0] <= 30:
            self.coord[0] = 50
        if self.coord[1] <= 30:
            self.coord[1] = 50
        if self.coord[0] >= (BORDER_EDGES[0] + 10):
            self.coord[0] = (BORDER_EDGES[0] - 10)
        if self.coord[1] >= (BORDER_EDGES[1] + 10):
            self.coord[1] = (BORDER_EDGES[1] - 10)


    def event(self):
        """
        функция, срабатывающая при клике мышки, проверяет попадание по шарику
        при попадании помечает шарик, впоследствии он уничтожается
        """
        if (X_m - self.coord[0])**2 + (Y_m - self.coord[1])**2 <= (self.r)**2:
            self.flag = False

pool = []

for _ in range (N):
    x = randint(100,950)
    y = randint(100, 750)
    vx_dir = randint(-1, 1)
    while vx_dir == 0:
        vx_dir = randint(-1, 1)
    vy_dir = randint(-1, 1)
    while vy_dir == 0:
        vy_dir = randint(-1, 1)
    V_x = randint(4, 10)*vx_dir
    V_y = randint(4, 10)*vy_dir
    r = randint(25, 40)
    randmove = 0
    color = 'BLUE'
    pool.append(Ball([x, y], [V_x, V_y], color, r, randmove))

for _ in range (N):
    x = randint(50,950)
    y = randint(50, 750)
    vx_dir = randint(-1, 1)
    while vx_dir == 0:
        vx_dir = randint(-1, 1)
    vy_dir = randint(-1, 1)
    while vy_dir == 0:
        vy_dir = randint(-1, 1)
    V_x = randint(4, 10)*vx_dir
    V_y = randint(4, 10)*vy_dir
    r = randint(10, 20)
    randmove = 1
    color = 'RED'
    pool.append(Ball([x, y], [V_x, V_y], color, r, randmove))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            X_m, Y_m = event.pos
            for ball in pool:
                ball.event()
            if end >= 15:
                if 450 < X_m <600 and 300 < Y_m < 350:
                    pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if end >= 10 and end < 15 and event.key != 8 and event.key != 13:
                Name = Name + event.unicode
            if end >= 10 and end < 15 and event.key == 8:
                Name = Name[:-1]
            if end >= 10 and end < 15 and event.key == 13:
                with open('Results.JSON', 'r') as h:
                    loaded = json.load(h)
                loaded["results"].append({"name": Name, "points": count})
                with open('Results.JSON', 'w') as h:
                    json.dump(loaded, h)
                h.close()
                end += 10

                
    for ball in pool:
        ball.move()
        ball.collisions()
        if ball.flag == False:
            if ball.color == 'BLUE':
                count += 5
            if ball.color == 'RED':
                count += 15
            if ball.color == 'RED' and ball.r <= 15:
                count += 10
            pool.remove(ball)
            end += 1

    text = f.render('Счет: ' + str(count), True, (255, 255, 255))
    if end < 10:
        screen.blit(text, (10, 10))

    if end >= 10 and end <= 15:
        for ball in pool:
            pool.remove(ball)
        screen.blit(text, (450, 100))
        screen.blit(name_text, (400, 200))
        name_name_text = f.render(Name, True, CYAN)
        screen.blit(name_name_text, (450, 300))
        
    if end >= 15:
        with open('Results.JSON', 'r') as h:
            loaded = json.load(h)
        h.close()
        res = loaded["results"]
        table = []
        names = []
        for i in res:
            table.append(i["points"])
            names.append(i["name"])
        A = len(table)
        for i in range(A-1):
            for j in range(A-i-1):
                if table[j] > table[j+1]:
                    table[j], table[j+1] = table[j+1], table[j]
                    names[j], names[j+1] = names[j+1], names[j]

        z = len(table) - 1
        while z >= 0:
            for i in res:
                i["points"] = table[z]
                i["name"] = names[z]
                z += -1

        leaderboard = f.render('Leaderboard', True, RED)
        screen.blit(text, (450, 100))
        screen.blit(name_name_text, (400, 200))
        screen.blit(end_text, (450, 300))
        screen.blit(leaderboard, (350, 325))
        c = 0
        for i in res:
            man = f.render(i["name"] + " " + str(i["points"]), True, GREEN)
            screen.blit(man, (350, 350 + c*25))
            c += 1


    pygame.display.update()
    screen.fill(BLACK)





pygame.quit()
