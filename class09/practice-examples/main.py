import js
p5 = js.window

class Sprite:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def draw(self):
        p5.ellipse(self.x, self.y, 50, 50)
        
# example of a child object class from a parent (in parantheses):
class SpriteChild(Sprite):        
    pass  # do nothing keyword
    # this class inherits all the attributes and methods of the parent (Sprite class)
    # you can "override" the parent method with a new one by including it in the child
    # for example, SpriteChild draw method will draw a rectangle instead of ellipse:
    def draw(self):
        p5.rect(self.x, self.y, 50, 50)

# variable sprite assigned to SpriteChild object:
sprite = SpriteChild(x = 150, y = 150)    
print('sprite.x = ' + str(sprite.x) + 'sprite.y = ' + str(sprite.y))

# variable sprite2 assigned to Sprite object:
sprite2 = Sprite(x = 50, y = 50) 
print('sprite2.x = ' + str(sprite2.x) + 'sprite2.y = ' + str(sprite2.y))

# example of a virtual Pet object class:
class Pet:
    energy = 10
    def feed(self):
        self.energy += 1
    def play(self):
        self.energy -= 1
    def speak(self):
        print('hi!')

print('examples instantiating a Pet object and using its methods:')
pet = Pet()
print('pet.energy = ' + str(pet.energy))
pet.play()
pet.play()
print('pet.energy = ' + str(pet.energy))
pet.feed()
print('pet.energy = ' + str(pet.energy))
pet.speak()

# example of an object class that is a child of Pet:
class Dog(Pet):  # Dog is child of Pet
    def bark(self):
        print('Woof!')
    def speak(self):
        self.bark()

# another example of an object class that is a child of Pet:
class Cat(Pet):  # Cat is also a child of Pet
    def meow(self):
        print('Meow!')
    def speak(self):
        self.meow()

print('examples of instantiating Dog and Cat objects and using their methods:')
pet1 = Dog()
print('pet1.energy = ' + str(pet1.energy))
pet1.speak()
pet2 = Cat()
pet2.speak()

print('examples of using strings as a sequence of characters:')
fruit = 'banana'  # fruit is a string (sequence of letters)
print(fruit)  # print the string assigned to variable fruit
print(fruit[0])  # print first item of fruit
print(fruit[1])  # print second item of fruit
i = 2
print(fruit[i])  # print item i of fruit
print(fruit[i+1])
n = len(fruit)  # n is length of fruit
print(n)
print(fruit[n-1])  # print the last item of fruit

print('example of traversing a string sequence:')
for i in range(len(fruit)):
    print(fruit[i])  # print item i of fruit

print('another shorter way to traverse a string sequence:')
for i in fruit:
    print(i)  # i is assigned to string letters one by one

print('examples of string slicing:')
print(fruit[0:3])  # print the first 3 items (index 0-2) of fruit
print(fruit[3:6])  # print the last 3 items (index 3-6) of fruit
print(fruit[1:])  # print from index 1 to the end of string
print(fruit[:3])  # print from beginning to index 3

print('example of using a negative index value:')
print(fruit[-1])  # print the last item of fruit

print('example of slicing a string to make a new string:')
greeting = 'Hello world!'
print(greeting)
print('J' + greeting[1:])  # print J followed by greeting slice from index 1

print('example of using string methods')
print(fruit.upper())  # upper method changes a string to uppercase

print('example of a list of numbers')
number_list = [1, 2, 3, 4, 5]
print(number_list)  # print the number_list
print(number_list[0])  # print item at index 0 of number_list
print(number_list[1])  # print item at index 1 of number_list
i = 2
print(number_list[i])  # print item at index i 

print('example of a list of strings')
fruit_list = ['apple', 'banana', 'orange']
print(fruit_list)
print(fruit_list[0])

print('example of traversing a list:')
for n in number_list:  # variable n will be assigned to each item of number_list
    print(n)  # print item

print('another example of traversing a list:')
for i in range(len(number_list)):
    number_list[i] *= 2  # multiply item by 2
    print(number_list[i])  # print item at index i

print('examples of using list methods:')
number_list = [2, 1]
number_list.append(0)  # add 0 at the end of number_list
print(number_list)
number_list.insert(0, 3)  # add 3 at index 0 of number_list
print(number_list)
number_list.sort()  # sort the number_list
print(number_list)
number_list.pop()  # remove the last item of number_list
print(number_list)
number_list.pop(0)  # remove item at index 0 from number_list
print(number_list)
number_list.remove(2)  # remove 2 from number_list
print(number_list)
number_list.pop()  # remove one more item
print(number_list)

sprite_list = []  # start with an empty list

def setup():
    p5.createCanvas(300, 300) 
    print('finished setup') 
    
def draw():
    p5.background(255)
    p5.fill(0)
    
    sprite.draw()  # this SpriteChild object is a square
    p5.text('sprite', sprite.x + 10, sprite.y - 5)
    
    sprite2.draw()  # this Sprite object is a circle
    p5.text('sprite2', sprite2.x - 20, sprite2.y - 30)
    
    s = Sprite(x = p5.mouseX, y = p5.mouseY)  # create new sprite
    global sprite_list
    sprite_list.append(s)  # add new sprite to sprite_list

    # traverse sprite list and draw each sprite:
    p5.noStroke()
    for i in range(len(sprite_list)):
        p5.fill(255 - i * 5)
        # draw sprite_list item at index i in one step:
        #sprite_list[i].draw()  
        # or do it in 2 steps by assigning a list item to a variable first:
        s = sprite_list[i]  # s is item i of sprite_list
        s.draw()
        # draw text above the last item in sprite_list:
        if(i == len(sprite_list) - 1):
            p5.text('sprite_list', s.x - 25, s.y - 30)
        
    # limit the number of sprite in sprite_list to 50 items:
    if(len(sprite_list) > 50):
        sprite_list.pop(0)  # remove item at index 0 from sprite_list
    
    
def keyPressed(event):
    pass 

def keyReleased(event):
    pass

def mousePressed(event):
    pass

def mouseReleased(event):
    pass
    