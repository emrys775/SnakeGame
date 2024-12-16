from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.color(self.random_color())  # Assign a random color
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)

    import random

    def random_color(self):
        # Generate a random color with exactly three components
        r = random.random()  # Random float between 0 and 1
        g = random.random()  # Random float between 0 and 1
        b = random.random()  # Random float between 0 and 1
        return (r, g, b)  # Return as a tuple (r, g, b)

