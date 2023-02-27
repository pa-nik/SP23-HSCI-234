import js
p5 = js.window

def setup():
    p5.createCanvas(300, 300)  
    print('finished setup..')

def draw():
    p5.background(255)           
    p5.text(str(p5.mouseX) + ", " + str(p5.mouseY), 10, 15)

def keyPressed(event):
    print('keyPressed.. ' + str(p5.key))

def keyReleased(event):
    print('keyReleased.. ' + str(p5.key))

def mousePressed(event):
    print('mousePressed..')

def mouseReleased(event):
    print('mouseReleased..')













