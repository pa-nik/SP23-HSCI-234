import js
p5 = js.window

def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas 

def draw():
    p5.background(255)           # white background
    # line function takes 4 arguments (x1, y1, x2, y2):
    p5.line(10, 10, 110, 100)
    # triangle function takes 6 arguments (x1, y1, x2, y2, x3, y3):
    p5.triangle(80, 20, 150, 40, 110, 80)
    # quad function takes 8 arguments (x1, y1, x2, y2, x3, y3, x4, y4):
    p5.quad(170, 20, 280, 20, 260, 100, 160, 90)
    # ellipse function takes 4 arguments (x, y, width, height):
    p5.ellipse(70, 150, 80, 80)
    # rect function takes 4 arguments (x, y, width, height):
    p5.rect(150, 130, 120, 40)
    # arc function takes 6 arguments (x, y, width, height, start, stop)
    # the start and stop angles are expressed in radians by default
    # we can use built-in p5 variables such as PI and TWO_PI:
    p5.arc(50, 240, 70, 70, p5.PI, p5.TWO_PI) 
    # there are also QUARTER_PI and p5.HALF_PI:
    p5.arc(140, 240, 70, 70, p5.QUARTER_PI, -p5.HALF_PI)
    # or we can convert angles to degrees using the radians function:
    p5.arc(230, 240, 70, 70, p5.radians(0), p5.radians(180))