import turtle
import random
import racers

screen = turtle.Screen()
screen.setup(800, 400)
screen.title("Turtle Racing Game")
screen.bgcolor(0, 0.5, 0)

t1 = racers.Racer(-380, 100)
t2 = racers.Racer(-380, 50)
t3 = racers.Racer(-380, 0)
t4 = racers.Racer(-380, -50)
t5 = racers.Racer(-380, -100)



while True:
    
    t1.move()
    t2.move()
    t3.move()
    t4.move()
    t5.move()
    
    screen.update()

