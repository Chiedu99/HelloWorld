#Chiedu Nduka-eze
#Friday, September 16
import math
import turtle

print("This program will calculate the acute angle of two different and connected coordinates starting from the origin.")
#this allows the user to input his coordinates
x1 = int(input("insert the first x coordinate:"))
y1=int(input("insert first y coordinate:"))

x2 = int(input("insert the second x coordinate:"))
y2 = int(input("insert the second y coordinate:"))

#these are the slopes of the two lines that are created
m1 = (y1 / x1)
m2 = (y2 - y1) / (x2 - x1)

print(m1)
print(m2)

#This makes the turtle draw the lines the user inputs
turtle.goto(x1 , y1)
turtle.goto(x2 , y2)

#This the the trigonometry that we use to calcluate the created angle in radians
tangent = (abs(m2 - m1)) / (1 + m1 * m2)
print(tangent)
math.atan(tangent)

#This changes the radians we calculated to degrees
angleInDegrees = (tangent) * 180 / math.pi

print(angleInDegrees)
turtle.write(angleInDegrees)
turtle.done()

