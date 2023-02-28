import js
p5 = js.window

angle = p5.radians(270)
timer_ms = 0

def setup():
    p5.createCanvas(300, 300)  
    print('finished setup() at ' + str(p5.millis()) + " ms")

def draw():
    p5.background(255)           
    msec = p5.millis()  # get running time in milliseconds
    sec = int(msec / 1000)  # calculate time in seconds
    p5.fill(0)
    p5.text('milliseconds: ' + str(msec), 10, 20)
    p5.text('seconds: ' + str(sec), 10, 35)

    global timer_ms, angle
    # compare current running time to saved timer plus interval:
    if(p5.millis() > timer_ms + 1000):  
        # print('1 second passed..')
        angle += p5.radians(6)  # update angle
        timer_ms = p5.millis()  # update timer
    # draw clock marks and handle:
    draw_marks()
    draw_handle()

    # draw a circle blinking every half second using
    # the remainder of running time compared to interval:
    p5.text('500ms: ', 10, 50)
    if(p5.millis() % 1000 < 500):
        p5.fill(255, 0, 0)
    else:
        p5.fill(255)
    p5.ellipse(58, 46, 10, 10)

  
def draw_marks():
    p5.push()
    p5.translate(p5.width/2, p5.height/2)
    for i in range(12):
        p5.rotate(p5.radians(30))
        p5.push()
        p5.translate(100, 0)
        p5.ellipse(0, 0, 10, 10)
        p5.pop()
    p5.pop()
  
def draw_handle():
  p5.push()
  p5.translate(p5.width/2, p5.height/2)
  p5.rotate(angle)
  p5.rect(0, -5, 100, 10)
  p5.pop()

def keyPressed(event):
    pass  # do nothing

def keyReleased(event):
    pass

def mousePressed(event):
    pass

def mouseReleased(event):
    pass