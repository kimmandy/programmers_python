# #문제24
# a = int(input("현재 구독자 수: "))
# b = int(input("시청시간: "))

# #논리연산 AND
# if a >=1000 and b >=4000 :
#     print("수익 창출 가능")
# else :
#     print("수익 창출 불가능")


# #문제25
# a = int(input("팔굽혀펴기: "))
# b = int(input("윗몸일으키기: "))
# c = int(input("턱걸이: "))

# #논리연산 OR
# if a >=30 or b >=35 or c >=5 :
#     print("pass")
# else :
#     print("fail")


# #문제26
# a = int(input("필기시험 점수를 입력하세요: "))

# if a >= 80:
#     b = input("면접결과를 입력하세요: ")
#     if b == 'pass':
#         print("최종합격")
#     elif b == 'fail':
#         print("불합격")
# else :
#     print("불합격")


# #문제27
# for i in range(5):
#     for j in range(i+1):
#         print("*", end=' ')
#     print()


# #문제28
# for i in range(5):
#     for j in range(5-i):
#         print("*", end=' ')
#     print()



# #문제29
# for i in range(5):
#     for j in range(4-i):
#         print(" ", end='')
#     for j in range(2*(i+1)-1):
#         print('*', end='')
#     print()


#문제30
while True :
    print("[메뉴를 입력하세요]")
    a = int(input("1.게임시작 2.랭킹보기 3.게임종료 >>>"))
    if a == 1:
        print("게임을 시작합니다.")
    elif a==2:
        print("실시간 랭킹")
    elif a==3:
        print("게임을 종료합니다.")
        break
    else :
        print("다시 입력해 주세요")