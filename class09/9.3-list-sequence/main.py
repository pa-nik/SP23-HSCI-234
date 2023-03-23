import js
p5 = js.window

print('press left and right arrow keys to highlight different numbers..')

# to create a list put values separated by commas in square brackets:
print('list of numbers:')
number_list = [1, 2, 3, 4, 5]
print(number_list)    
print('list of strings:')
fruit_list = ['apple', 'banana', 'orange']
print(fruit_list)    

# as with strings, use square brackets with index value to get a list item:
n = number_list[0]  
print('item 0 of number_list = ' + str(n))  
n = fruit_list[0]  
print('item 0 of fruit_list = ' + str(n))  

# also like strings, the len() function returns the length of a list sequence:
n = len(number_list)
print('number of items (length) of number_list = ' + str(n)) 
n = len(fruit_list)
print('number of items of fruit_list = ' + str(n)) 

# instead of a number, a variable can be used as index value:
i = 1
print('item ' + str(i) + ' of number_list = ' + str(number_list[i]))
i = 2
print('item ' + str(i) + ' of fruit_list = ' + str(fruit_list[i]))

# to traverse a list item by item, use a loop:
print('items of number_list printed with a loop:')
for i in range(len(number_list)):
    print(number_list[i])

# list "slicing" use the same [start:stop] syntax as string slicing:
number_list_slice = number_list[0:2]
print('slice 0-2 of number_list: ' + str(number_list_slice)) 
number_list_slice = number_list[2:5]
print('slice 2-5 of number_list: ' + str(number_list_slice)) 

# an empty list is just square brackets with nothing between:
new_list = []
print('new_list = ' + str(new_list))

# append list method adds an item to the end of a list:
new_list.append(1)
print('new_list after append(0) = ' + str(new_list))
new_list.append(2)
print('new_list after append(2) = ' + str(new_list))

# insert list method inserts an item at the specified index:
new_list.insert(0, 0)  # insert 0 at index 0
print('new_list after insert(0, 0) = ' + str(new_list))
new_list.insert(0, -1)  # insert -1 at index 0
print('new_list after insert(0, -1) = ' + str(new_list))

# pop list method removes an item at the specified index:
new_list.pop(0)  # remove item at index 0
print('new_list after pop(0) = ' + str(new_list))

# without an argument, the pop method removes the last list item:
new_list.pop()  # remove the last item
print('new_list after pop() = ' + str(new_list))

selected_index = 0

def setup():
    p5.createCanvas(300, 300)  
    p5.textFont('Monaco')  # apply built-in Monaco font texture
    
def draw():
    p5.background(255)   
    p5.fill(0)        
    p5.textSize(18)
    # draw each item of number_list using a loop:
    for i in range(len(number_list)):
        # draw selected_index letter in red, others black:
        if(selected_index == i):
            p5.fill(255, 0, 0)
        else:
            p5.fill(0)
        p5.text(number_list[i], 100 + i*20, 120)

    # draw each item of fruit_list using a loop:
    p5.fill(0)
    for i in range(len(fruit_list)):
        p5.text(fruit_list[i], 30 + i*80, 170)

def keyPressed(event):
    global selected_index
    # keys 0 - 9 change the selected_index value:
    if(p5.keyCode == p5.RIGHT_ARROW):
        if(selected_index < len(number_list)-1):
            selected_index += 1
    elif(p5.keyCode == p5.LEFT_ARROW):
        if(selected_index > 0):
            selected_index -= 1

def keyReleased(event):
    pass

def mousePressed(event):
    pass

def mouseReleased(event):
    pass