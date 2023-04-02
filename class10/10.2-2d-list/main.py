import js
p5 = js.window

print('2D list of numbers:')
number_list = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]
print('number_list =', number_list)
print('number_list[0] =', number_list[0])
print('number_list[1] =', number_list[1])
print('number_list[0][0] =', number_list[0][0])
print('number_list[0][1] =', number_list[0][1])
print('number_list[0][3] =', number_list[0][3])
print('number_list[1][0] =', number_list[1][0])
print('number_list[1][3] =', number_list[1][3])
print('len(number_list) = ', len(number_list))
print('len(number_list[0]) = ', len(number_list[0]))

print('traverse 2D list and print items one by one:')
for j in range(len(number_list)):
    for i in range(len(number_list[0])):
        print('number_list[' + str(j) + '][' + str(i) + '] =', number_list[j][i])

# object class template for a generic Sprite object:
class Sprite:  
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def draw(self):
        p5.ellipse(self.x, self.y, 50, 50) 

sprite_list_2d = []
# add 4 sprites to sprite_list:
for j in range(2):
    # create an empty sprite_list and add 4 sprites to it:
    sprite_list = []
    for i in range(4):
        sprite_list.append(Sprite(50 + i*65, 115))
    # add sprite_list to sprite_list_2d:
    sprite_list_2d.append(sprite_list)
    # create another empty sprite_list and add 4 sprites to it:
    sprite_list = []
    for i in range(4):
        sprite_list.append(Sprite(50 + i*65, 190))
    # add sprite_list to sprite_list_2d:
    sprite_list_2d.append(sprite_list)

def setup():
    p5.createCanvas(300, 300)  
    
def draw():
    p5.background(255)   
    p5.fill(0)     
    p5.noStroke()  
    # traverse sprite_list_2d and draw each sprite:
    for j in range(2):
        for i in range(4):
            sprite = sprite_list_2d[j][i]
            # calculate distance from cursor to sprite:
            d = p5.dist(p5.mouseX, p5.mouseY, sprite.x, sprite.y)
            if(d < 25):
                p5.fill(255, 0, 0)
            else:
                p5.fill(0)
            sprite.draw()
            p5.text('sprite[' + str(j) + '][' + str(i) + ']', sprite.x - 30, sprite.y - 30)

def keyPressed(event):
    pass

def keyReleased(event):
    pass

def mousePressed(event):
    pass

def mouseReleased(event):
    pass