from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

WALL_CHECK_AT = 280

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0, 1)
snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.update()
game_is_on = True
score.writer()
while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()

    # score
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.change_score()

    # wall collision
    if snake.head.xcor() > WALL_CHECK_AT or snake.head.xcor() < -1 * WALL_CHECK_AT or snake.head.ycor() > WALL_CHECK_AT or snake.head.ycor() < -1 * WALL_CHECK_AT:
        game_is_on = False
        score.game_over()

    # tail collision
    for segment in snake.turtles[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
