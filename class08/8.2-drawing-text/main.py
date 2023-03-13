import js
p5 = js.window

# to use fonts in a program follow 4 steps: 
# 1. copy font file(s) to the same directory as main.py 
# 2. use p5.loadFont function to assign font data to variable:
font1 = p5.loadFont('PressStart2P.otf')  # load font data to font1

def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas 
    
def draw():
    p5.background(255)
    # 3. use p5.textFont function to apply font texture
    p5.textFont(font1)  # use font1 texture
    # 4. use p5.text function to draw text
    # draw text at coordinates (20, 40):
    p5.text('PressStart2P', 20, 40)  
    p5.textSize(24)  # set text size to 24 points
    p5.text('24pt Size', 25, 75)  
    p5.textSize(14)  # set text size to 14 points
    # some common fonts may be supported without loading them:
    p5.textFont('Courier')
    p5.text('14pt Courier font', 20, 100) 
    # font size can be specified as the 2nd argument of p5.textFont:
    p5.textFont('Comic Sans MS', 18)
    p5.text('18pt Comic Sans MS font', 20, 130) 
    p5.textFont('Times', 18)
    p5.text('18pt Times font', 20, 160) 
    p5.textFont('Helvetica', 18)
    p5.fill(255, 0, 0)
    p5.text('18pt Helvetica font', 20, 190)
    p5.fill(0)
    # multi-line text in a bounding box can be drawn by adding
    # 3rd (width) and 4th (height) arguments to p5.text function:
    p5.text('Example of multi-line text in a bounding box..', 20, 220, 200, 100)

def keyPressed(event):
    pass

def keyReleased(event):
    pass

def mousePressed(event):
    pass

def mouseReleased(event):
    pass


    