import js
p5 = js.window

print('press keys 0 - 9 to highlight different letters of a string..')
# assign string to variable:
s = 'Monty Python'
print('this example uses the following string: ' + s)
# each letter of this string is an item in a sequence
# use square brackets with an index value to use the items:
print('item at index 0 of string: ' + s[0])
# the index value can be a variable:
i = 6
print('item at index ' + str(i) + ' of string: ' + s[i])
# len() is a function that returns the number of items in a sequence:
print('number of items (letters) in string: ' + str(len(s)))
# using a loop to traverse items of a string one by one:
print('first 5 items of string printed with a loop:')
for i in range(5):
    print(s[i])
# use "slicing" to get a portion of string with [start:stop] syntax:
print('items 0 - 5 of string with a slice: ' + s[0:5])
print('items 6 - 12 of string with a slice: ' + s[6:12])
# there are different Python methods available that work on strings
# for example, the upper() method converts a string to uppercase:
print('string converted to uppercase: ' + s.upper()) 

selected_index = 0

def setup():
    p5.createCanvas(300, 300)  
    p5.textFont('Monaco')  # apply built-in Monaco font texture
    
def draw():
    p5.background(255)   
    p5.fill(0)        
    p5.textSize(18)
    # draw each letter of string using a loop:
    for i in range(len(s)):
        # draw selected_index letter in red, others black:
        if(selected_index == i):
            p5.fill(255, 0, 0)
        else:
            p5.fill(0)
        p5.text(s[i], 80 + i*12, 150)

def keyPressed(event):
    global selected_index
    # keys 0 - 9 change the selected_index value:
    if(p5.key >= '0' and p5.key <= '9'):
        selected_index = int(p5.key)

def keyReleased(event):
    pass

def mousePressed(event):
    pass

def mouseReleased(event):
    pass