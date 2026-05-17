from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-230, 250)
        self.write("Level: 1", False, "center", font=("Courier", 15, "normal"))

    def new_level(self):
        """Updates the level scoreboard"""
        self.level += 1
        self.clear()
        self.write(
            f"Level: {self.level}", False, "center", font=("Courier", 15, "normal")
        )

    def game_over(self):
        """Prints the game over message on screen"""
        self.home()
        self.write("GAME OVER", False, "center", font=("Courier", 15, "normal"))
