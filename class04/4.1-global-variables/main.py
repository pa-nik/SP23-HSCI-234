import js
p5 = js.window

# global variables are created outside of any functions:
angle = 0.0  # variable to keep track of angle

def setup():
    p5.createCanvas(300, 300)   
    p5.rectMode(p5.CENTER)  # set rectangle drawing mode to CENTER

def draw():
    p5.background(255)    

    global angle  # use global keyword to re-use the existing variable
    # NOTE: without the global keyword a new local variable is created

    p5.push()
    p5.translate(p5.width/2, p5.height/2)  # translate to middle
    p5.rotate(angle)  # rotate by angle
    p5.rect(0, 0, 100, 100)
    angle = angle + 0.05  # increment angle
    p5.pop()
