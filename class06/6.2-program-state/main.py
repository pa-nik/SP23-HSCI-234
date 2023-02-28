import js
p5 = js.window

circle_x = 150
circle_speed = 1.5
circle_radius = 50
program_state = 'START'  # variable to keep track of program state

def setup():
    p5.createCanvas(300, 300)  
    print('program_state = ' + program_state)
    print('click to start moving the circle..')

def draw():
    p5.background(255)        
    p5.text('program_state = ' + program_state, 10, 20)   
    global circle_x, circle_speed
    # move circle during PLAY state:
    if(program_state == 'PLAY'):
        circle_x += circle_speed  # update circle position
    if (circle_x > p5.width - circle_radius) \
    or (circle_x < circle_radius):
        circle_speed *= -1  # change direction
    p5.ellipse(circle_x, 150, circle_radius * 2, circle_radius * 2)

def mousePressed(event):
    global program_state
    # change program state from current to next state:
    if(program_state == 'START'):
        program_state = 'PLAY'
    elif(program_state == 'PAUSE'):
        program_state = 'PLAY'
    elif(program_state == 'PLAY'):
        program_state = 'PAUSE'
    print('change program_state to ' + program_state)

def keyPressed(event):
    pass

def keyReleased(event):
    pass

def mouseReleased(event):
    pass













