from time import sleep
from turtle import Screen
from paddle import Paddle
from ball import Ball


screen = Screen()
screen.title("The Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))

ball = Ball()

screen.listen()
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

game_on = True

while game_on:
    sleep(0.1)
    screen.update()
    ball.move()

    # Hit the upper and lower walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

screen.exitonclick()
