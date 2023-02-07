import js
p5 = js.window

def setup():
    p5.createCanvas(300, 300)   

def draw():
    p5.background(255)    
    p5.noStroke()
    p5.fill(0)
    # useful built-in variables in p5:
    p5.text("p5.width = " + str(p5.width), 10, 20)
    p5.text("p5.height = " + str(p5.height), 10, 40)
    p5.text("p5.mouseX = " + str(p5.mouseX), 10, 60)
    p5.text("p5.mouseY = " + str(p5.mouseY), 10, 80)
    p5.stroke(0)
    p5.noFill()
    x = p5.width / 2  # assign x to center of canvas horizontally 
    y = p5.height / 2  # assign y to center of canvas vertically
    w = p5.mouseX  # horizontal cursor position
    h = p5.mouseY  # vertical cursor position
    p5.ellipse(x, y, w, h)