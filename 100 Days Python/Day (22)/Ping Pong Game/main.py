from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Abe's New Age Pong")

# Turn off automatic screen updates
screen.tracer(0)

r_paddle = Paddle((350, 0))
r_paddle.color("green")
l_paddle = Paddle((-350, 0))
l_paddle.color("blue")
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Main game loop
game_is_on = True
while game_is_on:
    # Update the screen manually
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Your game logic here, bounce in to the screen logic
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # collision with right and left paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # no collision or missed collision with right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.r_point()
    # no collision or missed collision with left paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.l_point()
# Close the window when the game is finished
screen.exitonclick()
