import js
p5 = js.window

rect_x = 150
rect_y = 150

def setup():
    p5.createCanvas(300, 300)   
    p5.rectMode(p5.CENTER)  # set rectangle drawing mode to CENTER

def draw():
    p5.background(255)    
    p5.fill(0)
    p5.text('p5.keyIsPressed: ' + str(p5.keyIsPressed), 10, 20)
    p5.text('p5.key: ' + str(p5.key), 10, 35)
    p5.text('p5.keyCode: ' + str(p5.keyCode), 10, 50)
    p5.fill(255)

    # p5.keyIsPressed is True when any key is pressed, False otherwise:
    if (p5.keyIsPressed):
        # p5.key is equal to the typed character string:
        if (p5.key == 'r') or (p5.key == 'R'):  
            p5.fill(255, 0, 0)  # red
        elif (p5.key == 'g') or (p5.key == 'G'):
            p5.fill(0, 255, 0)  # green
        elif (p5.key == 'b') or (p5.key == 'B'):
            p5.fill(0, 0, 255)  # blue
    else: 
        p5.fill(255)  # white
    
    global rect_x, rect_y
    
    if (p5.keyIsPressed == True): # key has been pressed
        # p5.keyCode is equal to special keys like arrows:
        if (p5.keyCode == p5.LEFT_ARROW):  # left arrow
            rect_x = rect_x - 1
        elif (p5.keyCode == p5.RIGHT_ARROW):  # right arrow
            rect_x = rect_x + 1
        elif (p5.keyCode == p5.UP_ARROW):  # up arrow
            rect_y = rect_y - 1
        elif (p5.keyCode == p5.DOWN_ARROW):  # down arrow
            rect_y = rect_y + 1

    p5.rect(rect_x, rect_y, 100, 100) 
