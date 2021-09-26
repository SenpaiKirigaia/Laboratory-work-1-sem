import turtle as t
from random import *
t.speed(20)
for _ in range (1000):
	a = randint(1,360)
	l = randint(1,50)
	t.left(a)
	t.forward(l)
