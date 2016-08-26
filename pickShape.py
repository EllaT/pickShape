from turtle import *
from random import randint
shapes = int(input("How many shapes?"))
for i in range(shapes):
	length_of_side = int(input("How many sides?"))
	size =  int(input("How many forward steps?"))
	color = (input("What color?"))
	number = (randint (20, 90))
	for i in range(length_of_side):
		pencolor(color)
		pendown()
		forward(size)
		if length_of_side <= 2:
			print("no no")
			#	Hmmm = False
		else:
			print("ok")
			angle = 360/length_of_side
			right (angle)
	#count += 1
	right (randint(20, 360))
	penup()
	forward(number)
getscreen()._root.mainloop()
