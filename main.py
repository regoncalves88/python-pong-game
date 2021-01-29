from time import sleep
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.title("The Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

game_on = True

while game_on:
    sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # Hit the upper and lower walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    # Hit the Paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()

    if ball.xcor() > 380:
        scoreboard.left_scored()
        ball.reset()

    if ball.xcor() < -380:
        scoreboard.right_scored()
        ball.reset()

screen.exitonclick()