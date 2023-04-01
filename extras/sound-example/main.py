import js
p5 = js.window

print('click on canvas to play sound..')

sound = None  # variable to store sound data

def setup():
    p5.createCanvas(300, 300) 
    # load sound file data and assign to the global sound variable:
    global sound
    sound = p5.loadSound('shoot.wav')
    print('finished setup') 
    
def draw():
    p5.background(255)           

def keyPressed(event):
    pass 

def keyReleased(event):
    pass

def mousePressed(event):
    print('play sound..')
    sound.play()

def mouseReleased(event):
    pass