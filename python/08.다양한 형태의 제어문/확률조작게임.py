#후후후 애송이.... 어서 오시게

import turtle as t
import random
import time

#가로 800, 세로 800 배경변경
t.setup(width=800, height=800)
t.shape('turtle')
t.color('white')
t.bgcolor('steelblue')

#중앙선
t.goto(0, 400)
t.goto(0, -400)
t.goto(0, 0)

#속도 변경
t.speed(1)

#펜 올리기
t.penup()

left = int(input("왼쪽 배팅 금액(원): "))
right = int(input("왼쪽 배팅 금액(원): "))


for i in range(10):
    #배팅 금액이 둘중에 하나라도 100만원 이상일 경우
    if left >= 1000000 or right>=1000000:
        #확률조작
        if left > right :
            t.forward(random.randint(-30, 60))
        else :
            t.forward(random.randint(-60, 30))
    else:
        t.forward(random.randint(-50, 50))
    time.sleep(1)

#거북이의 x좌표가 0보다 크다면    
if t.xcor() > 0:
    t.write("turtle goes right", font=('Arial', 16))
elif t.xcor() < 0:
    t.write("turtle goes left", font=('Arial', 16))

#화면 클릭 되었을 때 종료
t.exitonclick()