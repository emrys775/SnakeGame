from turtle import Turtle

#from main import game_is_on

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(
            f"Score: {self.score}  High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
        self.update_score()

    def get_high_score(self):
        try:
            with open("data.txt") as file:
                content = file.read().strip()
                return int(content) if content.isdigit() else 0
        except FileNotFoundError:
            return 0

    def save_high_score(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))

    def display_game_over(self):
         pass
        # self.goto(0, 0)
        # self.write("GAME OVER", align=ALIGNMENT, font=("Courier", 24, "bold"))


