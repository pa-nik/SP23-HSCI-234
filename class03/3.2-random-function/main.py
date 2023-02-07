import js
p5 = js.window

# variables assigned to random values once at the beginning of the program:
circle_gray = p5.random(255)  # random value between 0 - 255
circle_size = p5.random(150, 250)  # random value between 150 - 250 

def setup():
    p5.createCanvas(300, 300)   
    p5.rectMode(p5.CENTER)  # set rectangle drawing mode to CENTER

def draw():
    p5.background(255)    
    # circle in random gray color and size that doesn't change:
    p5.fill(circle_gray)
    p5.ellipse(150, 150, circle_size, circle_size)
    # variables assigned to random values every draw cycle:
    square_gray = p5.random(255)  # random value between 0 - 255
    square_size = p5.random(50, 100)  # random value between 50 - 100
    # square in random gray color and size that keeps changing:
    p5.fill(square_gray)
    p5.rect(150, 150, square_size, square_size)