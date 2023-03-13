import js
p5 = js.window

# to use images in a program follow 3 steps: 
# 1. copy image files to the same directory as main.py 
# 2. assign images to variables with p5.loadImage function 
img1 = p5.loadImage('invader_1.png');  # load image data to img1
img2 = p5.loadImage('invader_2.png');  # load image data to img2 

def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas 

def draw():
    p5.background(255)
    # 3. use p5.image function to draw images
    # draw img1 at coordinates (25, 25):
    p5.image(img1, 25, 25)  
    # draw img1 at (125, 25) and 2x width and height:
    p5.image(img1, 125, 25, img1.width*2, img1.height*2)
    p5.tint(0, 255, 0)  # enable green tint
    # draw img2 at coordinates (25, 150):
    p5.image(img2, 25, 150)  
    p5.noTint()  # disable tint
    p5.imageMode(p5.CENTER)  # draw images from center
    p5.push()
    p5.translate(200, 225)
    # alternate between img1 and img2 every 500 milliseconds:
    if(p5.millis() % 1000 < 500):
        p5.image(img1, 0, 0)
    else:
        p5.image(img2, 0, 0)
    p5.pop()
    p5.imageMode(p5.CORNER)  # draw images from corner

def keyPressed(event):
    pass

def keyReleased(event):
    pass

def mousePressed(event):
    pass

def mouseReleased(event):
    pass


    