#기본 함수 형태
def add_num(a,b):
    res = a+b
    return res
print(add_num(10, 20))


#결과값이 없는 함수
def div_num(a, b):
    res = a / b
    print("나눗셈 결과", res)
div_num(10,20)

#매개변수가 없는 함수
import random
def get_random_number():
    res = random.randint(1, 100)
    return res
print(get_random_number())


#결과값, 매개변수가 없는 함수
def say_hello():
    print("안녕하세요!")
    print("반갑습니다!")
say_hello()