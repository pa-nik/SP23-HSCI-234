import js
p5 = js.window

print('click on canvas to move point to cursor coordinates')
print('press RIGHT ARROW key to move point to the right')

# class definition for the Point object:
class Point:  # class header followed by class body
    x = 0  # attribute x (variable x is "inside" object Point)
    y = 0  # another object attribute 

# create an instance of Point object and assign it to variable:
point_obj = Point()  
print(point_obj)
print('point_obj.x =', point_obj.x)
print('point_obj.y =', point_obj.x)

# function that takes an object as argument:
def print_point(p):
    print('p.x = ' + str(p.x) + ', p.y = ' + str(p.y))

# update object attribute values directly:
point_obj.x = 100
point_obj.y = 100
print('point_obj after updating its attributes directly:')
print_point(p = point_obj)

# function that takes an object and 2 more arguments:
def move_point(p, distance_x, distance_y):
  p.x += distance_x
  p.y += distance_y

# update object attributes using a function:
move_point(point_obj, 50, 50)
print('point_obj after updating its attributes with a function:')
print_point(point_obj)

# function to draw a Point object:
def draw_point(p):
    p5.fill(0)
    p5.push()
    p5.translate(p.x, p.y)
    p5.ellipse(0, 0, 5, 5)
    p5.text('(' + str(p.x) + ',' + str(p.y) + ')', 10, 10)
    p5.pop()

def setup():
    p5.createCanvas(300, 300)  
    
def draw():
    p5.background(255)           
    draw_point(point_obj)

def keyPressed(event):
    if(p5.keyCode == p5.RIGHT_ARROW):
        print('move point 10 pixels to the right..')
        move_point(point_obj, 10, 0)

def keyReleased(event):
    pass

def mousePressed(event):
    print('update point_obj x, y attributes with cursor coordinates..')
    point_obj.x = p5.mouseX
    point_obj.y = p5.mouseY

def mouseReleased(event):
    pass