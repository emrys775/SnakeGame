# main.py
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Create the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Snake Game")
screen.tracer(0)  # Turn off automatic screen updates

# Create game objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Move the snake with keyboard
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


def restart_game():
    global snake, food, scoreboard, game_is_on
    snake.reset()
    scoreboard.reset()
    game_is_on = True


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 20:  # If the distance between snake's head & food is less than 15
        # Extract the pen color (1st element of the color tuple)
        snake.extend(color=food.color()[0])  # Pass only the first color value
        food.refresh()
        scoreboard.increase_score()

    # Snake wrapping behavior for crossing the screen edges

    # Detect collision with wall edges
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.display_game_over()

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.display_game_over()

                game_is_on = False  # End the game

            choice = screen.numinput("Game Over", "Enter 1 to Restart or 2 to Quit:", minval=1, maxval=2)
            if choice == 1:
                game_is_on = True
                restart_game()
            elif choice == 2:
                screen.bye()


    # Detect collision with itself
    # for segment in snake.segments[1:]:
    #     if snake.head.distance(segment) < 10:
    #         scoreboard.display_game_over()

            # Ask the player to choose Quit or Continue

            choice = screen.numinput("Game Over", "Enter 1 to Quit or 2 to Continue:", minval=1, maxval=2)
            # if choice == 1:
            #     game_is_on = True  # Quit the game
            # elif choice == 2:
            #     #restart_game()

screen.mainloop()
