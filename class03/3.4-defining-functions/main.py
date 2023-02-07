import js
p5 = js.window

def setup():
    p5.createCanvas(300, 300)   
    p5.rectMode(p5.CENTER)  # set rectangle drawing mode to CENTER

def draw():
    p5.background(255)    
    # skull on the left stays in place at specified coordinates:
    p5.push()  # save coordinates  
    p5.translate(80, 100)  # move coordinates by (80, 100)
    draw_skull()  # call function to draw the left skull
    draw_nose(size = 1.0)  # call function to draw nose with size = 1.0
    draw_teeth(number = 6)  # call function to draw 6 teeth
    draw_eye(x = -25, y = -25, radius = 20)  # draw left eye
    draw_eye(x = 25, y = -25, radius = 20)   # draw right eye
    draw_spine(x = 0, y = 55)
    p5.pop()   # restore coordinates
    # skull on the right moves up and down with cursor:
    p5.push()  # save coordinates
    p5.translate(220, p5.mouseY)  # move cordinates by 220 and mouseY
    draw_skull()  # call function to draw the right skull
    draw_nose(1.5)  # call function to draw nose with size = 1.5
    draw_teeth(7)  # call function to draw 7 teech
    # eyes change size with cursor movement left and right:
    draw_eye(-25, -25, 15 + p5.mouseX/20)  # left eye 
    draw_eye(25, -25, 15 + p5.mouseX/20)   # right eye 
    draw_spine(0, 55)
    p5.pop()   # restore coordinates

# function with no parameters:
def draw_skull():
    p5.arc(0, -20, 100, 100, p5.radians(130), p5.radians(50))
    p5.line(-32, 18, -32, 50)
    p5.line(32, 18, 32, 50)
    p5.line(-32, 50, 32, 50)

# function with one parameter:
def draw_nose(size):
    p5.push()  # save coordinates
    p5.scale(size)  # scale coordinates by size
    p5.fill(0)  
    p5.triangle(-5, 5, 5, 5, 0, -10)  # black triangle
    p5.pop()  # restore coordinates

# function with one parameter:
def draw_teeth(number):
    p5.push()  # save coordinates
    p5.translate((1-number)*6/2, 30)  # move coordinates to center teeth
    p5.fill(255)
    for i in range(0, number):  # draw number of teeth in a loop 
        p5.rect(0 + i*6, -4, 6, 8)
        p5.rect(0 + i*6, 4, 6, 8)
    p5.pop()  # restore coordinates

# function with two parameters:
def draw_spine(x, y):
    p5.fill(255)
    for i in range(25):  # draw 25 segments in a loop starting at x, y
        p5.rect(x, y + i*10, 15, 10)
        
# function with three parameters:
def draw_eye(x, y, radius):
    p5.fill(255)
    p5.ellipse(x, y, radius, radius)  # eye outline at x, y and radius
    p5.fill(0)
    p5.ellipse(x, y, radius/4, radius/4)  # eye pupil at x, y and radius/4






