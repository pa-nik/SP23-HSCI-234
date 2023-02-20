import js
p5 = js.window

ball_x = 150
ball_y = 150
ball_radius = 25
ball_xspeed = 2
ball_yspeed = 1
left_paddle_y = 150
right_paddle_y = 150


def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas 
    p5.rectMode(p5.CENTER)  # draw rectangles from center

def draw():
    p5.background(255)           # white background

    global ball_x, ball_xspeed
    global ball_y, ball_yspeed
    
    # bouncing of ball from canvas sides:
    p5.fill(255)

    if(ball_x < ball_radius) or (ball_x > p5.width - ball_radius):
        ball_xspeed = -ball_xspeed
    if(ball_y < ball_radius) or (ball_y > p5.height - ball_radius):
        ball_yspeed = -ball_yspeed
        
    # updating ball position:
    ball_x = ball_x + ball_xspeed
    ball_y = ball_y + ball_yspeed
    p5.ellipse(ball_x, ball_y, ball_radius*2, ball_radius*2)

    # player paddles:
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


