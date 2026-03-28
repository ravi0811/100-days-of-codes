from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(5,1)
        self.goto(position)

    def go_up(self):
        new_y=self.ycor()+20
        self.goto(x=self.xcor(),y=new_y)
    def go_down(self):
        new_y=self.ycor()-20
        self.goto(x=self.xcor(),y=new_y)



