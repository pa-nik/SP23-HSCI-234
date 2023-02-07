import js
p5 = js.window

def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas 

def draw():
    p5.background(255)           # white background
    p5.strokeWeight(1)
    p5.stroke(0)
    p5.fill(255)  # white fill
    p5.line(10, 10, 100, 80)
    p5.strokeWeight(2)
    p5.fill(150)  # fill with gray
    p5.stroke(0, 0, 255)  # blue stroke
    p5.triangle(110, 20, 150, 90, 200, 20)
    p5.strokeWeight(4)
    p5.fill(255)  # fill with white
    p5.stroke(120) # stroke with gray
    p5.quad(210, 10, 290, 20, 280, 100, 220, 90)
    p5.stroke(0) # black stroke
    p5.strokeWeight(1)
    p5.fill(200)
    p5.noStroke()  # no stroke
    p5.rect(10, 110, 120, 80)
    p5.noFill()  # no fill
    p5.stroke(0)  # black stroke
    p5.ellipse(60, 150, 60, 60)
    p5.fill(255, 255, 0)  # yellow fill
    p5.ellipse(150, 150, 80, 80)
    #p5.arc(150, 150, 60, 60, 0, p5.PI)
    #p5.arc(150, 150, 60, 60, 0, 3.14)
    p5.arc(150, 150, 60, 60, 0, p5.radians(180))
    p5.strokeCap(p5.ROUND)
    p5.strokeWeight(8)
    p5.line(200, 120, 280, 180)
    p5.strokeCap(p5.SQUARE)
    p5.line(200, 180, 280, 120)
    p5.noStroke()
    p5.fill(200, 0, 0)  # red fill
    p5.ellipse(50, 250, 50, 50)
    p5.fill(0, 255, 0, 150)  # green fill with transparency
    p5.ellipse(80, 250, 70, 70)
    p5.fill(0, 0, 200, 100)  # blue fill with transparency
    p5.rectMode(p5.CENTER)  # change rectangle drawing mode to center
    p5.rect(150, 250, 100, 50)
    p5.rectMode(p5.CORNER)  # change rect drawing mode to corner

    # drawing with variables
    y = 250
    d = 20
    #p5.ellipse(200, y, d, d)
    #p5.ellipse(240, y, d, d)
    #p5.ellipse(280, y, d, d)
    for i in range(3):  # loop from 0 to 3 stepping by 1
        x = 200 + i*30
        d = 20 + i*5
        gray = 100 + i*50
        p5.fill(gray)
        p5.ellipse(x, y, d, d)
        
    #for i in range(0, 80, 40)  # loop from 0 to 80 stepping by 40
    #    x = 200 + i
    #    p5.ellipse(x, y, d, d)