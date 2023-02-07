import js
p5 = js.window

def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas 

def draw():
    p5.background(255)           # white background
    # draw flower at specified coordinates:
    draw_flower(x = 100, y = 100)
    # draw another flower at smaller scale:
    p5.push()
    p5.translate(220, 220)  # move coordinates
    p5.scale(0.75)  # then scale
    draw_flower(x = 0, y = 0)  # draw at origin (0, 0)
    p5.pop()

# function with no parameters:
def draw_petal():
    p5.ellipse(50, 0, 75, 25)

# function with 2 parameters:
def draw_flower(x, y):
    p5.push()
    p5.translate(x, y)
    for i in range(20):
        p5.noStroke()
        p5.fill(i*25, 255-i*25, 0, 200)
        p5.rotate(p5.radians(360/20))
        draw_petal()
    p5.pop()
