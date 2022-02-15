import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)
screen.listen()

turtle = Player()
screen.onkey(turtle.move_up, "Up")

cars = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.4)
    screen.update()

    cars.create_car()
    cars.move_cars()

    # Detect turtle collision with cars
    for car in cars.all_cars:
        if car.distance(turtle) < 22:
            game_is_on = False
            scoreboard.display_game_over()

    # Detect if turtle reached finished line
    if turtle.is_finish_line_reached():
        turtle.goto_start_position()
        cars.level_up()
        scoreboard.level_up()

screen.exitonclick()
