import js
p5 = js.window

print('click on canvas to move point to cursor coordinates')
print('press RIGHT ARROW key to move point to the right')

# class definition for the Point object:
class Point:  # class header followed by class body
    x = 0  # attribute x (variable x is "inside" object Point)
    y = 0  # another object attribute 

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
point_obj = Point()  
Point.print_point(point_obj)  # call method using the function syntax
point_obj.print_point()  # call method using the method syntax
point_obj.move_point(150, 150)  # call method with 2 arguments

def setup():
    p5.createCanvas(300, 300)  
    
def draw():
    p5.background(255)           
    point_obj.draw()  # call the draw method of Point on point_obj

def keyPressed(event):
    if(p5.keyCode == p5.RIGHT_ARROW):
        print('move point 10 pixels to the right..')
        point_obj.move_point(10, 0)  

def keyReleased(event):
    pass

def mousePressed(event):
    print('update point_obj x, y attributes with cursor coordinates..')
    point_obj.set_point(p5.mouseX, p5.mouseY)

def mouseReleased(event):
    pass