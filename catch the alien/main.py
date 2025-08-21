import pgzrun
import random

#setting width and height of the screen
WIDTH = 700
HEIGHT = 425

message = "Catch The Alien"


#creationg the game charecter ghost
alien = Actor("ghost")
alien.pos = (500,333)

def move_alien():
    alien.pos = (random.randint(50,650),random.randint(50,375))

#adding mouse clicking events 
def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        move_alien()
        message = "Noo, you caught me"
    else:
        message = "Haha, you'll never catch me"

#creating default system functions to be used or drawing on the screen
def draw():
    #changing the screen color
    screen.fill("red")
    #displaying ghost actor
    alien.draw()
    screen.draw.text(message,center = alien.pos,fontsize = 20)

#comMAND TO KEEP UR SCREEN VISABLE AND STOP IT FROM SCROLLING
pgzrun.go()
