import math
from random import choice
from random import randint
import pygame
import json

pygame.init()
pygame.font.init()

f1 = pygame.font.Font(None, 24)
f2 = pygame.font.Font(None, 48)

FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, GREEN, MAGENTA, CYAN]
GOLD = (255, 215, 0)

WIDTH = 1000
HEIGHT = 800


class Ball:
    def __init__(self, screen_1: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen_1
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 1

    def move(self):
        self.y += self.vy
        self.x += self.vx
        if self.x + self.vx >= WIDTH - 50:
            self.vx *= -1
        if self.x + self.vx <= 50:
            self.vx *= -1
        if self.y <= -self.r:
            self.live = 0

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (int(self.x), int(self.y)),
            self.r)

    def hittest(self, obj):
        """
        Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """

        x2, y2 = obj.x, obj.y
        if (self.x - x2) ** 2 + (self.y - y2) ** 2 <= (self.r + obj.r) ** 2:
            self.color = (255, 0, 0)
            self.r = 30
            self.live = 0
            return True
        return False


class Target:
    def __init__(self, screen_2):
        self.x = randint(100, WIDTH - 100)
        self.y = randint(100, HEIGHT - 300)
        self.vx = randint(-5, 5)
        self.vy = randint(-5, 5)
        self.live = 1
        self.r = randint(30, 50)
        self.color = choice(GAME_COLORS)
        self.gun = 1000
        self.screen = screen_2
        self.object = randint(0, 1)

    def move(self):
        """
        описывает движение стреляющей мишени
        """
        global gunballs
        self.x += self.vx
        self.y += self.vy
        self.gun -= 5
        if self.x + self.vx >= WIDTH - 50:
            self.vx *= -1
        if self.x + self.vx <= 50:
            self.vx *= -1
        if self.y + self.vy >= HEIGHT - 50:
            self.vy *= -1
        if self.y + self.vy <= 50:
            self.vy *= -1
        if self.live == 0:
            self.x = self.y = -100
            self.vx = self.vy = 0
        if self.gun % 100 == 0:
            gg = Ball(self.screen)
            gg.x = self.x
            gg.y = self.y
            gg.color = (0, 200, 0)
            gg.vx = randint(-4, 4)
            gg.vy = randint(5, 10)
            gunballs.append(gg)

    def test(self, obj):
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= (self.r + obj.r) ** 2:
            self.live = 0
            return True
        return False

    def draw(self):
        if self.object:
            pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)
        else:
            x = self.x
            y = self.y
            r = self.r
            a = [(x - r, y - r), (x + r, y - r), (x + r, y + r), (x - r, y + r)]
            pygame.draw.polygon(self.screen, self.color, a)


class Tank:
    def __init__(self, screen_3):
        self.an = None
        self.x = WIDTH / 2
        self.y = HEIGHT - 20
        self.r = 10
        self.vx = 4
        self.live = 1
        self.color = (200, 0, 200)
        self.screen = screen_3

    def move_right(self):
        if self.x <= 750:
            self.x += self.vx

    def move_left(self):
        if self.x >= 50:
            self.x -= self.vx

    def alive(self):
        if self.live == 0:
            self.x = self.y = -100
            return True
        return False

    def draw(self):

        x = self.x
        y = self.y
        g = [(x - 20, y + 10), (x + 20, y + 10), (x + 20, y), (x - 20, y)]
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)
        pygame.draw.polygon(self.screen, self.color, g)

    def test(self, obj):
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= (self.r * 3 + obj.r) ** 2:
            self.live = 0
            return True
        return False

    def gungun(self, event_1):
        """Выстрел мячом. прицеливание

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        gun = Ball(self.screen)
        self.an = math.atan2((event_1.pos[1] - self.y), (event_1.pos[0] - self.x))
        gun.vx = int(20 * math.cos(self.an))
        gun.vy = int(20 * math.sin(self.an))
        gun.x = self.x
        gun.y = self.y
        balls.append(gun)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
gunballs = []
Name = ''
clock = pygame.time.Clock()
target = Target(screen)
tank = Tank(screen)
moving = 0
finished = False

count = 0
end = 0

while not finished:

    while end == 0:
        screen.fill(WHITE)
        greeting_text = f2.render('Приветствую любителей шаров', True, CYAN)
        greeting_text_rect = greeting_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        screen.blit(greeting_text, (greeting_text_rect[0], greeting_text_rect[1] - f2.size('Приветствую любителей '
                                                                                           'шаров')[1]))

        starting_text = f1.render('Начать', True, (180, 0, 0))
        starting_text_rect = starting_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        screen.blit(starting_text, (starting_text_rect[0], starting_text_rect[1]))

        exit_text = f1.render('Выйти', True, (180, 0, 0))
        exit_text_rect = exit_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        screen.blit(exit_text, (exit_text_rect[0], exit_text_rect[1] + f1.size('Выйти')[1]))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                X_m, Y_m = event.pos
                if (starting_text_rect[0] <= X_m <= starting_text_rect[0] + starting_text_rect[2] and
                        starting_text_rect[1] <= Y_m <= starting_text_rect[1] + starting_text_rect[3]):
                    end += 1
                if (exit_text_rect[0] <= X_m <= exit_text_rect[0] + exit_text_rect[2] and
                        exit_text_rect[1] + f1.size('Выйти')[1] <= Y_m <= exit_text_rect[1] + f1.size('Выйти')[1]
                        + exit_text_rect[3]):
                    pygame.quit()

        pygame.display.update()

    while end == 1:
        screen.fill(WHITE)

        greeting_text = f2.render('Приветствую любителей шаров', True, CYAN)
        greeting_text_rect = greeting_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        screen.blit(greeting_text, (greeting_text_rect[0], greeting_text_rect[1] - 2 * f2.size('Приветствую любителей '
                                                                                               'шаров')[1]))
        name_input = f1.render('Пожалуйста введите ваше имя', True, (180, 0, 0))
        name_input_rect = name_input.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        screen.blit(name_input, (name_input_rect[0], name_input_rect[1]))

        name_text = f1.render(Name, True, GREY)
        name_text_rect = name_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        screen.blit(name_text, (name_text_rect[0], name_text_rect[1] + f1.size(Name)[1]))

        exit_text = f1.render('Выйти', True, (180, 0, 0))
        exit_text_rect = exit_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        screen.blit(exit_text, (exit_text_rect[0], exit_text_rect[1] + 2 * f1.size('Выйти')[1]))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                X_m, Y_m = event.pos
                if (exit_text_rect[0] <= X_m <= exit_text_rect[0] + exit_text_rect[2] and
                        exit_text_rect[1] + 2 * f1.size('Выйти')[1] <= Y_m <= exit_text_rect[1] + 2 * f1.size('Выйти')[
                            1]
                        + exit_text_rect[3]):
                    pygame.quit()

            elif event.type == pygame.KEYDOWN:
                if end == 1 and event.key != 8 and event.key != 13:
                    Name = Name + event.unicode

                if end == 1 and event.key == 8:
                    Name = Name[:-1]

                if end == 1 and event.key == 13:
                    end += 1
        pygame.display.update()

    while end == 2:
        screen.fill(WHITE)
        target.draw()
        tank.draw()
        for gunball in gunballs:
            if gunball.live >= 1:
                gunball.draw()
        for ball in balls:
            if ball.live >= 1:
                ball.draw()

        exit_text = f1.render('Выйти', True, (180, 0, 0))
        screen.blit(exit_text, (WIDTH - f1.size('Выйти')[0] - 20, HEIGHT - f1.size('Выйти')[1] - 20))

        bullets_counter = f1.render('Количество пуль: ' + str(bullet), True, (180, 0, 0))
        points_counter = f1.render('Количество очков: ' + str(count), True, (180, 0, 0))
        points_counter_size = f1.size('Колисество очков: ' + str(count))
        screen.blit(bullets_counter, (10, 50))
        screen.blit(points_counter, (WIDTH - points_counter_size[0] - 20, 50))

        pygame.display.update()

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                X_m, Y_m = event.pos
                if (WIDTH - f1.size('Выйти')[0] - 20 <= X_m <= WIDTH - 20 and
                        HEIGHT - f1.size('Выйти')[1] - 20 <= Y_m <= HEIGHT - 20):
                    pygame.quit()
                if len(balls) < 6:
                    tank.gungun(event)

        if tank.alive():
            end += 1

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            tank.move_left()
        if keys[pygame.K_RIGHT]:
            tank.move_right()

        for gunball in gunballs:
            gunball.move()
            for ball in balls:
                gunball.hittest(ball)
                ball.hittest(gunball)
                if target.test(ball):
                    target = Target(screen)
                    count += 1
                tank.test(gunball)

        for ball in balls:
            ball.move()
            if ball.live == 0:
                balls.remove(ball)
        target.move()

    while end == 3:
        while end == 3:
            with open('Results.JSON', 'r') as h:
                loaded = json.load(h)
            loaded["results"].append({"name": Name, "points": count})
            with open('Results.JSON', 'w') as h:
                json.dump(loaded, h)
            h.close()
            end += 1
    while end == 4:
        screen.fill(WHITE)
        game_over_text = f2.render('GAME OVER. YOU ARE LOSER. HA-HA-HA', True, BLACK)
        game_over_rect = game_over_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        screen.blit(game_over_text,
                    (game_over_rect[0], game_over_rect[1] - f2.size('GAME OVER. YOU ARE LOSER. HA-HA-HA')[1]))

        exit_text = f1.render('Выйти', True, (180, 0, 0))
        exit_text_rect = exit_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        screen.blit(exit_text, (exit_text_rect[0], exit_text_rect[1]))

        leaderboard = f2.render('Leaderboard', True, RED)
        leaderboard_rect = leaderboard.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        screen.blit(leaderboard, (leaderboard_rect[0], leaderboard_rect[1] + leaderboard_rect[3]))

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
        for i in range(A - 1):
            for j in range(A - i - 1):
                if table[j] > table[j + 1]:
                    table[j], table[j + 1] = table[j + 1], table[j]
                    names[j], names[j + 1] = names[j + 1], names[j]

        z = len(table) - 1
        while z >= 0:
            for i in res:
                i["points"] = table[z]
                i["name"] = names[z]
                z += -1

        c = 0
        for i in res:
            man = f1.render(i["name"] + " " + str(i["points"]), True, GREEN)
            man_rect = man.get_rect(center=(WIDTH / 2, HEIGHT / 2))
            screen.blit(man, (man_rect[0], man_rect[1] + (c + 3) * 25))
            c += 1
            if c == 9:
                break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                X_m, Y_m = event.pos
                if (exit_text_rect[0] <= X_m <= exit_text_rect[0] + exit_text_rect[2] and
                        exit_text_rect[1] <= Y_m <= exit_text_rect[1] + exit_text_rect[3]):
                    pygame.quit()

        pygame.display.update()
        clock.tick(FPS)

pygame.quit()
