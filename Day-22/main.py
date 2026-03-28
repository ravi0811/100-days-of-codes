from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

#-----screen section0-----
screen= Screen()
screen.tracer(0)
screen.setup(width=800,height=600)
screen.bgcolor("black")

#-----initializtion
r_paddle= Paddle((350,0))
l_paddle= Paddle((-350,0))
ball= Ball()
#-----movement control-----
screen.listen()
screen.onkey(key="Up",fun=r_paddle.go_up)
screen.onkey(key="Down",fun=r_paddle.go_down)
screen.onkey(key="w",fun=l_paddle.go_up)
screen.onkey(key="s",fun=l_paddle.go_down)


#-----gameloop-----
game_is_on= True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()>-320:
        ball.bounce_x()
    

screen.exitonclick()
