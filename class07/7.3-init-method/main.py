import js
p5 = js.window

# class definition for the Point object:
class Point:  
    # this method is automatically called when object is instantated:
    def __init__(self, x = 0, y = 0):
        self.x = x  # initialize attribute x 
        self.y = y  # initialize attribute y 

    # print Point method (function "inside" object Point):
    def print_point(self):
        print('x = ' + str(self.x) + ', y = ' + str(self.y))

    # method to move the coordinates of a Point object:
    def move_point(self, distance_x, distance_y):
        self.x += distance_x
        self.y += distance_y

    # method to set the coordinates of a Point object:
    def set_point(self, x, y):
        self.x = x
        self.y = y

    # method to draw a Point object:
    def draw(self):
        p5.fill(0)
        p5.push()
        p5.translate(self.x, self.y)
        p5.ellipse(0, 0, 5, 5)
        p5.text('(' + str(self.x) + ',' + str(self.y) + ')', 10, 10)
        p5.pop()

# create an instance of Point object and assign it to variable:
point_1 = Point()  # instantiate an object with no arguments
point_1.print_point()

# create an instance of another Point object:
point_2 = Point(x = 100, y = 100)  # instantiate with x, y arguments
point_2.print_point()

point_3 = Point(200, 200)  # instantiate with x, y arguments
point_3.print_point()

def setup():
    p5.createCanvas(300, 300)  
    
def draw():
    p5.background(255)           
    point_1.draw()  
    point_2.draw() 
    point_3.draw() 

def keyPressed(event):
    pass 

def keyReleased(event):
    pass

def mousePressed(event):
    pass

def mouseReleased(event):
    pass