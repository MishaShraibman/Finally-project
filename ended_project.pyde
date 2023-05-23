tx = 0
ty = 0
zacruglenie = 10
c = 255
a = 1
k = 255
txr = 1900-12.5*5
tyr = 1000-12.5*3
b = 27.2
coordxrmf = random(0,1850)
coordyrmf = random(0,950)
coordxbmf = random(0,1850)
coordybmf = random(0,950)

def setup():
    size(1900,1000)
    noStroke()
    frameRate(2500000000000000000000000000)

def draw():
    global tx,ty,zacruglenie,c,k,txr,tyr,a,b,coordxrmf,coordyrmf,coordxbmf,coordybmf
    if tyr == ty and txr == tx:
        c = c - b
        k = k - b
    background(0,255,0)
    push()
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
    pop()
    push()
    fill(k,0,0)
    rect(txr,tyr,25,25,zacruglenie)
    translate(12.5,-12.5)
    rect(txr,tyr,37.5,37.5,zacruglenie)
    translate(0,12.5)
    rect(txr,tyr,12.5,37.5,zacruglenie)
    translate(25,0)
    rect(txr,tyr,12.5,37.5,zacruglenie)
    fill(150)
    translate(-12.5,0)
    rect(txr,tyr,37.5,12.5,zacruglenie)
    pop()
    fill(255,0,0)
    square(coordxrmf,coordyrmf,50)
    fill(0,0,255)
    square(coordxbmf,coordybmf,50)
    if keyPressed:
        if key == 'W' or key == 'w' or key == 'ц' or key == 'Ц':
            ty = ty - a
        if key == 'D' or key == 'd' or key == 'В' or key == 'в':
            tx = tx + a
        if key == 'A' or key == 'a' or key == 'Ф' or key == 'ф':
            tx = tx - a
        if key == 'ы' or key == 'Ы' or key == 'S' or key == 's':
            ty = ty + a 
        if key == 'i' or key == 'I' or key == 'ш' or key == 'Ш':
            tyr = tyr - a
        if key == 'д' or key == 'Д' or key == 'l' or key == 'L':
            txr = txr + a
        if key == 'j' or key == 'J' or key == 'О' or key == 'о':
            txr = txr - a
        if key == 'л' or key == 'Л' or key == 'K' or key == 'k':
            tyr = tyr + a 
    if ty >= coordyrmf and ty <= coordyrmf + 50 and tx >= coordxrmf and tx <= coordxrmf + 50:
        k -= b
        coordxrmf = random(0,1850)
        coordyrmf = random(0,950)
    if tyr >= coordybmf and tyr <= coordybmf + 50 and txr >= coordxbmf and txr <= coordxbmf + 50:
        c -= b
        coordxbmf = random(0,1850)
        coordybmf = random(0,950)
