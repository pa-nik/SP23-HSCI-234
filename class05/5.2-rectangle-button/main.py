import js
p5 = js.window

rect_x = 100
rect_y = 125
rect_w = 100
rect_h = 50

def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas 

def draw():
    p5.background(255)           # white background
    p5.noStroke()

    if(cursor_inside_rect() == True):  # cursor is inside rect
        if(p5.mouseIsPressed == True):  # mouse/trackpad is pressed
            p5.fill(100)  # dark gray
        else:
            p5.fill(150)  # medium gray
    else:
        p5.fill(200)  # light gray
    p5.rect(rect_x, rect_y, rect_w, rect_h)

    p5.noStroke()
    p5.fill(0)
    p5.text("cursor_inside_rect() = " + 
        str(cursor_inside_rect()), 10, 20)
    p5.text("p5.mouseIsPressed = " + 
        str(p5.mouseIsPressed), 10, 35)

    p5.fill(255)
    p5.text("CLICK ME!", 120, 155)

# function returns True if cursor is inside rectangle, False otherwise: 
def cursor_inside_rect():
    # there are 4 conditions combined with logical operator and 
    # using backslash (\) character to break up a long line of code:
    if(p5.mouseX > rect_x) and (p5.mouseX < rect_x + rect_w) \
    and (p5.mouseY > rect_y) and (p5.mouseY < rect_y + rect_h):
        return True
    else:
        return False

