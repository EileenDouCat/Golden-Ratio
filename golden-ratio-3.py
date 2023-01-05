#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 11:50:02 2023

@author: linlin
"""
from math import *
from turtle import *
import time
import sys
import os


hideturtle()
penup()

setposition(-170, 350)

color('Red')
style = ('Courier', 40, 'bold')

write('The Golden Ratio',align='left',font=style)

color('Blue')
style = ('Courier', 30, 'bold')

setposition(-160, 300)
write('a/b= (a+b)/a = 1.618...',align='left',font=style)

color('Blue')
style = ('Courier', 20, 'bold')

setposition(-360, 250)
write('Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...',align='left',font=style)
color('Blue')
style = ('Courier', 30, 'bold')

setposition(-160, 210)
write('Fn+1/Fn -> 1.618...',align='left',font=style)

pendown()




time.sleep(10)

phi = (1+sqrt(5))/2 # The golden ratio. phi = 1.61803...

# function to draw a square with Turtle graphics
def square(side_length=100):
  for i in range(4):
    forward(side_length)
    right(90)

speed(6)  
showturtle()
penup()
goto(-190,-190) # start in lower left corner

setheading(90) # point up
pencolor("blue")
pendown()
size = 233 


# draw a series of squares in a spiral fashion
for i in range(8):
  square(size)
  forward(size)
  right(90)
  forward(size)
  size = size/phi



penup()
goto(-190,-190) # start in lower left corner
pendown()
pencolor("red")
radius = 233
for i in range(8):
  circle(-radius,90) # negative radius means draw clockwise
  radius = radius/phi
  ttt=position()


done()







