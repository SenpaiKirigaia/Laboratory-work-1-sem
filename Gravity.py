import turtle as t

eps = 0 
g = 9.81 
vx = 15 
vy = 30 
dt = 0.1 #сек
x, y = -300, 0


t.goto (300, 0)
t.goto (-300, 0)
while (x < 300):
    x += vx * dt
    vy -= g * dt
    y += vy * dt
    t.goto (x, y)
    if (y <= 0):
        vy = - 0.9 * vy
        if (abs (vy) < 0):
            break
