import turtle

turtle.up()
turtle.goto(-500,300)
turtle.down()
y = 0
for x in range(100):
	turtle.forward(20)
	turtle.right(90)
	turtle.forward(30+y)
	turtle.left(90)
	turtle.forward(40+y)
	turtle.right(90)
	turtle.forward(50+y)
	y = y+2
	turtle.forward(20)
	turtle.right(90)
	turtle.forward(30+y)
	turtle.left(90)
	turtle.forward(40+y)
	y = y+2
	turtle.forward(20)
	turtle.right(90)
	turtle.forward(30+y)
	turtle.left(90)
	turtle.forward(40+y)
	turtle.right(90)
	turtle.forward(50+y)
	y = y+2
	turtle.forward(20)
	turtle.right(90)
	turtle.forward(30+y)
	turtle.left(90)
	turtle.forward(40+y)
	y = y+2
	turtle.goto(-250+y,250+y)
	y = y+10
turtle.mainloop()