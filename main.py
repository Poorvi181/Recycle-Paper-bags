import pgzrun,random
TITLE="Recycle Paper bags"
WIDTH=800
HEIGHT=600
centreX=WIDTH//2
centreY=HEIGHT//2
centre=(centreX,centreY)
Finallevel=10
Gameover=False
Gamecomplete=False
Currentlevel=1
items=["bag","battery","bottle","chips"]
def draw():
    screen.blit("bg2",(0,0))
def update():
    pass

def makeitems(numberofitems):
    numberofitems=["paperimg"]
    for i in range(0,numberofitems):
        randomitems=random.choice(items)
        numberofitems.append(randomitems)
    return numberofitems



        
pgzrun.go()

