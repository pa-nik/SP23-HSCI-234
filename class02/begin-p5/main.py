import js
p5 = js.window

def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas 

def draw():
    p5.background(255)           # white background
    p5.push()
    p5.translate(150, 150)
    draw_flower()
    p5.pop()
    
def draw_petal():
    p5.ellipse(75, 0, 100, 25)

def draw_flower():
    for i in range(20):
        p5.noStroke()
        p5.fill(i*25, 255-i*25, 0)
        p5.rotate(p5.radians(360/20))
        draw_petal()
