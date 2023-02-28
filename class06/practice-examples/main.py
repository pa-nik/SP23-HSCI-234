import js
p5 = js.window

state = 'ice'

def heat():
    global state
    print('heating..')
    if(state == 'ice'):
        state = 'liquid'
    elif(state == 'liquid'):
        state = 'steam'

def cool():
    global state
    print('cooling..')
    if(state == 'steam'):
        state = 'liquid'
    elif(state == 'liquid'):
        state = 'ice'
heat()
heat()
print(state)
cool()
print(state)
cool()
print(state)

ball_x = 150
ball_y = 150
ball_radius = 15
ball_xspeed = p5.random(1, 1.5)
ball_yspeed = p5.random(-1, 1)

program_state = 'START'
program_timer = p5.millis()
print("program_timer = " + str(program_timer))

def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas 
    p5.rectMode(p5.CENTER)  # draw rectangles from center

def draw():
    p5.background(0)           # black background

    global program_timer, program_state, ball_xspeed, ball_yspeed

    p5.fill(255)
    p5.text('program_state = ' + program_state, 10, 20)

    # change program state to PLAY after 3 seconds:
    if(p5.millis() > program_timer + 3000):
        print('3 seconds passed..')
        program_state = 'PLAY'
        program_timer = p5.millis()
    
    # begin playing with a mouse click if the ball is stopped:
    if(ball_xspeed == 0 and ball_yspeed == 0):
        if(p5.mouseIsPressed):
            # set random ball speed:
            ball_xspeed = p5.random(1, 1.5)
            ball_yspeed = p5.random(-1, 1)

    # update and draw ball:
    if(program_state == 'PLAY'):
        update_ball()
    draw_ball(ball_x, ball_y)

    # draw rectangle button during START state
    if(program_state == 'START'):
        p5.fill(255, 255, 0)  # yellow
        p5.rect(150, 150, 90, 40)
        p5.fill(0)
        p5.text('3 sec pause..', 115, 155)
    
    # check if wall is hit and update score:
    wall_hit = check_walls_hit()  # check if a wall was hit 
    if(wall_hit != None):
        ball_xspeed *= -1  # reverse horizontal ball speed

# update ball position (using a function with no arguments):
def update_ball():
    global ball_x, ball_xspeed
    global ball_y, ball_yspeed
    # updating ball position:
    ball_x = ball_x + ball_xspeed
    ball_y = ball_y + ball_yspeed
    # bouncing of ball from walls vertically:
    if(ball_y < ball_radius) or (ball_y > p5.height - ball_radius):
        ball_yspeed = -ball_yspeed
        
# draw ball (using a function with 2 arguments)
def draw_ball(x, y):
    p5.fill(255)
    p5.ellipse(x, y, ball_radius*2, ball_radius*2)

# check if the ball hit left or right wall:
def check_walls_hit():
    if(ball_xspeed > 0):  # ball is moving to the right
        if(ball_x + ball_radius >= p5.width):
            return 'right'
    elif(ball_xspeed < 0):  # ball is moving to the left
        if(ball_x - ball_radius <= 0):
            return 'left'
    else:
        return None

def keyPressed(event):
    pass  # do nothing

def keyReleased(event):
    pass  # do nothing

def mousePressed(event):
    global program_timer
    print('mousePressed..')
    global program_state
    if(program_state == 'PAUSE'):
        program_state = 'PLAY'
    elif(program_state == 'PLAY'):
        program_state = 'PAUSE'
        program_timer = p5.millis()  # update program timer
    print('change program_state to ' + program_state)

def mouseReleased(event):
    print('mouseReleased..')