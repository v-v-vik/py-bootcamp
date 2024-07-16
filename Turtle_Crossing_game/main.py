from turtle import Screen
from car_manager import Car_manager
import time
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.title("Turtle Crossing")
screen.tracer(0)
car_manager = Car_manager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.go_forward, "w")
screen.onkeypress(player.go_backwards, "s")



game_on = True
while game_on:
    screen.update()
    time.sleep(car_manager.speed)

    car_manager.create_cars()
    car_manager.move_cars()

    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.add_score()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_on = False
            scoreboard.game_over()




screen.exitonclick()