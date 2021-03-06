from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import Score

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
is_on = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

# Detect collision with food
    if snake.head.distance(food) < 15:
        food.ref()
        snake.extend()
        score.inc()

# Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.game_over()
        is_on = False


# Detect collision with tail
    for seg in snake.segment[1:]:
        if snake.head.distance(seg) < 10:
            is_on = False
            score.game_over()

screen.exitonclick()