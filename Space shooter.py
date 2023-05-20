import pgzrun
TITLE="Space shooter"
WIDTH=1200
HEIGHT=800

ammo=0
side=1
point=0
win=False

bee=Actor("bee2")
bee2=Actor("bee2")
bee3=Actor("bee2")
bee4=Actor("bee2")
bee5=Actor("bee2")
bee6=Actor("bee2")
bee7=Actor("bee2")
bee8=Actor("bee2")

ship=Actor("spaceship")
bullet=Actor("bullet2")

def draw():

    screen.blit("space",(0,0))
    screen.blit("space",(800,0))
    screen.blit("space",(0,600))
    screen.blit("space",(800,600))

    bee.draw()
    bee2.draw()
    bee3.draw()
    bee4.draw()
    bee5.draw()
    bee6.draw()
    bee7.draw()
    bee8.draw()
    bullet.draw()
    ship.draw()

    if win==True:
        screen.draw.text("You Win!",(WIDTH/2-125,HEIGHT/2-25),fontsize=100)

def move():

    ship.x=WIDTH/2
    ship.y=HEIGHT-50

    bullet.x=WIDTH+100
    bullet.y=HEIGHT+150

    bee.x=377
    bee.y=40

    bee2.x=322
    bee2.y=40

    bee3.x=267
    bee3.y=40

    bee4.x=212
    bee4.y=40

    bee5.x=161
    bee5.y=40

    bee6.x=110
    bee6.y=40

    bee7.x=55
    bee7.y=40

    bee8.x=0
    bee8.y=40

def update():
    global ammo, side, bullet, point, win

    if ship.right <= WIDTH:
        if keyboard.right:
            ship.x=ship.x+5

    if ship.left >= 0:
        if keyboard.left:
            ship.x=ship.x-5
            
    if keyboard.Space:
        #bullet = Actor("spaceship")
        bullet.x = ship.x
        bullet.y = ship.y+25
        bullet.draw()
        ammo=ammo+1
        print("ammo: ",ammo)
        print("Score:",point)
    
    if bee8.left <= 0:
        side=1

    if bee.right >= WIDTH:
        side=2

    if side == 1:
        bee.x=bee.x+3
        bee2.x=bee2.x+3
        bee3.x=bee3.x+3
        bee4.x=bee4.x+3
        bee5.x=bee5.x+3
        bee6.x=bee6.x+3
        bee7.x=bee7.x+3
        bee8.x=bee8.x+3
        
    if side == 2:
        bee.x=bee.x-3
        bee2.x=bee2.x-3
        bee3.x=bee3.x-3
        bee4.x=bee4.x-3
        bee5.x=bee5.x-3
        bee6.x=bee6.x-3
        bee7.x=bee7.x-3
        bee8.x=bee8.x-3

    bullet.y=bullet.y-25

    if bullet.colliderect(bee):
        point=point+1
        bee.y=10000
        bullet.y=-10000


    if bullet.colliderect(bee2):
        point=point+1
        bee2.y=10000
        bullet.y=-10000

    if bullet.colliderect(bee3):
        point=point+1
        bee3.y=10000
        bullet.y=-10000

    if bullet.colliderect(bee4):
        point=point+1
        bee4.y=10000
        bullet.y=-10000

    if bullet.colliderect(bee5):
        point=point+1
        bee5.y=10000
        bullet.y=-10000

    if bullet.colliderect(bee6):
        point=point+1
        bee6.y=10000
        bullet.y=-10000

    if bullet.colliderect(bee7):
        point=point+1
        bee7.y=10000
        bullet.y=-10000

    if bullet.colliderect(bee8):
        point=point+1
        bee8.y=10000
        bullet.y=-10000

    if point==8:
        win=True


move()
update()

pgzrun.go()