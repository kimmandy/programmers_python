import turtle as t1
import time
import random

#스크린 사이즈
t1.setup(width=800, height=800)
t1.bgcolor('steelblue')
t1.color('orange')

#거북이 사이즈
t1.turtlesize(3)

t1.shape('turtle') #커서 모양을 거북이로 바꿔줌
t1.penup() #선을 그리지 얺도록 설정
t2 = t1.clone() #2번 거북이 (빨갱이)
t2.color('tomato')

#준비 위치
t1.goto(-400, 300)
t2.goto(-400, -300)

#속도
t1.speed(1)
t2.speed(1)

#출발하기
while True:
    t1.forward(random.randint(1, 100)) #px (픽셀 값)
    t2.forward(random.randint(1, 100)) #px (픽셀 값)

    #도착
    if t1.xcor() > 400 :
        t1.goto(0,0)
        t1.write("   winner!", font=('Arial', 20))
        break
    elif t2.xcor() >400 :
        t2.goto(0,0)
        t2.write("   winner!", font=('Arial', 20))
        break

t1.exitonclick()