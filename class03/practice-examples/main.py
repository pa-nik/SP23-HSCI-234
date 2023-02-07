import js
p5 = js.window

random_size = p5.random(25, 50)  # assign a random value 25 - 50 to random_size

def setup():
    p5.createCanvas(300, 300)    

def draw():
    p5.background(255)           
    s = 50
    
    # example of translation:
    p5.push()  # save coordinates
    p5.translate(20, 30)  # move coordinates by (20, 30)
    p5.fill(255, 0, 0)
    p5.rect(0, 0, s, s)  # red square
    p5.pop() # go back to previously saved coordinates
    
    # coordinates are now back to origin (0, 0)
    p5.fill(0, 255 ,0)
    p5.rect(0, 0, s, s)  # green square

    # example of translation followed by another translation:
    p5.push() # save coordinates
    p5.translate(80, 30)  # move coordinates by (80, 30)
    p5.fill(0, 0, 255)
    p5.rect(0, 0, s, s)  # blue square
    p5.translate(50, 50)  # move coordinates by another (50, 50)
    p5.fill(0, 255, 255)
    p5.rect(0, 0, s, s)  # light blue square
    p5.pop() # go back to previously saved coordinates

    # example of rotation:
    p5.push()
    p5.translate(50,100)
    #p5.rotate(p5.PI/4)  # rotate by PI/4 radians (45 degrees)
    #p5.rotate(p5.radians(45))  # rotate by converting 45 degrees to radians
    # we can also set the angle mode:
    p5.angleMode(p5.DEGREES)  # change angle mode to use degrees
    p5.rotate(45)
    p5.fill(0)
    p5.rect(0, 0, s, s)  # black square
    p5.angleMode(p5.RADIANS)  # change angle mode to use radians
    p5.pop()

    # example of rotation followed by translation:
    p5.push()
    p5.rotate(p5.radians(-45))  # rotate coordinates by -45 degrees
    p5.translate(50,100)  # translate after rotation
    p5.fill(255)
    p5.rect(0, 0, s ,s)  # white square
    p5.pop()

    # example of scaling:
    p5.push()
    p5.translate(200, 100)  
    p5.scale(1.5)  # scale canvas by x2
    p5.fill(255, 0, 255)
    p5.rect(0, 0, 50, 50)  # purple square
    p5.pop()

    # example of using p5.mouseX and p5.mouseY built-in variables:
    p5.push()
    p5.rectMode(p5.CENTER)  # change rectangle mode to center
    p5.translate(p5.mouseX, p5.mouseY)
    p5.noFill()
    p5.rect(0, 0, 50, 50)  # empty square
    p5.rectMode(p5.CORNER)  # change rectangle mode to corner
    p5.pop()

    # example of using random function:
    s = p5.random(50)
    p5.fill(255, 120, 120)
    p5.rect(20, 200, s, s)  # pink rectangle that keeps changing size
    p5.fill(150)
    p5.rect(80, 200, random_size, random_size)  # gray rectangle 

    draw_yellow_square()  # call function to make it run
    draw_orange_square(x = 225, y = 200)  # call another function

# function definition to draw yellow square with no parameters:
def draw_yellow_square():
    p5.push()
    p5.translate(150, 200)
    p5.fill(255, 255, 0)
    p5.rect(0, 0, 50, 50)  # yellow square
    p5.pop()

# function definition to draw orange square with x and y parameters:
def draw_orange_square(x, y):
    p5.push()
    p5.translate(x, y)
    p5.fill(255, 170, 0)
    p5.rect(0, 0, 50, 50)  # yellow square
    p5.pop()