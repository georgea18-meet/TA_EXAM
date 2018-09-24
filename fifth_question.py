from turtle import Turtle
import turtle, math

turtle.ht()

class Image(Turtle):
    def __init__(self, dx, dy):
        Turtle.__init__(self)
        turtle.register_shape('trump.gif')
        self.dx = dx
        self.dy = dy
        self.shape('trump.gif')
        self.pu()
        self.speed(0)
    def move(self):
        while math.fabs(self.xcor())<turtle.window_width()/2 and math.fabs(self.ycor())<turtle.window_height()/2:
            self.goto(self.xcor()+self.dx,self.ycor()+self.dy)
        if math.fabs(self.xcor())>=turtle.window_width()/2:
            self.dx = 0-self.dx
            self.goto(self.xcor()+self.dx,self.ycor()+self.dy)
        else:
            self.dy = 0-self.dy
            self.goto(self.xcor()+self.dx,self.ycor()+self.dy)
        self.move()

i = Image(10,10)
i.move()
