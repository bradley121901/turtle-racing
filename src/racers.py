import turtle
import random

class Racer:
    # class attributes

    
    #constructor
    def __init__(self, x, y):
        self.turtle_racer = turtle.Turtle()
        self.turtle_racer.penup()
        self.turtle_racer.goto(x, y)
        self.turtle_racer.shape("turtle")
        
        r = random.randint(7, 9) * 0.1
        g = random.randint(7, 9) * 0.1
        b = random.randint(7, 9) * 0.1
        
        self.turtle_racer.color(r, g, b)
    
    def move(self):
        self.turtle_racer.setx(self.turtle_racer.xcor() + random.randint(0,3))
    
    