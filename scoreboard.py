from turtle import Turtle

FONT = ("Courier", 20, "bold")
ALIGN = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setpos(-220, 250)
        self.level = 1
        self.display_level()

    def level_up(self):
        self.level += 1
        self.display_level()

    def display_level(self):
        self.clear()
        self.write(f"Level {self.level}", False, ALIGN, FONT)

    def display_game_over(self):
        self.setpos(0, 0)
        self.write(f"GAME OVER", False, ALIGN, FONT)
