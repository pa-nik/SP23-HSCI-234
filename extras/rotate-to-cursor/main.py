import js
p5 = js.window

# object class with x, y and angle attributes:
class Sprite:  
    x = 0
    y = 0
    angle = 0

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def draw(self):
        p5.push()
        p5.translate(self.x, self.y)
        p5.rotate(self.angle)
        p5.triangle(25, 0, -25, 25, -25, -25)   
        p5.pop()

sprite = Sprite(150, 150)

def setup():
    p5.createCanvas(300, 300)  
    
def draw():
    p5.background(255)   
    p5.fill(255)    
    p5.stroke(0)
    # calculate the angle between cursor and sprite using arc tangent:
    dx = p5.mouseX - sprite.x
    dy = p5.mouseY - sprite.y
    sprite.angle = p5.atan2(dy, dx) 
    sprite.draw()
    # draw line between mouse cursor and sprite:
    p5.stroke(150)
    p5.line(p5.mouseX, p5.mouseY, sprite.x, sprite.y)

def keyPressed(event):
    pass

def keyReleased(event):
    pass

def mousePressed(event):
    pass

def mouseReleased(event):
    pass