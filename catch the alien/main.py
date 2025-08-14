import pgzrun
import random

#setting width and height of the screen
WIDTH = 700
HEIGHT = 425
#creationg the game charecter ghost
ghost = Actor("ghost")
ghost.pos = (500,333)

def move_ghost():
    ghost.pos = (random.randint(50,650),random.randint(50,375))

#creating default functions to be used or drawing on the screen
def draw():
    #changing the screen color
    screen.fill("red")
    #displaying ghost actor
    ghost.draw()

#comMAND TO KEEP UR SCREEN VISABLE AND STOP IT FROM SCROLLING
pgzrun.go()
