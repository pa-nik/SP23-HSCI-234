import js
p5 = js.window

# object template for Point object:
class Point:  # header
    #pass  # do nothing
    x = 0  # x is an attribute of Point object
    y = 0  # another attribute of Point object

    # method that will automatically run when object is instantiated:
    def __init__(self, x_init = 0, y_init = 0):
        self.x = x_init
        self.y = y_init

    # method to print coordinates of a Point:
    def print_point(self):
        print('print_point method inside Point class..')
        print('x = ' + str(self.x) + ', y = ' + str(self.y))  

    def set_point(self, new_x, new_y):
        print('set_point method inside Point class')
        self.x = new_x
        self.y = new_y
        
    # method to draw the Point object:
    def draw_point(self):
        p5.push()
        p5.translate(self.x, self.y)
        p5.fill(0)
        p5.ellipse(0, 0, 5, 5)
        p5.text('(' + str(self.x) + ', ' + str(self.y) + ')', 10, 10)
        p5.pop()


    
# function to print attributes of Point object:
def print_point(p):
    print('print_point function..')
    print('x = ' + str(p.x) + ', y = ' + str(p.y))  

# create an instance of Point object and assign it to variable point
point_obj = Point() 
print(point_obj)
#print('x =', point_obj.x)
print('x = ' + str(point_obj.x) + ', y = ' + str(point_obj.y))
point_obj.x = 100  # change attribute x of point_obj to 100
point_obj.y = 100
print('x = ' + str(point_obj.x) + ', y = ' + str(point_obj.y))
print_point(p = point_obj)
Point.print_point(point_obj)  # function syntax to run print_point method
point_obj.print_point()  # method syntax to run print_point method

point2 = Point(x_init = 150, y_init = 150)  # instantiate a Point with two arguments
point2.print_point()

point3 = Point(x_init = 200)  # instantiate a Point with one argument
point3.print_point()
    
def setup():
    p5.createCanvas(300, 300)  
    print('finished setup..')

def draw():
    p5.background(255)           
    p5.text(str(p5.mouseX) + ", " + str(p5.mouseY), 10, 15)
    point_obj.draw_point()  # call the draw_point method of point_obj
    point2.draw_point()


def keyPressed(event):
    pass

def keyReleased(event):
    pass

def mousePressed(event):
    print('mousePressed..')
    point_obj.set_point(new_x = p5.mouseX, new_y = p5.mouseY)

def mouseReleased(event):
    pass
