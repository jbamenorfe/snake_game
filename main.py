"""This program uses python's turtle module to create the snake game. By JBAmenorfe on 11.01.2025"""

from turtle import Screen
from snake import Snake
import time

# Create Screen object
screen = Screen()
screen.setup(width=600, height=600)     # Set the screen width and height
screen.bgcolor("black")                 # Set the screen background color to black
screen.title("The Snake Game")          # Set the screen title
screen.tracer(0)                        # Turn off the tracer function of the screen

# Create a snake object
snake = Snake()

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









# Call the exitonclick() method
screen.exitonclick()