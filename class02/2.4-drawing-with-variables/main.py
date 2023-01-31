import js
p5 = js.window

def setup():
    p5.createCanvas(300, 300)    

def draw():
    p5.background(255)  # white background
    p5.fill(255)  # white fill
    y = 60 # variable for vertical position
    d = 75 # variable for circle diameter
    # draw 3 circles:
    p5.ellipse(60, y, d, d) 
    p5.ellipse(150, y, d, d) 
    p5.ellipse(240, y, d, d) 
    # draw same circles with a loop:
    for i in range(3):
        x = 60 + i*90
        y = 150
        p5.fill(50 + i*50)
        p5.ellipse(x, y, d, d) 
    # another way to loop using start, stop and step:
    for x in range(60, 250, 90):
        p5.ellipse(x, 240, d, d) 