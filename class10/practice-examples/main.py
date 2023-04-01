import js
p5 = js.window

print('example of while loop:')
i = 0
while(i < 3):
    print(i)
    i += 1
    
class Sprite:
    x = 0
    y = 0
    w = 50
    h = 50
    def __init__(self, x=0, y=0, w=50, h=50):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    def draw(self):
        p5.ellipse(self.x, self.y, self.w, self.h)

class Button(Sprite):  # Button is a child of Sprite
    is_selected = False
    
    def draw(self):
        if(p5.mouseX > self.x) and (p5.mouseX < self.x + self.w) \
        and (p5.mouseY > self.y) and (p5.mouseY < self.y + self.h):
            p5.fill(255, 0, 0)  # red
            self.is_selected = True
        else:
            p5.fill(255)
            self.is_selected = False
        p5.rect(self.x, self.y, self.w, self.h)

sprite_list = []  # empty list to start
for i in range(5):
    #sprite = Sprite(x=150, y=150)  # create a Sprite object
    x = p5.random(50, 250)
    y = p5.random(50, 250)
    size = p5.random(30, 70)
    sprite = Sprite(x, y, size, size)  # create a Sprite object at (x, y)
    sprite_list.append(sprite)  # add sprite to the end of sprite_list
print('number of items in sprite_list = ' + str(len(sprite_list)))

btn = Button(x = 10, y = 10, w = 100, h = 50)  # create a Button object

def setup():
    p5.createCanvas(300, 300) 
    print('finished setup') 
    
def draw():
    p5.background(255)    
    p5.fill(255)
    #sprite.draw()
    #sprite_list[i].draw()  # draw the first item in sprite_list
    i = 0
    while(i < len(sprite_list)):
    #for i in range(len(sprite_list)):
        sprite = sprite_list[i]
        #sprite.y += 1
        # calculate distance between mouse cursor and sprite:
        d = p5.dist(sprite.x, sprite.y, p5.mouseX, p5.mouseY)
        if(d < sprite.w/2):
            p5.fill(255, 0, 0)
            if(p5.mouseIsPressed):
                # remove item i from sprite_list:
                print('remove item ' + str(i))
                sprite_list.pop(i)
        else:
            p5.fill(255)
        sprite.draw()  # draw item at index i in sprite_list
        i += 1  # increment i
    # check if mouse cursor is inside btn object:
    
    btn.draw()  
    

def keyPressed(event):
    pass 

def keyReleased(event):
    pass

def mousePressed(event):
    pass

def mouseReleased(event):
    if(btn.is_selected):
        print('clicked inside button!')