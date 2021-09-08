#Simple pong game from FreeCodeCamp on Youtube.
#By @TokyoEdTecg

import turtle


wn = turtle.Screen()
wn.title("Pong by CheckReality")
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)


#Paddlle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.penup()
paddle_a.goto()


#Paddle B


#Ball



#Main game loop
while True:
    wn.update()
    