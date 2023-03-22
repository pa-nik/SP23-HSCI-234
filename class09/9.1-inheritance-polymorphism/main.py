import js
p5 = js.window

# object class template for a generic Sprite object:
class Sprite:  
    x = 0
    y = 0

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def draw(self):
        p5.rect(self.x, self.y, 50, 50)   

# object class template for a ChildSprite object that is a child of Sprite:
# (this is an example of using inheritance)
class SpriteChild(Sprite):  # parent class name is in parantheses
    # this object class will inherit all attributes and methods of Sprite
    # it can also "override" methods of its parent, such as draw:
    # (this is an example of polymorphism)
    def draw(self):
        p5.ellipse(self.x, self.y, 50, 50)

# create an instance of Sprite object and assign it to variable:
sprite1 = Sprite(x = 100, y = 150)  

# create an instance of SpriteChild object and assign it to variable:
sprite2 = SpriteChild(x = 200, y = 150)  

def setup():
    p5.createCanvas(300, 300)  
    p5.rectMode(p5.CENTER)
    
def draw():
    p5.background(255)   
    p5.fill(0)        
    sprite1.draw()
    p5.text('sprite1', sprite1.x - 20, sprite1.y - 30)
    sprite2.draw()
    p5.text('sprite2', sprite2.x - 20, sprite2.y - 30)

def keyPressed(event):
    pass

def keyReleased(event):
    pass

def mousePressed(event):
    pass

def mouseReleased(event):
    pass