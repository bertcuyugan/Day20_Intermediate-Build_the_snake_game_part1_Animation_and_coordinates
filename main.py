from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# for the snake to follow each one without delay
screen.tracer(0)
snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")




# better ways of doing the below positioning using tuple
# starting_positions = [(0, 0), (-20, 0), (-40, 0)]

# snake to move
segments = []

# for position in starting_positions:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)

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

    snake.move()


    # for seg_num in range(len(segments) - 1, 0, -1):
    #     new_x = segments[seg_num - 1].xcor()
    #     new_y = segments[seg_num - 1].ycor()
    #     segments[seg_num].goto(new_x, new_y)
    # segments[0].forward(20)

screen.exitonclick()
