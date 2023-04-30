from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# for the snake to follow each one without delay
screen.tracer(0)

# better ways of doing the below positioning using tuple
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

# snake to move
snakes = []

for position in starting_positions:
    new_snake = Turtle("square")
    new_snake.color("white")
    new_snake.penup()
    new_snake.goto(position)
    snakes.append(new_snake)

# snake_1 = Turtle("square")
# snake_1.color("white")
#
# snake_2 = Turtle("square")
# snake_2.color("white")
# snake_2.goto(x=-20, y=0)
#
# snake_3 = Turtle("square")
# snake_3.color("white")
# snake_3.goto(x=-40, y=0)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for snake_num in range(len(snakes) - 1, 0, -1):
        new_x = snakes[snake_num - 1].xcor()
        new_y = snakes[snake_num - 1].ycor()
        snakes[snake_num].goto(new_x, new_y)
    snakes[0].forward(20)

screen.exitonclick()
