import turtle
import time
import random

# 游戏基础配置
WIDTH, HEIGHT = 600, 600
DELAY = 0.15  # 移动速度，数值越小越快
SCORE = 0
HIGH_SCORE = 0

# 初始化窗口
wn = turtle.Screen()
wn.title("贪吃蛇 Snake Game")
wn.bgcolor("black")
wn.setup(WIDTH, HEIGHT)
wn.tracer(0)  # 关闭自动刷新，手动控制更流畅

# 蛇头
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# 食物
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# 计分板
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"得分: 0  最高分: 0", align="center", font=("Courier", 24, "normal"))

# 蛇身列表
segments = []

# 方向控制函数
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# 键盘绑定
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# 游戏主循环
while True:
    wn.update()

    # 检测撞墙
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # 清空蛇身
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

        # 重置分数
        SCORE = 0
        pen.clear()
        pen.write(f"得分: {SCORE}  最高分: {HIGH_SCORE}", align="center", font=("Courier", 24, "normal"))

    # 检测吃到食物
    if head.distance(food) < 20:
        # 随机生成新食物
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        # 添加蛇身
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("lightgreen")
        new_segment.penup()
        segments.append(new_segment)

        # 加分
        SCORE += 10
        if SCORE > HIGH_SCORE:
            HIGH_SCORE = SCORE
        pen.clear()
        pen.write(f"得分: {SCORE}  最高分: {HIGH_SCORE}", align="center", font=("Courier", 24, "normal"))

    # 蛇身跟随移动
    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # 检测撞到自己
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            SCORE = 0
            pen.clear()
            pen.write(f"得分: {SCORE}  最高分: {HIGH_SCORE}", align="center", font=("Courier", 24, "normal"))

    time.sleep(DELAY)

wn.mainloop()