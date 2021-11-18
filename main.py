# Importing all the required module
from snake import Snake
from turtle import Turtle, Screen
import time
from food import Food
from scoreboard import ScoreBoard
# Setup screen its width and height
my_screen = Screen()
my_screen.title(titlestring="Snake Game")
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.tracer(0)

# Position for first three square of snake
# Creating Three Square and storing its objects in segment list

new_snake = Snake()
foo = Food()
board = ScoreBoard()

# Listen keys
my_screen.listen()
my_screen.onkey(new_snake.up,"Up")
my_screen.onkey(new_snake.down,"Down")
my_screen.onkey(new_snake.left,"Left")
my_screen.onkey(new_snake.right,"Right")
# For moving forward
race_is_on = True
while race_is_on:
    my_screen.update()
    time.sleep(0.1)
    new_snake.move()
    # Detect collision with food
    if new_snake.head.distance(foo) < 15:
        score = foo.refresh()
        new_snake.extend()
        board.increment(score)
    # Detect if collision with the wall
    if new_snake.head.xcor() > 280 or new_snake.head.xcor() < -280 or new_snake.head.ycor() > 280 or new_snake.head.ycor() < -280:
        race_is_on = False
        board.gameover()

    # Detect collision with tail
    for segment in new_snake.segments:
        if segment == new_snake.head:
            pass
        elif new_snake.head.distance(segment) < 10:
            race_is_on = False
            board.gameover()
my_screen.exitonclick()
# Yeah and it's done my first game completly compied i know