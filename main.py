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
players=[]
def draw():
    screen.blit("bg2",(0,0))
    for player in players:
        player.draw()

def update():
    global players,Currentlevel
    if len(players)==0:
        players=creation(Currentlevel)
    

def creation(numberofitems):
    itemstocreate=makeitems(numberofitems)
    newitems=createitems(itemstocreate)
    layoutitems(newitems)
    return newitems()

def makeitems(numberofitems):
    numberofitem=["paperimg"]
    for i in range(0,numberofitems):
        randomitems=random.choice(items)
        numberofitem.append(randomitems)
    return numberofitem


def createitems(numberofitems):
    newitems=[] 
    for i in range(0,numberofitems): 
        item=Actor(i)
        newitems.append(item)
    return newitems

def layoutitems(numberofitems):
    numberofgaps=len(numberofitems)+1
    gapsize=WIDTH/numberofgaps
    random.shuffle(numberofitems)
    for index,item in enumerate(numberofitems):
        newXpos=(index+1)*gapsize
        item.x=newXpos



pgzrun.go()
