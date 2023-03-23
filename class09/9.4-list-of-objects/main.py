import js
p5 = js.window

print('click with a mouse to create new Sprite objects on canvas')
print('press arrow left and right keys to select and highlight a sprite')
print('press Delete (Backspace) key to delete selected sprite')

# object class template for a generic Sprite object:
class Sprite:  
    x = 0
    y = 0
    speed = 0

    def __init__(self, x = 0, y = 0, speed = 0):
        self.x = x
        self.y = y
        self.speed = speed

    def update(self):
        if(self.y < p5.height + 25):
            self.y += self.speed
        else:
            self.y = -25

    def draw(self):
        p5.rect(self.x, self.y, 50, 50)   


sprite_list = []  # empty list
selected_index = 0

def setup():
    p5.createCanvas(300, 300)  
    p5.rectMode(p5.CENTER)
    
    global sprite_list
    sprite = Sprite(x = 100, y = 100, speed = 1)  # create a Sprite object
    sprite_list.append(sprite)  # append sprite to sprite_list
    sprite = Sprite(x = 200, y = 200, speed = 1.5)  # create another Sprite object
    sprite_list.append(sprite)  # append sprite to sprite_list
    
def draw():
    p5.background(255)   
    p5.fill(0)        
    p5.noStroke()
    # draw each item of number_list using a loop:
    for i in range(len(sprite_list)):
        if(selected_index == i):
            p5.fill(255, 0, 0)
        else:
            p5.fill(0)
        sprite = sprite_list[i]  # get sprite at index i from sprite_list
        sprite.update()
        sprite.draw()
        p5.text('sprite ' + str(i), sprite.x - 20, sprite.y - 30)

def keyPressed(event):
    global sprite_list
    global selected_index
    # keys 0 - 9 change the selected_index value:
    if(p5.keyCode == p5.RIGHT_ARROW):
        if(selected_index < len(sprite_list)-1):
            selected_index += 1
    elif(p5.keyCode == p5.LEFT_ARROW):
        if(selected_index > 0):
            selected_index -= 1
    elif(p5.keyCode == p5.BACKSPACE):
        print('remove selected sprite..')
        sprite_list.pop(selected_index)

def keyReleased(event):
    pass

def mousePressed(event):
    print('add new sprite..')
    global sprite_list
    sprite = Sprite(x = p5.mouseX, y = p5.mouseY, speed = p5.random(1, 2))
    sprite_list.append(sprite)

def mouseReleased(event):
    pass