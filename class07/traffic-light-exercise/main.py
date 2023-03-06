import js
p5 = js.window

class TrafficLight:
    state = 'green'
    timer = 0
    
    def update(self):
        # check if time is greater than timer + 2 seconds:
        if(p5.millis() > self.timer + 2000):  
            # print('update light..')
            if(self.state == 'green'):
                self.state = 'yellow'
            elif(self.state == 'yellow'):
                self.state = 'red'
            elif(self.state == 'red'):
                self.state = 'green'
            self.timer = p5.millis()  # update the timer attribute

    def draw(self):
        p5.push()
        p5.translate(p5.width/2, p5.height/2)
        if(self.state == 'red'):
            p5.fill(255, 0, 0)  # bright red
        else:
            p5.fill(150, 0, 0)  # dim red
        p5.ellipse(0, -p5.height/4, 60, 60)
        if(self.state == 'yellow'):
            p5.fill(255, 255, 0)  # bright yellow
        else:
            p5.fill(150, 150, 0)  # dim yellow
        p5.ellipse(0, 0, 60, 60)
        if(self.state == 'green'):
            p5.fill(0, 255, 0)  # bright green
        else:
            p5.fill(0, 150, 0)  # dim green
        p5.ellipse(0, p5.height/4, 60, 60)
        p5.pop()

# instantiate the TrafficLight object and assign it to variable:
traffic_light = TrafficLight()

def setup():
    p5.createCanvas(300, 300)
	    
def draw():
    p5.background(0)
    # update and draw the traffic_light object:
    traffic_light.update()
    traffic_light.draw()  

def keyPressed(event):
    pass 

def keyReleased(event):
    pass

def mousePressed(event):
    pass

def mouseReleased(event):
    pass