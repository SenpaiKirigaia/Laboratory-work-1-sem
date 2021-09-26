import turtle as t
import math
t.speed(20)
l=50
a=90
a1=45
def zero(num):
	t.penup()
	t.goto(num*(l+10), 0)
	t.setheading(0)
	t.pendown()
	t.forward(l)
	t.right(a)
	t.forward(2*l)
	t.right(a)
	t.forward(l)
	t.right(a)
	t.forward(2*l)

def one(num):
	t.penup()
	t.goto(num*(l+10), -l)
	t.setheading(0)
	t.pendown()
	t.left(a1)
	t.forward(math.sqrt(2)*l)
	t.setheading(-a)
	t.forward(2*l)

def two(num):
	t.penup()
	t.goto(num*(l+10), 0)
	t.setheading(0)
	t.pendown()
	t.forward(l)
	t.right(a)
	t.forward(l)
	t.right(a)
	t.forward(math.sqrt(2)*l)
	t.setheading(0)
	t.forward(l)

def three(num):
	t.penup()
	t.goto(num*(l+10), 0)
	t.setheading(0)
	t.pendown()
	t.forward(l)
	t.right(a+a1)
	t.forward(math.sqrt(2)*l)
	t.setheading(0)
	t.forward(l)
	t.right(a+a1)
	t.forward(math.sqrt(2)*l)

def four(num):
	t.penup()
	t.goto(num*(l+10), 0)
	t.setheading(0)
	t.pendown()
	t.right(a)
	t.forward(l)
	t.left(a)
	t.forward(l)
	t.right(a)
	t.forward(l)
	t.right(180)
	t.forward(2*l)

def five(num):
	t.penup()
	t.goto(num*(l+10), 0)
	t.setheading(0)
	t.pendown()
	t.forward(l)
	t.right(180)
	t.forward(l)
	t.left(a)
	t.forward(l)
	t.left(a)
	t.forward(l)
	t.right(a)
	t.forward(l)
	t.right(a)
	t.forward(l)

def six(num):
	t.penup()
	t.goto(num*(l+10), -l)
	t.setheading(0)
	t.pendown()
	t.left(a1)
	t.forward(math.sqrt(2)*l)
	t.right(180)
	t.forward(math.sqrt(2)*l)
	t.setheadng(-a)
	t.forward(l)
	t.left(a)
	t.forward(l)
	t.left(a)
	t.forward(l)
	t.left(a)
	t.forward(l)

def seven(num):
	t.penup()
	t.goto(num*(l+10), 0)
	t.setheading(0)
	t.pendown()
	t.forward(l)
	t.setheading(-135)
	t.forward(math.sqrt(2)*l)
	t.setheading(-a)
	t.forward(l)

def eight(num):
	t.penup()
	t.goto(num*(l+10), 0)
	t.setheading(0)
	t.pendown()
	t.forward(l)
	t.right(a)
	t.forward(2*l)
	t.right(a)
	t.forward(l)
	t.right(a)
	t.forward(2*l)
	t.right(180)
	t.forward(l)
	t.left(a)
	t.forward(l)

def nine(num):
	t.penup()
	t.goto(num*(l+10), 0)
	t.setheading(0)
	t.pendown()
	t.forward(l)
	t.right(a)
	t.forward(l)
	t.right(a)
	t.forward(l)
	t.right(a)
	t.forward(l)
	t.right(a)
	t.forward(l)
	t.right(a1)
	t.forward(math.sqrt(2)*l)

ind = [one, four, one, seven, zero, zero]

for i, num in enumerate(ind):
	num(i)
	
	











