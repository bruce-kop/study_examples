import turtle as t

t.pensize(2)
t.speed(1)     #设置画画的速率
t.colormode(255)
t.pencolor("black")
t.begin_fill()
#房顶
t.fillcolor(0,245,255)

for i in range(3):

    t.forward(240)

    t.left(120)

t.end_fill()

#房顶阁楼窗户外框

t.penup()

t.goto(80,20)

t.pendown()

t.begin_fill()

t.fillcolor("white")

for i in range(4):

    t.forward(80)

    t.left(90)

t.end_fill()

#阁楼窗户内部的横线

t.penup()

t.goto(80,60)

t.pendown()

t.forward(80)

#阁楼窗户内部的竖线

t.penup()

t.goto(120,100)

t.pendown()

t.right(90)

t.forward(80)

t.right(90)

t.forward(80)

#房屋主体

t.left(90)

t.penup()

t.goto(0,0)

t.pendown()

t.begin_fill()

t.fillcolor(255,165,0)

for i in range(2):

    t.forward(240)

    t.left(90)

    t.forward(240)

    t.left(90)

t.end_fill()

#屋门

t.penup()

t.goto(30,-130)

t.pendown()

t.begin_fill()

t.fillcolor("blue")

for i in range(2):

    t.forward(100)

    t.left(90)

    t.forward(80)

    t.left(90)

t.end_fill()

#窗框

t.penup()

t.goto(140,-90)

t.pendown()

t.begin_fill()

t.fillcolor("white")

for i in range(4):

    t.forward(70)

    t.left(90)

t.end_fill()

#窗户上的竖线

t.penup()

t.goto(175,-90)

t.pendown()

t.left(90)

t.forward(70)

t.hideturtle()
t.mainloop()