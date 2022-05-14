import turtle as t

t.Screen().bgcolor('black')
t.pensize(2)
t.speed(10)

for i in range(10):
	for color in ("red","orange","blue","purple","green","white","yellow"):
		t.color(color)
		t.circle(100)
		t.left(100)
	t.hideturtle()
t.done()