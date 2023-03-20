import js
p5 = js.window

# class definition for the Bullet object:
class Bullet:  
    def __init__(self, x = 150, y = 250):
        self.x = x  
        self.y = y  

    def draw(self):
        p5.push()
        p5.translate(self.x, self.y)
        p5.fill(255, 0, 127)
        p5.rect(0, 0, 4, 8)
        p5.pop()
    
    def update(self):
        self.y -= 2

# class definition for the Spaceship object:
class Spaceship():  
    def __init__(self):
        self.img = p5.loadImage('spaceship.png')
        self.x = 150
        self.y = 282
    
    def draw(self):
        p5.push()
        p5.translate(self.x, self.y)
        p5.image(self.img, 0, 0)
        p5.pop()

# class definition for the Invader object:
class Invader:
    def __init__(self, x = 150, y = 150):
        self.x = x  
        self.y = y
        self.timer = p5.millis()
        self.img1 = p5.loadImage('invader_1.png');  
        self.img2 = p5.loadImage('invader_2.png');   
    
    def update(self):
        if(p5.millis() > self.timer + 500):
            if(self.y < p5.height - self.img1.height/2):
                self.y += 5
            else:
                self.y = self.img1.height/2
            self.timer = p5.millis()  # update timer

    def draw(self):
        p5.push()
        p5.translate(self.x, self.y)
        if(p5.millis() % 1000 < 500):
            p5.image(self.img1, 0, 0)
        else:
            p5.image(self.img2, 0, 0)
        p5.pop()


spaceship = Spaceship()  # instantiate the Spaceship object
bullet = Bullet(150, 0)  # instantiate the Bullet object
invader = Invader(150, 50)  # instantiate Invader object
font = p5.loadFont('PressStart2P.otf')
program_state = 'PLAY'

def setup():
    p5.createCanvas(300, 300)  
    p5.rectMode(p5.CENTER)
    p5.imageMode(p5.CENTER)
    print('use space bar to shoot the invaders..')

def draw():
    global spaceship
    p5.background(0)    
    global program_state
    if(program_state == 'PLAY'):
        bullet.update() 
        bullet.draw() 
        if(p5.keyIsPressed == True):
            if(p5.keyCode == p5.RIGHT_ARROW):
                if(spaceship.x < p5.width - spaceship.img.width/2):
                    spaceship.x += 2
                    bullet.x = spaceship.x
            elif(p5.keyCode == p5.LEFT_ARROW):
                if(spaceship.x > spaceship.img.width/2):
                    spaceship.x -= 2
                    bullet.x = spaceship.x 
        spaceship.draw()
        invader.update()
        invader.draw()
        # calculate the distance between invader and bullet:
        d = p5.dist(invader.x, invader.y, bullet.x, bullet.y)
        if(d < 20):  
            print('invader hit!')
            program_state = 'WIN'
        # condition to check if the invader reached the bottom:
        if(invader.y > p5.height - invader.img1.height/2):
            program_state = 'LOOSE'
    elif(program_state == 'WIN'):
        p5.textFont(font)
        p5.textSize(18)
        p5.fill(255)
        p5.text('You Win!', 80, 150)
    elif(program_state == 'LOOSE'):
        p5.textFont(font)
        p5.textSize(18)
        p5.fill(255)
        p5.text('You Loose!', 60, 150)
    
def keyPressed(event):
    pass

def keyReleased(event):
    global bullet
    if(p5.key == ' '):
        # reset the bullet to spaceship coordinates:
        bullet.x = spaceship.x
        bullet.y = spaceship.y

def mousePressed(event):
    pass

def mouseReleased(event):
    pass