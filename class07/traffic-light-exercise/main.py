import js
p5 = js.window

class TrafficLight:
    def __init__(self):
        self.state = 'green'
        self.timer = 0
    
    def update(self):
        if(self.state == 'green'):
            self.state = 'yellow'
        elif(self.state == 'yellow'):
            self.state = 'red'
        elif(self.state == 'red'):
            self.state = 'green'
        
    def draw(self):
        p5.push()
        p5.translate(p5.width/2, p5.height/2)
        if(self.state == 'red'):
            p5.fill(255, 0, 0)
        else:
            p5.fill(150, 0, 0)
        p5.ellipse(0, -p5.height/4, 60, 60)
        p5.pop()

def setup():
    p5.createCanvas(300, 300)
	    
def draw():
    p5.background(0)

def keyPressed(event):
    pass 

def keyReleased(event):
    pass

def mousePressed(event):
    pass

def mouseReleased(event):
    pass