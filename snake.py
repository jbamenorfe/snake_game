from turtle import Turtle
START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.snake_head = self.snake_body[0]

    def create_snake(self):
        # Create a turtle object with a square shape
        self.snake_body = []
        for position in START_POSITIONS:
            new_body_segment = Turtle("square")
            new_body_segment.color("white")
            new_body_segment.penup()
            new_body_segment.goto(position)
            self.snake_body.append(new_body_segment)

    # Define a method to move the snake
    def move(self):
        for segment_number in range(len(self.snake_body) - 1, 0, -1):
            new_x_position = self.snake_body[segment_number - 1].xcor()
            new_y_position = self.snake_body[segment_number - 1].ycor()
            self.snake_body[segment_number].goto(new_x_position, new_y_position)
        self.snake_head.forward(MOVE_DISTANCE)

    # Define a method to turn the snake upwards
    def up(self):
        if not self.snake_head.heading() == DOWN:
            self.snake_head.setheading(UP)

    # Define a method to turn the snake downwards
    def down(self):
        if not self.snake_head.heading() == UP:
            self.snake_head.setheading(DOWN)

    # Define a method to turn the snake right
    def right(self):
        if not self.snake_head.heading() == LEFT:
            self.snake_head.setheading(RIGHT)

    # Define a method to turn the snake left
    def left(self):
        if not self.snake_head.heading() == RIGHT:
            self.snake_head.setheading(LEFT)