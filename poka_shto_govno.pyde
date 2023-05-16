tx = 0
ty = 0
zacruglenie = 10
c = 255
k = 255

def setup():
    size(1920,1080)
    noStroke()
    frameRate(10000)

def draw():
    global tx,ty,zacruglenie,c,k
    background(0,255,0)
    translate(0,12.5)
    fill(0,0,c)
    rect(tx,ty,25,25,zacruglenie)
    translate(12.5,-12.5)
    rect(tx,ty,37.5,37.5,zacruglenie)
    translate(0,12.5)
    rect(tx,ty,12.5,37.5,zacruglenie)
    translate(25,0)
    rect(tx,ty,12.5,37.5,zacruglenie)
    fill(150)
    translate(-12.5,0)
    rect(tx,ty,37.5,12.5,zacruglenie)
    fill(k,0,0)
    rect(tx,ty,25,25,zacruglenie)
    translate(12.5,-12.5)
    rect(tx,ty,37.5,37.5,zacruglenie)
    translate(0,12.5)
    rect(tx,ty,12.5,37.5,zacruglenie)
    translate(25,0)
    rect(tx,ty,12.5,37.5,zacruglenie)
    fill(150)
    translate(-12.5,0)
    rect(tx,ty,37.5,12.5,zacruglenie)
    if keyPressed:
        if key == 'W' or key == 'w' or key == 'ц' or key == 'Ц':
            ty = ty - 1
    elif keyPressed:
        if key == 'D' or key == 'd' or key == 'В' or key == 'в':
            tx = tx + 1
    elif keyPressed:
        if key == 'A' or key == 'a' or key == 'Ф' or key == 'ф':
            tx = tx - 1
    elif keyPressed:
        if key == 'ы' or key == 'Ы' or key == 'S' or key == 's':
            ty = ty + 1 
    elif keyPressed:
        if key == 'i' or key == 'I' or key == 'ш' or key == 'Ш':
            tyr = tyr - 1
    elif keyPressed:
        if key == 'д' or key == 'Д' or key == 'l' or key == 'L':
            txr = txr + 1
    elif keyPressed:
        if key == 'j' or key == 'J' or key == 'О' or key == 'о':
            txr = txr - 1
    elif keyPressed:
        if key == 'л' or key == 'Л' or key == 'K' or key == 'k':
            tyr = tyr + 1 
