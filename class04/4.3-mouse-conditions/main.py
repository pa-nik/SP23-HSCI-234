import js
p5 = js.window

def setup():
    p5.createCanvas(300, 300)   
    p5.rectMode(p5.CENTER)  # set rectangle drawing mode to CENTER

def draw():
    p5.background(255)    
    p5.fill(0)
    p5.text('p5.mouseIsPressed: ' + str(p5.mouseIsPressed), 10, 20)
    p5.text('p5.mouseButton: ' + str(p5.mouseButton), 10, 35)
    p5.fill(255)  # white
    # p5.mouseIsPressed is True when mouse is pressed, False otherwise:
    if (p5.mouseIsPressed == True):
        # p5.mouseButton is equal to p5.LEFT with 'left' (or one-figer) click:
        if (p5.mouseButton == p5.LEFT):
            p5.fill(0)  # black
        # p5.mouseButton is equal to p5.RIGHT with 'right' (or two-finger) click:
        elif (p5.mouseButton == p5.RIGHT):
            p5.fill(255, 0, 0)  # red
    p5.ellipse(p5.width/2, p5.height/2, 100, 100)
    # NOTE: p5.mouseIsPressed seems to get stuck after 'right' click,
    # until the next 'left' click