"""This program uses python's turtle module to create the snake game. By JBAmenorfe on 11.01.2025"""

from turtle import Screen
from scoreboard import ScoreBoard
from snake import Snake
from food import Food
from gamefield import GameField
import time

TOP_BOUNDARY = 240
LEFT_BOUNDARY = -280
BOTTOM_BOUNDARY = -275
RIGHT_BOUNDARY = 275

# Create Screen object
screen = Screen()
screen.setup(width=600, height=600)  # Set the screen width and height
screen.bgcolor("black")  # Set the screen background color to black
screen.title("The Snake Game")  # Set the screen title
screen.tracer(0)  # Turn off the tracer function of the screen

# Create a snake object
snake = Snake()

# Create the food object
food = Food()

# Create the scoreboard object
scoreboard = ScoreBoard()

# Create a gamefield object
gamefield = GameField()

# Call the screen.listen() method
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

# screen.update()         # Redraws the screen to show the snake body at once
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # Detect snake's heard's collission with food
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    if snake.snake_head.xcor() > RIGHT_BOUNDARY or snake.snake_head.xcor() < LEFT_BOUNDARY or snake.snake_head.ycor() > TOP_BOUNDARY or snake.snake_head.ycor() < BOTTOM_BOUNDARY:
        scoreboard.reset()
        snake.reset()
        scoreboard.save_score_data()

    # Detect collision with tail
    for segment in snake.snake_body[1:]:
        if snake.snake_head.distance(segment) < 5:
            scoreboard.reset()
            snake.reset()
            scoreboard.save_score_data()

# Call the exitonclick() method
screen.exitonclick()
