import js
p5 = js.window

angle = 0
x = 150
y = 150
circle_x = 150
circle_y = 150
circle_xspeed = 2
circle_yspeed = 1
circle_radius = 25

left_paddle_y = 150
right_paddle_y = 150


def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas 

def draw():
    global angle  # use global variable angle
    global x, y  # use global variables x and y
    
    p5.background(255)           # white background
    p5.fill(0)
    p5.text("p5.mouseIsPressed: " + str(p5.mouseIsPressed), 10, 20)
    p5.text("p5.mouseButton: " + str(p5.mouseButton), 10, 35)
    p5.text("p5.keyIsPressed: " + str(p5.keyIsPressed), 10, 50)
    p5.text("p5.key: " + str(p5.key), 10, 65)

    
    # keyboard conditions:
    if(p5.keyIsPressed == True):
        if(p5.key == 'g' or p5.key == 'G'):
            p5.fill(0, 255, 0)  # green
        elif(p5.key == 'b' or p5.key == 'B'):
            p5.fill(0, 0, 255)  # blue
        if(p5.keyCode == p5.UP_ARROW):
            y = y - 1  # decrement y by 1
        elif(p5.keyCode == p5.DOWN_ARROW):
            y = y + 1  # increment y by 1
        elif(p5.keyCode == p5.RIGHT_ARROW):
            x += 1  # increment x by 1
        elif(p5.keyCode == p5.LEFT_ARROW):
            x -= 1  # decrement x by 1
            
    # mouse conditions:
    elif(p5.mouseIsPressed == True):
        if(p5.mouseButton == p5.RIGHT):
            p5.fill(255, 0, 0)  # red
        else:
            p5.fill(0)  # white
    else:
        p5.fill(255)  # black
    
    p5.rectMode(p5.CENTER)
    p5.push()
    #p5.translate(150, 150)
    p5.translate(x, y)
    #angle = angle + 1  # increment variable by 1
    angle += 2  # another way to write angle = angle + 1
    p5.rotate(p5.radians(angle))
    p5.rect(0, 0, 100, 100)
    p5.pop()

    p5.fill(255)

    global circle_x, circle_xspeed
    global circle_y, circle_yspeed
    
    #if(circle_x < circle_radius):  # circle reached left side
    #    circle_speed = -circle_speed  # reverse the speed
    #elif(circle_x > p5.width - circle_radius):  # circle reached right side
    #    circle_speed = -circle_speed
    if(circle_x < circle_radius) or (circle_x > p5.width - circle_radius):
        circle_xspeed = -circle_xspeed
    if(circle_y < circle_radius) or (circle_y > p5.height - circle_radius):
        circle_yspeed = -circle_yspeed
    
    circle_x = circle_x + circle_xspeed
    circle_y = circle_y + circle_yspeed
    p5.ellipse(circle_x, circle_y, circle_radius*2, circle_radius*2)

    global left_paddle_y, right_paddle_y
    if(p5.keyIsPressed == True):
        if(p5.key == 'q'):
            if(left_paddle_y > 100/2):
                left_paddle_y -= 1
        elif(p5.key == 'a'):
            if(left_paddle_y < p5.height - 100/2):
                left_paddle_y += 1
        elif(p5.key == 'p'):
            if(right_paddle_y > 100/2):
                right_paddle_y -= 1
        elif(p5.key == 'l'):
            if(right_paddle_y < p5.height - 100/2):
                right_paddle_y += 1
    p5.fill(0)
    p5.rect(10, left_paddle_y, 20, 100)
    p5.rect(290, right_paddle_y, 20, 100)
