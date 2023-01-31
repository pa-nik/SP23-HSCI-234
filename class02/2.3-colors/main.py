import js
p5 = js.window

def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas 

def draw():
    p5.background(255)           # white background
    # fill function with 1 argument sets gray fill
    # use values in the range 0 (black) to 255 (white):
    p5.fill(255) # white fill
    p5.ellipse(40, 50, 60, 60) 
    p5.fill(204) # light gray fill
    p5.ellipse(110, 50, 60, 60) 
    p5.fill(153) # medium gray fill
    p5.ellipse(180, 50, 60, 60)
    p5.fill(102) # dark gray fill
    p5.ellipse(250, 50, 60, 60)
    # noFill function turns off fill and takes no arguments:
    p5.noFill()
    p5.ellipse(70, 120, 60, 60) 
    p5.ellipse(110, 120, 60, 60) 
    # noStroke function turns off stroke:
    p5.noStroke()
    p5.ellipse(150, 120, 60, 60) # invisible! (no fill, no stroke)
    p5.fill(200) # light gray fill
    p5.ellipse(220, 120, 60, 60) 
    # fill function with 3 arguments sets RGB colors:
    p5.fill(255, 0, 0) # red fill
    p5.ellipse(40, 190, 60, 60) 
    p5.fill(0, 255, 0) # green fill
    p5.ellipse(110, 190, 60, 60) 
    p5.fill(0, 0, 255) # blue fill
    p5.ellipse(180, 190, 60, 60)
    p5.fill(255, 200, 50) # orange fill
    p5.ellipse(250, 190, 60, 60)
    # fill function with 4 arguments sets RGB colors + transparency:
    p5.fill(255, 0, 0, 150) # red fill with transparency
    p5.ellipse(40, 260, 60, 60) 
    p5.fill(0, 255, 0, 150) # green fill with transparency
    p5.ellipse(80, 260, 60, 60) 
    p5.fill(0, 0, 255, 150) # blue fill with transparency
    p5.ellipse(120, 260, 60, 60)
    p5.strokeWeight(4)
    p5.stroke(255, 0, 0) # red stroke
    p5.fill(255, 255, 0) # yellow fill
    p5.ellipse(190, 260, 60, 60)
    p5.stroke(0, 0, 255, 128) # blue stroke with transparency
    p5.noFill()
    p5.ellipse(230, 260, 60, 60)
    p5.stroke(0) # black stroke (reset)
    p5.fill(255) # white fill (reset)
    p5.strokeWeight(1) # 1-pixel stroke (reset)