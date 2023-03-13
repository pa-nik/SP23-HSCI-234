import js
p5 = js.window

# "encapsulation" means adding variables and functions 
# inside an object class as attributes and methods  
class Invader:
    def __init__(self, x = 150, y = 150):
        self.x = x  
        self.y = y
        self.timer = p5.millis()
        self.img1 = p5.loadImage('invader_1.png');  
        self.img2 = p5.loadImage('invader_2.png');   
    
    # "abstraction" means hiding implementation details  
    # inside methods, usually to simplify using an object
    def update(self):
        if(p5.millis() > self.timer + 500):
            if(self.y < p5.height - self.img1.height/2):
                self.y += 5
            else:
                self.y = self.img1.height/2
            self.timer = p5.millis()  # update timer

    def draw(self):
        p5.push()
        p5.translate(self.x, self.y)
        if(p5.millis() % 1000 < 500):
            p5.image(self.img1, 0, 0)
        else:
            p5.image(self.img2, 0, 0)
        p5.pop()

invader = Invader()  # instantiate Invader object

def setup():
    p5.createCanvas(300, 300)    
    p5.imageMode(p5.CENTER)

def draw():
    p5.background(0)
    # update and draw the Invader object:
    invader.update()
    invader.draw()

def keyPressed(event):
    pass

def keyReleased(event):
    pass

def mousePressed(event):
    pass

def mouseReleased(event):
    pass


    