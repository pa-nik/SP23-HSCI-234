import js
p5 = js.window

circle_x = 75
circle_y = 150
circle_r = 50

rect_x = 175
rect_y = 125
rect_w = 100
rect_h = 50

def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas 

def draw():
    p5.background(255)           # white background
    
    p5.noStroke()
    draw_circle_button()
    draw_rect_button()

    p5.fill(0)
    p5.text("cursor_inside_circle() = " + str(cursor_inside_circle()), 10, 20)
    p5.text("cursor_inside_rect() = " + str(cursor_inside_rect()), 10, 35)
    p5.text("circle_is_pressed() = " + str(circle_is_pressed()), 10, 50)
    p5.text("rect_is_pressed() = " + str(rect_is_pressed()), 10, 65)
    

def draw_circle_button():
    if(cursor_inside_circle() == True):  # cursor is inside circle
        if(p5.mouseIsPressed == True):  # mouse/trackpad is pressed
            p5.fill(100)  # dark gray
        else:
            p5.fill(150)  # medium gray
    else:
        p5.fill(200)  # light gray
    p5.ellipse(circle_x, circle_y, circle_r * 2, circle_r * 2)
    p5.fill(255)
    p5.text("BUTTON 1", circle_x - 30, circle_y + 5)

def draw_rect_button():
    if(cursor_inside_rect() == True):  # cursor is inside rect
        if(p5.mouseIsPressed == True):  # mouse/trackpad is pressed
            p5.fill(100)  # dark gray
        else:
            p5.fill(150)  # medium gray
    else:
        p5.fill(200)  # light gray
    p5.rect(rect_x, rect_y, rect_w, rect_h)
    p5.fill(255)
    p5.text("BUTTON 2", rect_x + 20, rect_y + 30)

# function returns True if cursor is inside circle, False otherwise: 
def cursor_inside_circle():
    d = p5.dist(p5.mouseX, p5.mouseY, circle_x, circle_y)
    if(d < circle_r):
        return True
    else:
        return False
    
# function returns True if cursor is inside rectangle, False otherwise: 
def cursor_inside_rect():
    # there are 4 conditions combined with logical operator and 
    # using backslash (\) character to break up a long line of code:
    if(p5.mouseX > rect_x) and (p5.mouseX < rect_x + rect_w) \
    and (p5.mouseY > rect_y) and (p5.mouseY < rect_y + rect_h):
        return True
    else:
        return False

# function returns True if circle button is pressed, False otherwise:
def circle_is_pressed():
    return (cursor_inside_circle() and p5.mouseIsPressed)

# function returns True if rect button is pressed, False otherwise:
def rect_is_pressed():
    return (cursor_inside_rect() and p5.mouseIsPressed)
