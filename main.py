import turtle
import random

screen = turtle.Screen()
screen.setup(800, 400)
screen.title("Turtle Racing Game")
screen.bgcolor(0, 0.5, 0)

t1 = turtle.Turtle()
t1.shape("turtle")
t1.color(1.0, 0.9, 0.8)
t1.penup()
t1.goto(-380, 100)

t2 = turtle.Turtle()
t2.shape("turtle")
t2.color(1.0, 0.9, 0.8)
t2.penup()
t2.goto(-380, 50)

t3 = turtle.Turtle()
t3.shape("turtle")
t3.color(1.0, 0.9, 0.8)
t3.penup()
t3.goto(-380, 0)

t4 = turtle.Turtle()
t4.shape("turtle")
t4.color(1.0, 0.9, 0.8)
t4.penup()
t4.goto(-380, -50)

t5 = turtle.Turtle()
t5.shape("turtle")
t5.color(1.0, 0.9, 0.8)
t5.penup()
t5.goto(-380, -100)



while True:
    screen.update()

