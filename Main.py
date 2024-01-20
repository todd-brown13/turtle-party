# Joy Of Coding - Beginning Python Challenge
# Author:   Todd Brown
# Date:     1/8/24
#
# print ("Hello, World!")
#
name = "Todd"
print( "Hello,"+ name + "!")
#
import turtle
turtle.color( "Red")

def triangle (size):
  for i in range(3):
    turtle.forward( size)
    turtle.left( 120)
  
def square (size):
  for i in range(4):
    turtle.forward( size)
    turtle.left( 90)
  
def move_back(size):
  turtle.penup()
  turtle.backward(size)
  turtle.pendown()
  
def move_left(size):
  turtle.penup()
  turtle.left(size)
  turtle.pendown()
  
# Def to print a polygon.  Size and # of sides are inputs.
def polygon(num_sides, size):
  for i in range(num_sides):
    turtle.forward( size)
    turtle.left( 360/num_sides)
  
# Def to go forward
def move_fwd( length):
  move_back(-1 * length)
  
# Code to draw 3 triangles of decreasing size.

# size = 100
# triangle (size)
# move_back (75)
# size = 50
# triangle (size)
# move_back (50)
# size = 25
# triangle (size)

# Code to draw 3 squares of decreasing size.
# size = 100
# square (size)
# move_back (75)
# size = 50
# square (size)
# move_back (50)
# size = 25
# square (size)

# Code to draw multiple polygons passing in the number of sides as well as
# the length of each side.
#
# num_sides = 8
# size = 25
# polygon(8, 25)
# move_back(100)
# num_sides = 4
# size = 25
# polygon(4, 30)

# Code to draw multiple polygons in a circle.
#
# poly_st_sides = 4   # Number of sides for first polygon to be drawn.
# poly_end_sides = 6 # Number of sides for last polygon to be drawn.
# if poly_st_sides < 3:
#   print "Error - A Polygon cannot have less than 3 sides."
#   exit()
#
#   size = 80
# for loop in range( poly_st_sides, poly_end_sides +1): # 
#   polygon( loop, size/loop)
#   move_fwd(360/(poly_end_sides-poly_st_sides+1))
#   move_left(360/(poly_end_sides-poly_st_sides+1))

# Code to draw a spiral.

# size = 10
# angle = 45
# for loop in range (1,20):
#   turtle.forward(size)
#   turtle.left(angle)
#   turtle.forward(size)
#   turtle.left(angle)
#   turtle.forward(size)
#   turtle.left(angle)
#   size = size + 5
