# https://trinket.io/docs/python

from turtle import *
import numpy as np

import time

#screen_width = GetSystemMetrics(0)
#screen_height = GetSystemMetrics(1)

sw = 1920
sh = 1080
#import ctypes
#user32 = ctypes.windll.user32
#sw,sh = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

width  = sw*0.49
height = sh*0.75
startx = sw/2
starty = sh*0.1
background = "white"

turtle_color = "blue"

size_pen = 1

dot_size = 12

dotsPos = dict()
squaresPos = dict()

def pause(t):
    time.sleep(t)

def move_forward(d):
    time.sleep(1)
    forward(d)

def move_backward(d):
    time.sleep(1)
    backward(d)

def rotate(a):
    time.sleep(1)
    if a > 0:
        right(a)
    else:
        left(-a)

def rotate_left(a):
    time.sleep(1)
    left(a)

def rotate_right(a):
    time.sleep(1)
    right(a)
        
        
def get_invisible():        
    hideturtle()
    penup()

def get_visible():        
    showturtle()
    pendown()

def get_speed():
    return speed()

def set_speed(s):
    # from 0 to 10, increasingly faster
    speed(s)
    
def slower(f):
    tracer(1,f)

def faster(f):
    tracer(f)

def stop():
    {}

def get_heading():
    return heading()

def set_heading(angle):
    setheading(angle)

def get_position():
    return position()

def set_position(x,y):
    setpos(x,y)

def set_start_position(x,y):
    tracer(0)
    get_invisible()
    setpos(x,y)
    get_visible()
    tracer(1)

    
# place a square at the nearest integer coordinate, in order to not be too
# difficult to catch a dot, the (x,y) is the center of the square
def place_square(x,y, color, label=None, len=dot_size*1.5, store=True):
    current_x, current_y = position()
    drawings.tracer(0)
    drawings.hideturtle()
    drawings.penup()
    drawings.color(color)
    xx = round(x)
    yy = round(y)
    drawings.goto(xx - len/2 , yy - len/2)
    drawings.pendown()
    drawings.goto(xx - len/2, yy + len/2)
    drawings.goto(xx + len/2, yy + len/2)
    drawings.goto(xx + len/2, yy - len/2)
    drawings.goto(xx - len/2, yy - len/2)
    
    if store == True:
        if label != None:
            drawings.write(label, font=('Arial', 16, 'normal'), align='right')
            squaresPos[(xx, yy)] = label
        else:
            squarePos[(xx, yy)] = 255
    #goto(current_x, current_y)
    #get_visible()
    drawings.penup()
    drawings.tracer(1,1)

    
# place a "dot" at the nearest integer coordinate, in order to not be too
# difficult to catch a dot
def place_dot(x,y, color, label=None, _dot_size=dot_size, store=True):
    current_x, current_y = position()
    drawings.tracer(0)
    drawings.hideturtle()
    drawings.penup()
    drawings.goto(x,y)
    drawings.pendown()
    drawings.dot(_dot_size, color)
    if store == True:
        if label != None:
            drawings.write(label, font=('Arial', 16, 'normal'), align='center')
            dotsPos[(round(x), round(y))] = label
        else:
            dotsPos[(round(x), round(y))] = 255
    #goto(current_x, current_y)
    #get_visible()
    drawings.tracer(1,1)

def place_temporary_dot(x,y, color, label=None, _dot_size=dot_size, store=True):
    temp.tracer(0)
    temp.hideturtle()
    temp.penup()
    temp.goto(x,y)
    temp.dot(_dot_size, color)
    if store == True:
        if label != None:
            temp.write(label, font=('Arial', 16, 'normal'), align='center')
            dotsPos[(round(x), round(y))] = label
        else:
            dotsPos[(round(x), round(y))] = 255
    temp.tracer(1,1)

def is_dot(x,y):
    if (round(x), round(y)) in dotsPos:
        return True
    else:
        return False

def is_dot_by_id(x,y, id):
    if (round(x), round(y)) in dotsPos and dotsPos[(round(x), round(y))] == id:
        return True
    else:
        return False

def is_square(x,y):
    if (round(x), round(y)) in squaresPos:
        return True
    else:
        return False

def is_square_by_id(x,y, id):
    if (round(x), round(y)) in squaresPos and squaresPos[(round(x), round(y))] == id:
        return True
    else:
        return False

def is_dot_in_fov_by_id(id, x,y, heading, range=50):
    if heading < 0:
        heading = 360 + heading 

    show_fov(x,y,heading, range)
    circle_fov = (x + range * np.cos((np.pi / 180.) * (heading)), y + range * np.sin((np.pi / 180.) * (heading)))

    for pos in dotsPos:
        if ((circle_fov[0] - pos[0])*(circle_fov[0] - pos[0]) + (circle_fov[1] - pos[1])*(circle_fov[1] - pos[1])) < range*range:
            #print "Found dot ...", pos
            if dotsPos[pos] == id:
                print("Found dot by id: ", id)
                hide_fov(x,y,heading, range)
                return pos
    time.sleep(0.02)
    hide_fov(x,y,heading, range)
    return None, None


def is_square_in_fov_by_id(id, x,y, heading, range=50):
    if heading < 0:
        heading = 360 + heading 

    show_fov(x,y,heading, range)
    circle_fov = (x + range * np.cos((np.pi / 180.) * (heading)), y + range * np.sin((np.pi / 180.) * (heading)))

    for pos in squaresPos:
        if ((circle_fov[0] - pos[0])*(circle_fov[0] - pos[0]) + (circle_fov[1] - pos[1])*(circle_fov[1] - pos[1])) < range*range:
            #print "Found square ...", pos
            if squaresPos[pos] == id:
                time.sleep(0.5)
                hide_fov(x,y,heading, range)
                print("Found square by id: ", id)
                return pos
    time.sleep(0.5)
    hide_fov(x,y,heading, range)
    return None, None

    
def show_fov(x,y, heading, range=50):
    if heading < 0:
        heading = 360 + heading 
    circle_fov = (x + range * np.cos((np.pi / 180.) * (heading)), y + range * np.sin((np.pi / 180.) * (heading)))
    place_temporary_dot(circle_fov[0], circle_fov[1], 'lightgray', None, 2*range, False)

def hide_fov(x,y,heading, range=50):
    temp.reset()
    #if heading < 0:
    #    heading = 360 + heading 
    #circle_fov = (x + range * np.cos((np.pi / 180.) * (heading)), y + range * np.sin((np.pi / 180.) * (heading)))
    #place_dot(circle_fov[0], circle_fov[1], background, None, 2.05*range, False)
    
    
def are_dots_in_field_of_view(x,y, heading, range=50, angle=60):

    if heading < 0:
        heading = 360 + heading 

    circle_fov = (x + range * np.cos((np.pi / 180.) * (heading)), y + range * np.sin((np.pi / 180.) * (heading)))
    place_dot(circle_fov[0], circle_fov[1], 'lightgray', None, 2*range, False)
    print(circle_fov)

    dots_in_fov = []
    for pos in dotsPos:
        if ((circle_fov[0] - pos[0])*(circle_fov[0] - pos[0]) + (circle_fov[1] - pos[1])*(circle_fov[1] - pos[1])) < range*range:
            print("Ok! ", pos)
            dots_in_fov.append(pos)
        else:
            print("Not! in FOV", pos)
    
    return dots_in_fov

    
def are_squares_in_field_of_view(x,y, heading, range=50, angle=60):

    if heading < 0:
        heading = 360 + heading 

    circle_fov = (x + range * np.cos((np.pi / 180.) * (heading)), y + range * np.sin((np.pi / 180.) * (heading)))
    place_dot(circle_fov[0], circle_fov[1], 'lightgray', None, 2*range, False)
    #print circle_fov

    squares_in_fov = []
    for pos in squaresPos:
        if ((circle_fov[0] - pos[0])*(circle_fov[0] - pos[0]) + (circle_fov[1] - pos[1])*(circle_fov[1] - pos[1])) < range*range:
            print("Ok! ", pos)
            squares_in_fov.append(pos)
        else:
            print("Not! in FOV", pos)
    
    return squares_in_fov

    
def eat_dot(x,y):
    drawings.tracer(0)
    drawings.hideturtle()
    drawings.penup()
    drawings.goto(x,y)
    drawings.pendown()
    drawings.dot(dot_size+2, background)
    drawings.tracer(1,1)
    del dotsPos[(round(x), round(y))]

def pick_up_square(x,y):
    drawings.tracer(0)
    drawings.hideturtle()
    drawings.penup()
    drawings.color(background)
    xx = round(x)
    yy = round(y)
    len = dot_size*1.5
    drawings.goto(xx - len/2, yy - len/2)
    drawings.pendown()
    drawings.goto(xx - len/2, yy + len/2)
    drawings.goto(xx + len/2, yy + len/2)
    drawings.goto(xx + len/2, yy - len/2)
    drawings.goto(xx - len/2, yy - len/2)
    drawings.penup()
    drawings.tracer(1,1)
    del squaresPos[(xx, yy)]


def get_nearest_dot(x,y):
    min_d = width + height
    min_pos = (-1.0, -1.0)
    for pos in dotsPos:
        d = sqrt((x - pos[0])*(x - pos[0]) + (y - pos[1])*(y - pos[1]))
        if d < min_d:
            min_pos = pos
            min_d = d
    return min_pos


def get_nearest_square(x,y):
    min_d = width + height
    min_pos = (-1.0, -1.0)
    for pos in squaresPos:
        d = sqrt((x - pos[0])*(x - pos[0]) + (y - pos[1])*(y - pos[1]))
        if d < min_d:
            min_pos = pos
            min_d = d
    return min_pos

    
####################################
    
wn = Screen()
mc = Turtle()

drawings = Turtle()
temp = Turtle()

# window setup: color, size, position
bgcolor(background)       
setup(width, height, startx, starty)

setworldcoordinates(0,0, width, height)

#print("W: ", window_width(), "H: ", window_height())

color(turtle_color)              # make turtle blue
pensize(size_pen)                 # set the width of pen

shape('turtle')

title("MindCraft's Turtle")

set_start_position(width/2,height/2)
# TJ:	added this function as a wrapper for write; to 
#   	increase the default size of the font
def write_text(str):
	write(str, font=("Arial", 25, "normal"))

def is_square_in_fov(id):
	x,y = get_position()
	return is_square_in_fov_by_id(id, x, y, get_heading(), 150)
		
def teleport(x,y):
	hideturtle()
	penup()
	goto(x,y)
	pendown()
	showturtle()
	
def setup_squares():
    place_square(100, 100, 'red', 1)
    place_square(100, 300, 'red', 2)
    place_square(300, 100, 'red', 3)
    place_square(300, 300, 'red', 4)
    place_square(300, 380, 'red', 5)
    place_square(220, 320, 'red', 6)
  
#import mymaze
def clear_shell():
    print ("\n" * 100)

clear_shell()