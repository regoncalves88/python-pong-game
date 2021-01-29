from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_direction = 10
        self.y_direction = 10
        self.ball_speed = 0.1

    def move(self):
        new_x_pos = self.xcor() + self.x_direction
        new_y_pos = self.ycor() + self.y_direction
        self.setposition(new_x_pos, new_y_pos)

    def bounce_wall(self):
        self.y_direction *= -1

    def bounce_paddle(self):
        self.x_direction *= -1
        self.ball_speed *= 0.9

    def reset(self):
        self.setposition(0, 0)
        self.bounce_paddle()
        self.ball_speed = 0.1
