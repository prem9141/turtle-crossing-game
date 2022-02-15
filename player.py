from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 300


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto_start_position()

    def move_up(self):
        if self.ycor() <= FINISH_LINE_Y:
            self.forward(MOVE_DISTANCE)

    def is_finish_line_reached(self):
        return self.ycor() > FINISH_LINE_Y

    def goto_start_position(self):
        self.setpos(STARTING_POSITION)
        self.setheading(90)


