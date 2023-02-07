import js
p5 = js.window

def setup():
    p5.createCanvas(300, 300)   
    p5.rectMode(p5.CENTER)  # set rectangle drawing mode to CENTER

def draw():
    p5.background(255)    
    p5.push()  # save coordinates (transformation matrix)       
    # draw rectangle at specified coordinates:
    p5.rect(50, 50, 50, 50)  # draw rectangle at (50, 50)
    # draw rectangle after moving the coordinates:
    p5.translate(100, 50)  # move by (100, 50)
    p5.rect(0, 0, 50, 50)  # draw rectangle at (0, 0)
    # draw rectangle after moving and rotating coordinates:
    p5.translate(50, 0)  # move by (50, 0)
    p5.rotate(p5.radians(30))  # rotate by 30 degrees
    p5.rect(0, 0, 50, 50)  # draw rectangle at (0, 0)
    # draw rectangle after moving already rotated coordinates: 
    p5.translate(50, 0)  # move by (50, 0)
    p5.rect(0, 0, 50, 50) # draw rectangle at (0, 0)
    # draw rectangle after rotating coordinates the other way then moving: 
    p5.rotate(p5.radians(-30))  # rotate by -30 degrees
    p5.translate(50, 0)  # move by (50, 0)
    p5.rect(0, 0, 50, 50)  # draw rectangle at (0, 0)
    p5.pop()   # restore coordinates
    p5.push()  # save coordinates
    p5.translate(50, 150)  # move by (50, 150)
    p5.rect(0, 0, 50, 50)  # draw rectangle at (0, 0)
    p5.pop()   # restore coordinates
    p5.push()  # save coordinates
    p5.translate(150, 150)  # move by (150, 150)
    p5.scale(1.5)  # scale by x1.5
    p5.rect(0, 0, 50, 50)  # draw rectangle at (0, 0)
    p5.pop()   # restore coordinates
    p5.push()  # save coordinates
    p5.translate(250, 150)  # move by (250, 150)
    p5.scale(0.75)  # scale by x0.75
    p5.rect(0, 0, 50, 50)  # draw rectangle at (0, 0)
    p5.pop()   # restore coordinates
    p5.push()  # save coordinates
    p5.translate(50, 250)  # move by (50, 250)
    for i in range(5):
        p5.push()  # save coordinates
        p5.translate(50*i, 0)  # move horizontally by 50*i
        p5.rotate(p5.radians(15*i))  # rotate by 15*i degrees
        p5.scale(1.0 - 0.1*i)  # scale down by 0.1*i
        p5.rect(0, 0, 50, 50)  # draw rectangle at (0, 0)
        p5.pop()   # restore coordinates
    p5.pop()   # restore coordinates