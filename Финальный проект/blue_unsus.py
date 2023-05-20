tx = 0
ty = 0
zacruglenie = 10
c = 255
a = 12.5

def setup():
    size(1900,1000)
    noStroke()
    frameRate(20)

def draw():
    if tyr == ty and txr == tx:
    c = c - b
    global tx,ty,zacruglenie,c,a
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
    if keyPressed:
        if key == 'W' or key == 'w' or key == 'ц' or key == 'Ц':
            ty = ty - a
        if key == 'D' or key == 'd' or key == 'В' or key == 'в':
            tx = tx + a
        if key == 'A' or key == 'a' or key == 'Ф' or key == 'ф':
            tx = tx - a
        if key == 'ы' or key == 'Ы' or key == 'S' or key == 's':
            ty = ty + a 
