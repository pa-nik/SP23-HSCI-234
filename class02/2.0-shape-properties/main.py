import js
p5 = js.window

def setup():
    p5.createCanvas(300, 300)    

def draw():
    p5.background(255)           
    # strokeWeight function takes 1 agrument (weight)
    # set stroke weight to 1 pixel:
    p5.strokeWeight(1)
    p5.ellipse(50, 50, 80, 80)
    # set stroke weight to 8 pixels:
    p5.strokeWeight(8) 
    p5.ellipse(150, 50, 70, 70)
    # set stroke weight to 20 pixels
    p5.strokeWeight(20) 
    p5.ellipse(250, 50, 60, 60)
    # strokeCap function takes 1 agrument (cap)
    # use built-in p5 variables ROUND, SQUARE and PROJECT
    # round line caps:
    p5.strokeCap(p5.ROUND) 
    p5.line(30, 120, 80, 180)
    # project line caps:
    p5.strokeCap(p5.PROJECT) 
    p5.line(100, 120, 150, 180)
    # square line caps:
    p5.strokeCap(p5.SQUARE) 
    p5.line(170, 120, 220, 180)
    # set stroke weight to 12 pixels:
    p5.strokeWeight(12)
    p5.line(230, 120, 280, 180)
    # strokeJoin function takes 1 argument (join)
    # use built-in p5 variables MITER (default), ROUND and BEVEL:
    # miter stroke corners:
    p5.strokeJoin(p5.MITER) 
    p5.rect(20, 220, 60, 60)
    # round stroke corners:
    p5.strokeJoin(p5.ROUND) 
    p5.rect(120, 220, 60, 60)
    # bevel stroke corners:
    p5.strokeJoin(p5.BEVEL) 
    p5.rect(220, 220, 60, 60)