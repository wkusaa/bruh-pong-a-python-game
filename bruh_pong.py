import turtle
import winsound

def bruhSound():
    winsound.PlaySound("bruh.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)

class Border:
    def __init__(self, upper, down, left, right):
        self.upper = upper
        self.left = left
        self.right = right
        self.down = down

    def __init__(self, width, height):
        self.upper = height/2 - 10
        self.down = - (height/2 - 10)
        self.left = -(width/2 - 10)
        self.right = width/2 - 10

    def setUpper(self, upper):
        self.upper = upper

    def setDown(self, down):
        self.down = down

    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right

    def getUpper(self):
        return self.upper

    def getDown(self):
        return self.down

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right


# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# border
border = Border(800, 600)

win = turtle.Screen()
win.title("Bruh Pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

#Score
score1 = 0
score2 = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(border.getLeft()+40, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(border.getRight()-40, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1


# Line
line = turtle.Turtle()
line.speed(0)
line.shape("square")
line.color("white")
line.shapesize(stretch_wid=30, stretch_len=0.1)
line.penup()

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"->Player 1 : {score1}  Player 2: {score2}<-", align = "center", font=("Consolas", 24, "normal"))


# keyboard binding
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")



while True:
    win.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > border.getUpper():
        ball.sety(border.getUpper())
        ball.dy *= -1
        bruhSound()
        

    if ball.ycor() < border.getDown():
        ball.sety(border.getDown())
        ball.dy *= -1
        bruhSound()

    if ball.xcor() > border.getRight():
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        pen.clear()
        pen.write(f"->Player 1 : {score1}  Player 2: {score2}<-", align = "center", font=("Cascadia Code PL", 24, "normal"))
        bruhSound()

    if ball.xcor() < border.getLeft():
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        pen.clear()
        pen.write(f"->Player 1 : {score1}  Player 2: {score2}<-", align = "center", font=("Cascadia Code PL", 24, "normal"))
        bruhSound()

    # paddble b collide
    if ball.xcor() > border.getRight()-50 and (ball.ycor() < paddle_b.ycor() + 50
                              and ball.ycor() > paddle_b.ycor() - 50):
        ball.dx *= -1
        ball.setx(border.getRight()-50)
        bruhSound()

    # paddle a collide
    if ball.xcor() < border.getLeft()+50 and (ball.ycor() < paddle_a.ycor() + 50
                               and ball.ycor() > paddle_a.ycor() - 50):
        ball.dx *= -1
        ball.setx(border.getLeft()+50)
        bruhSound()

    