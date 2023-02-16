import js
p5 = js.window

def setup():
    p5.createCanvas(300, 300)   
    #p5.rectMode(p5.CENTER)  # set rectangle drawing mode to CENTER

def draw():
    p5.background(255)    
    
    # condition with 2 alternatives (if, else)
    # using relational operator less than (<):
    if(p5.mouseX < 150):
        p5.fill(200)
    else:
        p5.fill(255)
    p5.rect(1, 1, 149, 149)  # top left square

    p5.fill(0)
    p5.text('mouseX: ' + str(p5.mouseX), 10, 20)
    p5.text('mouseY: ' + str(p5.mouseY), 10, 35)
    p5.text('mouseX < 150: ' + str(p5.mouseX < 150), 10, 65)

    # condition with 3 alternatives (if, elif, else)
    # using relational operator greater or equal than (>=)
    # using logical operator (and):
    if(p5.mouseX >= 150 and p5.mouseY < 150):
        p5.fill(150)
    elif(p5.mouseX >= 150):
        p5.fill(200)
    else:
        p5.fill(255)
    p5.rect(150, 1, 149, 149)  # top right square

    p5.fill(0)
    p5.text('mouseX >= 150: ' + str(p5.mouseX >= 150), 160, 20)
    p5.text('mouseX >= 150 and ', 160, 50)
    p5.text('mouseY < 150: ' + str(p5.mouseX >= 150 and p5.mouseY < 150), 160, 65)

    # nested condition (if, else inside of if)
    # using logical operator (or):
    if(p5.mouseX < 150 or p5.mouseY > 150):
        if(p5.mouseY > 150):
            p5.fill(150)
        else:
            p5.fill(200)
    else:
        p5.fill(255)
    p5.rect(1, 150, 149, 149)  # bottom left square
    
    p5.fill(0)
    p5.text('mouseY > 150: ' + str(p5.mouseY > 150), 10, 170)
    p5.text('mouseX < 150 or ', 10, 200)
    p5.text('mouseY < 150: ' + str(p5.mouseX < 150 or p5.mouseY > 150), 10, 215)

    # another nested condition (if, else inside of else)
    # using remainder (%) operator
    # also using relational operator not equal (!=):
    if(p5.mouseX % 100 < 50):  # True every other 50 pixels horizontally
        p5.fill(200)
    else:
        if(p5.mouseY % 100 < 50):  # True every other 50 pixels vertically
            p5.fill(150)
        else:
            p5.fill(255)
    p5.rect(150, 150, 149, 149)  # bottom right square

    p5.fill(0)
    p5.text('mouseX % 100 < 50: ', 160, 170) 
    p5.text(str(p5.mouseX % 100 < 50), 160, 185)
    p5.text('mouseY % 100 < 50: ', 160, 215)
    p5.text(str(p5.mouseY % 100 < 50), 160, 230)
    