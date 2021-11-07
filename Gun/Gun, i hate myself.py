import math
from random import choice
from random import randint

import pygame
pygame.init()
pygame.font.init()

f1 = pygame.font.Font(None, 24)

FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
#YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, GREEN, MAGENTA, CYAN]
GOLD = (255, 215, 0)

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 1
        self.time = 0

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.x += self.vx
        self.y -= self.vy
        self.vy -= 5
        if self.x >= (800 - self.r) or self.x <= self.r :
            self.vx *= -1
            self.x += 2*self.vx
        if self.y >= (600 - self.r) or self.y <= self.r :
            self.vy *= -0.8

        self.time += 1
            

    def draw(self):
        pygame.draw.circle( self.screen, self.color, (int(self.x), int(self.y)), self.r)

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME
        x2, y2 = obj.x, obj.y
        if (self.x-x2)**2+(self.y-y2)**2<=(self.r+obj.r)**2:
            return True
        return False



class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY


    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global pool, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        pool.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        cos = math.cos(self.an)
        sin = math.sin(self.an)
        x0, y0 = 10,500
        d = self.f2_power
        l = 20
        x1, y1 = x0 + d*cos, y0+d*sin
        x2, y2 = x0+l*cos, y0-l*sin
        x3, y3 = x1+l*cos, y1-l*sin
        pygame.draw.polygon(self.screen, self.color, [(x0,y0), (x1,y1), (x3,y3), (x2,y2)])
        
    
    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self, screen, difficulty):
        self.screen = screen
        self.points = 0
        self.live = 1
        self.new_target(difficulty)
        self.difficulty = difficulty

    def new_target(self, difficulty):
        """ Инициализация новой цели. """
        self.x = randint(600, 740)
        self.y = randint(300, 520)
        self.difficulty = difficulty
        if self.difficulty == 0:
            r = self.r = randint(20, 50)
            self.vx = randint(-1, 1)
            while self.vx == 0:
                self.vx = randint(-1, 1)
        if self.difficulty == 1:
            r = self.r = randint(10, 20)
            self.vx = randint(-3, 3)
            while self.vx == 0:
                self.vx = randint(-3, 3)
        if self.difficulty == 2:
            r = self.r = randint(5, 10)
            self.vx = randint(-5, 5)
            while self.vx == 0:
                self.vx = randint(-5, 5)
        else:
            r = self.r = randint(20,50)
        
        color = self.color = RED
        
        self.vy = randint(-3, 3)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)
        pygame.draw.circle(self.screen, BLACK, (self.x, self.y), self.r, 1)

    def move(self):
        x, y, vx, vy = self.x, self.y, self.vx, self.vy
        r = self.r
        x += vx
        y += vy
        if x+r+vx > 801:
            vx *= -1
        if x-r+vx < 0:
            vx*=-1
        if y+r+vy > 601:
            vy*=-1
        if y-r+vy < 0:
            vy*=-1
        self.x, self.y, self.vx, self.vy = x, y, vx, vy


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
pool = []

clock = pygame.time.Clock()
gun = Gun(screen)
target = Target(screen, 0)
target2 = Target(screen, 1)
target3 = Target(screen, 2)
finished = False
count = 0


while not finished:
    screen.fill(WHITE)
    gun.draw()
    target.draw()
    target2.draw()
    target3.draw()
    for ball in pool:
        if ball.live >= 1:
            ball.draw()
    text1 = f1.render('Количество пуль: '+str(bullet), True, (180,0,0))
    text2 = f1.render('Количество очков: '+str(count), True, (180,0,0))
    screen.blit(text1, (10, 50))
    screen.blit(text2, (500, 50))
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for ball in pool:
        ball.move()
        if ball.hittest(target) and target.live:
            target.live = 1
            target.hit()
            pool.remove(ball)
            target.new_target(0)
            count += 5
        if ball.hittest(target2) and target2.live:
            target2.live = 1
            target2.hit()
            pool.remove(ball)
            target2.new_target(1)
            count += 10
        if ball.hittest(target3) and target3.live:
            target3.live = 1
            target3.hit()
            pool.remove(ball)
            target3.new_target(2)
            count += 20
    target.move()
    target2.move()
    target3.move()
    
    for ball in pool:
        if ball.time >= 45:
            pool.remove(ball)

    gun.power_up()

pygame.quit()