import js
p5 = js.window

circle_x = 150
circle_y = 150
circle_r = 50  # radius of the circle
speed = 1  # speed of circle

rect_x = 125
rect_y = 125
rect_w = 50
rect_h = 50

def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas 

def draw():
    p5.background(255)           # white background
    p5.stroke(0)

    global circle_x
    circle_x += speed  # update circle position
    
    # wrap moving circle around the edge of canvas:
    if(circle_x > p5.width + circle_r):
        circle_x = -circle_r

    # calculate distance from center of circle to cursor:
    d = dist(x1 = circle_x, y1 = circle_y, x2 = p5.mouseX, y2 = p5.mouseY)
    #d = dist(circle_x, circle_y, p5.mouseX, p5.mouseY)
    # use the built-in p5.dist function instead:
    #d = p5.dist(circle_x, circle_y, p5.mouseX, p5.mouseY)

    # check if cursor is inside circle:
    #if(d < circle_r):  #  distance to cursor is less than radius
    # use the result of a function as a condition:
    if(is_inside_circle(x = p5.mouseX, y = p5.mouseY) == True):
        p5.fill(200)  # gray
    else:
        p5.fill(255)  # white
    p5.ellipse(circle_x, circle_y, circle_r*2, circle_r*2)

    # check if cursor is inside square:
    if(p5.mouseX > rect_x) and (p5.mouseX < rect_x + rect_w) \
    and (p5.mouseY > rect_y) and (p5.mouseY < rect_y + rect_h):
        p5.fill(150)
    else:
        p5.fill(255)
    p5.rect(rect_x, rect_y, rect_w, rect_h)

    p5.noStroke()
    p5.fill(0)
    p5.text("hours_to_minutes(1) = " + str(hours_to_minutes(1)), 10, 20)
    #p5.text("hours_to_minutes(2) = " + str(hours_to_minutes(2)), 10, 35)
    p5.text("is_divisible(2, 2) = " + str(is_divisible(2, 2)), 10, 35)
    p5.text("is_divisible(3, 2) = " + str(is_divisible(3, 2)), 10, 50)
    p5.text("is_inside_circle(p5.mouseX, p5.mouseY) = " + 
        str(is_inside_circle(p5.mouseX, p5.mouseY)), 10, 65)
    p5.text("is_inside_rect(p5.mouseX, p5.mouseY) = " + 
        str(is_inside_rect(p5.mouseX, p5.mouseY)), 10, 80)

    # draw line between center of circle and cursor, show distance:
    p5.fill(255, 0, 0)
    p5.text("dist: " + str(int(d)), p5.mouseX + 10, p5.mouseY + 10)
    p5.stroke(255, 0, 0)
    p5.line(circle_x, circle_y, p5.mouseX, p5.mouseY)

# function that takes hours as input, returns minutes as output:
def hours_to_minutes(hours):
    minutes = hours * 60
    return minutes

# function that returns True if x is divisible by y, False otherwise
def is_divisible(x, y):
    if(x % y == 0):  # x % y is remainder of x divided by y 
        return True
    else:
        return False
        
# function that returns distance between points (x1, y1) and (x2, y2)
def dist(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    distance = p5.sqrt(dx*dx + dy*dy)
    return distance

# function returns True if (x, y) are inside circle, False otherwise: 
def is_inside_circle(x, y):
    d = p5.dist(x, y, circle_x, circle_y)  
    if(d < circle_r):
        return True
    else:
        return False

# function returns True if (x, y) are inside rectangle, False otherwise: 
def is_inside_rect(x, y):
    # using backslash (\) character to break up a long line of code:
    if(p5.mouseX > rect_x) and (p5.mouseX < rect_x + rect_w) \
    and (p5.mouseY > rect_y) and (p5.mouseY < rect_y + rect_h):
        return True
    else:
        return False

