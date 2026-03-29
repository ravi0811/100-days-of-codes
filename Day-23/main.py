import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player= Player()
car_manager= CarManager()
scoreboard= Scoreboard()

screen.listen()
screen.onkey(player.go_up,"Up")
counter=0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if counter==6:
        car_manager.create_cars()
        counter=0

    counter+=1
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player)<20:
            game_is_on=False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
screen.exitonclick()
