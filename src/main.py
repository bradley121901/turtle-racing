import turtle
import random
import racers

FINISH_LINE_XCOORD = 350
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
START_XCOORD = -380

screen = turtle.Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.title("Turtle Racing Game")
screen.bgcolor(0, 0.5, 0)

t1 = racers.Racer(START_XCOORD, 100)
t2 = racers.Racer(START_XCOORD, 50)
t3 = racers.Racer(START_XCOORD, 0)
t4 = racers.Racer(START_XCOORD, -50)
t5 = racers.Racer(START_XCOORD, -100)

finish_line = turtle.Turtle()
finish_line.penup()
finish_line.goto(FINISH_LINE_XCOORD, 500)
finish_line.pendown()
finish_line.goto(FINISH_LINE_XCOORD, -500)


while True:
    t1.move()
    t2.move()
    t3.move()
    t4.move()
    t5.move()
    
    if t1.check_finish(FINISH_LINE_XCOORD):
        print("turtle 1 wins!")
        break
    if t1.check_finish(FINISH_LINE_XCOORD):
        print("turtle 2 wins!")
        break
    if t1.check_finish(FINISH_LINE_XCOORD):
        print("turtle 3 wins!")
        break
    if t1.check_finish(FINISH_LINE_XCOORD):
        print("turtle 4 wins!")
        break
    if t1.check_finish(FINISH_LINE_XCOORD):
        print("turtle 5 wins!")
        break
    
    screen.update()

