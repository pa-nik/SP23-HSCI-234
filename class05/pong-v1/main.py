# V1 of Pong game
# click on canvas to begin playing
# use 'q' and 'a' to move left player paddle
# use 'p' and 'l' to move right player paddle

import js
p5 = js.window

ball_x = 150
ball_y = 150
ball_radius = 15
ball_xspeed = 0
ball_yspeed = 0

left_paddle_x = 10
left_paddle_y = 150
right_paddle_x = 290
right_paddle_y = 150
paddle_w = 20
paddle_h = 80

left_score = 0
right_score = 0

def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas 
    p5.rectMode(p5.CENTER)  # draw rectangles from center

def draw():
    p5.background(0)           # black background
    
    # global variables used in this function:
    global left_score, right_score
    global ball_xspeed, ball_yspeed

    p5.fill(255)
    p5.textSize(18)
    
    p5.text('left: ' + str(left_score), 50, 40)
    p5.text('right: ' + str(right_score), 200, 40)
    
    draw_dotted_line()

    # begin playing with a mouse click if the ball is stopped:
    if(ball_xspeed == 0 and ball_yspeed == 0):
        if(p5.mouseIsPressed):
            # set random ball speed:
            ball_xspeed = p5.random(1, 1.5)
            ball_yspeed = p5.random(-1, 1)
            # make the ball go in the direction of the winning player:
            if(left_score > right_score):
                ball_xspeed *= -1

    # update and draw ball:
    update_ball()
    draw_ball(ball_x, ball_y)
    
    # update and draw player paddles:
    update_paddles()
    draw_paddle(left_paddle_x, left_paddle_y)
    draw_paddle(right_paddle_x, right_paddle_y)
    
    # check if wall is hit and update score:
    wall_hit = check_walls_hit()  # check if a wall was hit 
    if(wall_hit != None):
        if(wall_hit == 'right'):  # right wall hit
            left_score += 1  # left player scores
            reset_game()
        elif(wall_hit == 'left'):  # left wall hit
            right_score += 1  # right player scores
            reset_game()

    # check if player paddle is hit and bounce ball:
    paddle_hit = check_paddles_hit()
    if(paddle_hit != None):
        ball_xspeed *= -1  # reverse horizontal ball speed

# reset the game variables:
def reset_game():
    global ball_x, ball_y
    global ball_xspeed, ball_yspeed
    ball_x = 150
    ball_y = 150
    ball_xspeed = 0
    ball_yspeed = 0

# draw dotted vertical line at the center of canvas:
def draw_dotted_line():
    p5.stroke(255)
    p5.push()
    p5.translate(p5.width/2, 5)
    for i in range(15):
        p5.line(0, 0, 0, 10)
        p5.translate(0, 20)
    p5.pop()
    p5.noStroke()

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

# move player paddles using 'a', 'q', 'p' and 'l' keys ):
def update_paddles():
    global left_paddle_y, right_paddle_y
    if(p5.keyIsPressed == True):
        if(p5.key == 'q'):
            # move left paddle up if it is above top of canvas:
            if(left_paddle_y > paddle_h/2):
                left_paddle_y -= 1
        elif(p5.key == 'a'):
            # move left paddle down if it is below bottom of canvas:
            if(left_paddle_y < p5.height - paddle_h/2):
                left_paddle_y += 1
        elif(p5.key == 'p'):
            # move right paddle up if it is above top of canvas:
            if(right_paddle_y > paddle_h/2):
                right_paddle_y -= 1
        elif(p5.key == 'l'):
            # move right paddle down if it is below bottom of canvas:
            if(right_paddle_y < p5.height - paddle_h/2):
                right_paddle_y += 1

# draw player paddle:
def draw_paddle(x, y):
    p5.fill(255)
    p5.rect(x, y, paddle_w, paddle_h)

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

# check if the ball hit left or right player paddle:  
def check_paddles_hit():
    if(ball_xspeed > 0):  # ball is moving to the right
        if(ball_x + ball_radius >= right_paddle_x - paddle_w/2) \
        and (ball_y > right_paddle_y - paddle_h/2) \
        and (ball_y < right_paddle_y + paddle_h/2):
            return 'right'  # right paddle hit
    elif(ball_xspeed < 0):  # ball is moving to the left
        if(ball_x - ball_radius <= left_paddle_x + paddle_w/2) \
        and (ball_y > left_paddle_y - paddle_h/2) \
        and (ball_y < left_paddle_y + paddle_h/2):
            return 'left'  # left paddle hit
    else:
        return None  # no paddles were hit

