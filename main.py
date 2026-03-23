from turtle import Turtle,Screen
import random
screen=Screen()
screen.setup(width=500,height=400)
colors= ["red","yellow","green","orange","purple","blue"]
user_bet= screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a colour: ")
is_race_0n= False

turtles=["t1","t2","t3","t4","t5","t6"]
turtles_pos=[150,90,30,-30,-90,-150]

for number in range(6):
    turtles[number]=Turtle(shape="turtle")
    turtles[number].penup()
    turtles[number].color(colors[number])
    turtles[number].goto(x=-230,y=turtles_pos[number])
    

 


if user_bet:
    is_race_0n= True

while is_race_0n:
    for turtle in turtles:
        random_distance= random.randint(0,10)
        turtle.forward(random_distance)
        if turtle.xcor()>230:
            is_race_0n= False
            winning_color=turtle.pencolor()
            if winning_color== user_bet:
                print(f"You've won! The {winning_color} turtle is winner")
            else:
                print(f"You've lost! The {winning_color} turtle is winner")







screen.exitonclick()
