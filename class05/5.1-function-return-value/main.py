import js
p5 = js.window

circle_x = 150
circle_y = 150
circle_r = 50

def setup():
    p5.createCanvas(300, 300)   
    p5.rectMode(p5.CENTER)  # set rectangle drawing mode to CENTER

def draw():
    p5.background(255)    
    p5.fill(0)

    a = 2
    b = 2
    c = get_sum(a, b)  # c is the output or result of get_sum function
    p5.text("get_sum(2, 2) = " + str(c), 10, 20)

    c = do_sum(a, b)  # c is None because do_sum has no output 
    p5.text("do_sum(2, 2) = " + str(c), 10, 35)

    # the distance between center of circle and mouse cursor:
    d = get_distance(circle_x, circle_y, p5.mouseX, p5.mouseY)
    # same function as get_distance exists in p5:
    # d = p5.dist(circle_x, circle_y, p5.mouseX, p5.mouseY)

    p5.stroke(0)
    if(d < circle_r):
        p5.fill(200)
    else:
        p5.fill(255)
    p5.ellipse(circle_x, circle_y, circle_r * 2, circle_r * 2)

    # draw the line between center of circle and mouse cursor:
    p5.stroke(255, 0, 0)
    p5.line(circle_x, circle_y, p5.mouseX, p5.mouseY)

    p5.noStroke()
    p5.fill(255, 0, 0)
    p5.text(int(d), p5.mouseX + 5, p5.mouseY - 5)

    p5.fill(0)
    p5.text("cursor_inside_circle() = " + str(cursor_inside_circle()), 10, 50)
    
# function that returns the sum of a + b:
def get_sum(a, b):
    sum = a + b
    return sum  # the output of this function is sum

# function that computes a + b, but has no return statement:
def do_sum(a, b):
    sum = a + b
    # the output of this function is the keyword None

# function that returns distance between points (x1, y1) and (x2, y2)
def get_distance(x1, y1, x2, y2):
    d = p5.sqrt((x1-x2)**2 + (y1-y2)**2)
    return d 

# function that returns True if cursor is inside circle, False otherwise:
def cursor_inside_circle():
    d = get_distance(p5.mouseX, p5.mouseY, circle_x, circle_y)
    if(d < circle_r):
        return True
    else:
        return False