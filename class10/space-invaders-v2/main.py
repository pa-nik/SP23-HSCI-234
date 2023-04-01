import js
p5 = js.window

# class definition for the generic Sprite object:
class Sprite:
    def __init__(self, x = 150, y = 250):
        self.x = x  
        self.y = y   
        
# class definition for the Bullet object:
# Bullet inherits x, y attributes of Sprite
class Bullet(Sprite):  # Bullet is a child of Sprite  
    def draw(self):
        p5.push()
        p5.translate(self.x, self.y)
        p5.fill(255, 0, 127)
        p5.rect(0, 0, 4, 8)
        p5.pop()
    
    def update(self):
        self.y -= 2

# class definition for the Spaceship object:
# Spaceship inherits x, y attributes of Sprite and contains 
# new attributes width, height
class Spaceship(Sprite):  # Spaceship is a child of Sprite
    def __init__(self):
        self.img = p5.loadImage('spaceship.png')
        self.x = 150
        self.y = 282
        self.width = self.img.width
        self.height = self.img.height
    
    def draw(self):
        p5.push()
        p5.translate(self.x, self.y)
        p5.image(self.img, 0, 0)
        p5.pop()

# class definition for the Invader object:
# Invader inherits x, y attributes of Sprite and contains 
# new attributes width, height, timer, bitmap1, bitmap2
class Invader(Spaceship):
    # 2D list of 11x8 Invader bits (first set of pixels)
    bitmap1  = [
        [ 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1 ],
        [ 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1 ],
        [ 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1 ],
        [ 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1 ],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [ 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0 ],
        [ 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0 ],
        [ 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1 ]
    ]
    # 2D list of 11x8 Invader bits (second set of pixels)
    bitmap2  = [
        [ 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1 ],
        [ 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0 ],
        [ 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0 ],
        [ 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0 ],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
        [ 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1 ],
        [ 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1 ]
    ]

    def draw_bitmap(self, n):
        p5.fill(255)
        p5.noStroke()
        p5.push()
        p5.translate(-11*3, -8*3)  # center the 11x8 pixel bitmap
        # traverse 2D lists with i and j loops:
        for j in range(8):
            for i in range(11):
                if(n == 1):  # draw column j, row i of bitmap1
                    if(self.bitmap1[j][i] == 0):
                        p5.rect(i*6, j*6, 6, 6)
                else:        # draw column j, row i of bitmap2
                    if(self.bitmap2[j][i] == 0):
                        p5.rect(i*6, j*6, 6, 6)
        p5.pop()

    def __init__(self, x = 150, y = 150):
        self.x = x  
        self.y = y
        self.width = 56
        self.height = 77
        self.timer = p5.millis()
        #self.img1 = p5.loadImage('invader_1.png');  
        #self.img2 = p5.loadImage('invader_2.png');   
    
    def update(self):
        if(p5.millis() > self.timer + 500):
            if(self.y < p5.height - self.height/2):
                self.y += 5
            else:
                self.y = self.height/2
            self.timer = p5.millis()  # update timer

    def draw(self):
        p5.push()
        p5.translate(self.x, self.y)
        if(p5.millis() % 1000 < 500):
            #p5.image(self.img1, 0, 0)
            self.draw_bitmap(1)  
        else:
            #p5.image(self.img2, 0, 0)
            self.draw_bitmap(2)  
        p5.pop()


spaceship = Spaceship()  # instantiate the Spaceship object
bullet = Bullet(150, 0)  # instantiate the Bullet object 
font = p5.loadFont('PressStart2P.otf')
program_state = 'START' 

def init_invaders():
    global invader_list
    invader_list = [] 
    for j in range(2):
        for i in range(3):
            invader = Invader(50 + i*100, 50 + j*60)  # instantiate Invader object
            invader_list.append(invader)  # add Invader object to invader_list

def setup():
    p5.createCanvas(300, 300)  
    p5.rectMode(p5.CENTER)
    p5.imageMode(p5.CENTER)
    init_invaders()
    print('use space bar to shoot the invaders..')

def draw():
    global spaceship
    p5.background(0)    
    global program_state
    if(program_state == 'START'):
        p5.textFont(font)
        p5.textSize(18)
        s = 'Click to Start!'
        for i in range(len(s)):
            if(i % 2 == 1) and (p5.millis() % 1000 < 500):
                p5.fill(255)
            elif(i % 2 == 0) and (p5.millis() % 1000 > 500):
                p5.fill(255)
            else:
                p5.fill(0, 255, 0)
            p5.text(s[i], 20 + i*18, 150)
    elif(program_state == 'PLAY'):
        bullet.update() 
        bullet.draw() 
        if(p5.keyIsPressed == True):
            if(p5.keyCode == p5.RIGHT_ARROW):
                if(spaceship.x < p5.width - spaceship.width/2):
                    spaceship.x += 2
            elif(p5.keyCode == p5.LEFT_ARROW):
                if(spaceship.x > spaceship.width/2):
                    spaceship.x -= 2 
        spaceship.draw() 
        i = 0    
        while(i < len(invader_list)):  # traverse invader_list
            invader = invader_list[i]  # invader is item i of invader_list
            invader.update()
            invader.draw()
            # calculate the distance between invader and bullet:
            d = p5.dist(invader.x, invader.y, bullet.x, bullet.y)
            if(d < 30):  
                print('invader hit!')
                bullet.y = 0  # move bullet to top of screen
                invader_list.pop(i)  # remove item i from invader_list
                if(len(invader_list) == 0): # invader_list is empty
                    print('all invaders eliminated!')
                    program_state = 'WIN' 
               # condition to check if the invader reached the bottom:
            if(invader.y > p5.height - invader.height/2):
                program_state = 'LOOSE'
            i += 1  # increment i   
    elif(program_state == 'WIN'):
        p5.textFont(font)
        p5.textSize(18)
        p5.fill(0, 255, 0)
        p5.text('You Win!', 80, 150)
    elif(program_state == 'LOOSE'):
        p5.textFont(font)
        p5.textSize(18)
        p5.fill(255)
        p5.text('You Loose!', 60, 150)
    if(program_state == 'WIN') or (program_state == 'LOOSE'):
        if(p5.millis() % 1000 < 500):
            p5.fill(255)
        else:
            p5.fill(255, 255, 0)
        p5.textSize(12)
        p5.text('click to restart game', 25, 260)
    
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
    global program_state
    if(program_state == 'START'):
        program_state = 'PLAY'
        print('changed program_state to ' + program_state)
    elif(program_state == 'WIN') or (program_state == 'LOOSE'):
        print('restart game..')
        init_invaders()
        program_state = 'PLAY'
